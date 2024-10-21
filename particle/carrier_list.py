import ROOT
ROOT.gROOT.SetBatch(True)
class CarrierListFromG4P:
    def __init__(self, material, my_g4p, batch):
        """
        Description:
            Events position and energy depositon
        Parameters:
            material : string
                deciding the energy loss of MIP
            my_g4p : Particles
            batch : int
                batch = 0: Single event, select particle with long enough track
                batch != 0: Multi event, assign particle with batch number
        Modify:
            2022/10/25
        """
        if (material == "SiC"):
            self.energy_loss = 8.4 #ev
        elif (material == "Si"):
            self.energy_loss = 3.6 #ev

        if batch == 0 and my_g4p.geant4_model == "time_resolution":
            total_step=0
            particle_number=0
            for p_step in my_g4p.p_steps_current:   # selecting particle with long enough track
                if len(p_step)>1:
                    particle_number=1+particle_number
                    total_step=len(p_step)+total_step
            for j in range(len(my_g4p.p_steps_current)):
                if(len(my_g4p.p_steps_current[j])>((total_step/particle_number)*0.5)):
                    self.batch_def(my_g4p,j)
                    my_g4p.selected_batch_number=j
                    break
            if particle_number > 0:
                batch=1

            if batch == 0:
                print("=========RASER info ===========\nGeant4:the sensor didn't have particles hitted\n==========================")
                raise ValueError
            
        elif batch == 0 and my_g4p.geant4_model == "Si_strip":
            # P13 cut condition
            h1 = ROOT.TH1F("Edep_device", "Energy deposition in Detector", 100, 0, max(my_g4p.edep_devices)*1.1)
            for i in range (len(my_g4p.edep_devices)):
                h1.Fill(my_g4p.edep_devices[i])
            max_event_bin=h1.GetMaximumBin()
            bin_wide=max(my_g4p.edep_devices)*1.1/100
            c=ROOT.TCanvas("c","c",700,500)
            h1.Draw()
            # c.SaveAs("./output/particle/edeptest.pdf")

            for j in range (len(my_g4p.edep_devices)):
                #compare to experimental data
                if (my_g4p.edep_devices[j]<0.084 and my_g4p.edep_devices[j]>0.083):
                    try_p=1
                    for single_step in my_g4p.p_steps_current[j]:
                        if abs(single_step[0]-my_g4p.p_steps_current[j][0][0])>5:
                            try_p=0
                    if try_p==1:
                        self.batch_def(my_g4p,j)
                        my_g4p.selected_batch_number=j
                        batch = 1
                        break
        else:
            self.batch_def(my_g4p,batch)

    def batch_def(self,my_g4p,j):
        self.beam_number = j
        self.track_position = [[single_step[0],single_step[1],single_step[2],1e-9] for single_step in my_g4p.p_steps_current[j]]
        self.tracks_step = my_g4p.energy_steps[j]
        self.tracks_t_energy_deposition = my_g4p.edep_devices[j] #为什么不使用？
        self.ionized_pairs = [step*1e6/self.energy_loss for step in self.tracks_step]
    