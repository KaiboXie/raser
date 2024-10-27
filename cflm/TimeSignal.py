import os
import re
import numpy
import ROOT
import json
import multiprocessing
from . import get_signal
from elec.set_pwl_input import set_pwl_input as pwlin
import subprocess

def TimeSignal():
    file = ROOT.TFile("raser/cflm/output/DataFile.root", "READ")
    tree = file.Get("electrons")

    pos, mom, energy, time = [], [], [], []

    def worker_function(queue, lock, j):
       try:
           print(f"运行 loop_solver:{j}")
           result_message = "Execution completed successfully"
           get_signal.get_signal()
       except Exception as e:
           result_message = f"Error: {e}"
       with lock:
            queue.put(result_message)
  
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()

    for i in range(tree.GetEntries()):

        tree.GetEntry(i)
        pos.append([tree.pos_x, tree.pos_y, tree.pos_z])
        mom.append([tree.px, tree.py, tree.pz])
        energy.append(tree.s_energy)
        time.append(tree.time)
    
    for j in range(tree.GetEntries()):     
        with open('./setting/absorber/cflm.json', 'r') as file:
                g4_dic = json.load(file)    
                g4_dic['par_in']      = [pos[j]]
                g4_dic['par_direct']  = [mom[j]]
                g4_dic['par_energy']  = [energy[j]]
                g4_dic['CurrentName'] = f"TimeSignal_{j}_tmp.root"     
                updated_g4_dic = json.dumps(g4_dic, indent=4)
        
        with open('./setting/absorber/cflm.json', 'w') as file:
                
                file.write(updated_g4_dic)
        p = multiprocessing.Process(target=worker_function, args=(queue, lock, j))

        p.start()
        p.join()
        while not queue.empty():
            output_info = queue.get() 
            print("队列输出:", output_info)  # 确认输出内容
            if output_info is None:
                print("警告: worker_function 返回了 None,可能发生了错误!")
        
        
        current_path = f'raser/cflm/output/TimeSignal_{j}_tmp_pwl_current.txt'
        if os.path.exists(current_path):
            
            with open(current_path, 'r') as file_oldtxt:
                    
                    lines = file_oldtxt.readlines()
                    new_lines = []
                    for line in lines:
                        parts = line.split()  
                        if len(parts) > 0:
                            txttime = float(parts[0])  
                            txttime_new = txttime + time[j]*1e-9  
                            new_line = str(txttime_new) + ' ' + ' '.join(parts[1:])  
                            new_lines.append(new_line)

            with open(current_path, 'w') as file_newtxt:
                    for line in new_lines:
                        file_newtxt.write(line + '\n')
        
        else:
            print("No secondary particles hit the beam pipe, no current file generated")
            
        print(f'tmp_{j} has benn created')
       
    output_path = "raser/cflm/output"
    pattern = re.compile(r"TimeSignal_(\d+)_tmp_pwl_current.txt")

    particleNo, time, current = [], [], []

    for filename in os.listdir(output_path):
        if pattern.match(filename):
           j = int(pattern.match(filename).group(1))
           particleNo.append(j)

    particleNo.sort()

    for i in particleNo:

        file_str = f'raser/cflm/output/TimeSignal_{i}_tmp_pwl_current.txt'

        with open(file_str, 'r') as current_file:
             for line in current_file:
                 columns = line.strip().split(' ')       
                 time.append(columns[0])
                 current.append(columns[1])

    total_current_path = "raser/cflm/output/TimeSignalTotalCurrent.txt"
    with open(total_current_path, 'w') as output_file:
         for t, c in zip(time, current):
             output_file.write(f"{t} {c}\n")

    with open('raser/cflm/output/TimeSignalTotalCurrent.txt', 'r') as file:
         lines = file.readlines()

    sorted_lines = sorted(lines, key=lambda x: float(x.split()[0]))

    with open('raser/cflm/output/TimeSignalTotalCurrentSorted.txt', 'w') as file:
        for line in sorted_lines:
            file.write(line)
    
    pwlin(f"raser/cflm/output/TimeSignalTotalCurrentSorted.txt", 'raser/cflm/ucsc.cir', 'raser/cflm/output/')
    subprocess.run([f"ngspice -b -r ./xxx.raw raser/cflm/output/ucsc_tmp.cir"], shell=True) 

    file_name_v = 'Current_test.raw'
    file_name_c = 'TimeSignalTotalCurrentSorted.txt'
    
    time_v, volt = TimeSignalVoltage(output_path,file_name_v)
    length_v = len(time_v)
    time_c, curr = TimeSignalCurrent(output_path,file_name_c)
    length_c = len(time_c)

    ROOT.gROOT.SetBatch()
        
    c1 = ROOT.TCanvas('c1','c1',4000,2000)
    f1 = ROOT.TGraph(length_c, time_c, curr)
    f1.SetTitle(' ')
    f1.SetLineColor(2)
    f1.SetLineWidth(2)
    f1.GetXaxis().SetTitle('Time [us]')
    f1.GetXaxis().SetLimits(0,65)
    f1.GetXaxis().CenterTitle()
    f1.GetXaxis().SetTitleSize(0.05)
    f1.GetXaxis().SetTitleOffset(0.8)
    f1.GetYaxis().SetTitle('Current [uA]')
    f1.GetYaxis().SetTitleOffset(1.2)
    f1.GetYaxis().SetLimits(0,-5)
    f1.GetYaxis().CenterTitle()
    f1.GetYaxis().SetTitleSize(0.07)
    f1.GetYaxis().SetTitleOffset(0.7)
    f1.Draw('AL')
    c1.SaveAs("raser/cflm/output/TimeSignalCurrent.pdf")

    c2 = ROOT.TCanvas('c2','c2',4000,2000)
    f2 = ROOT.TGraph(length_v, time_v, volt)
    f2.SetTitle(' ')
    f2.SetLineColor(2)
    f2.SetLineWidth(2)
    f2.GetXaxis().SetTitle('Time [us]')
    f2.GetXaxis().SetLimits(0,65)
    f2.GetXaxis().CenterTitle()
    f2.GetXaxis().SetTitleSize(0.05)
    f2.GetXaxis().SetTitleOffset(0.8)
    f2.GetYaxis().SetTitle('Voltage [mV]')
    f1.GetYaxis().SetTitleOffset(1.2)
    f2.GetYaxis().SetLimits(0,-5)
    f2.GetYaxis().CenterTitle()
    f2.GetYaxis().SetTitleSize(0.07)
    f2.GetYaxis().SetTitleOffset(0.7)
    f2.Draw('AL')
    c2.SaveAs("raser/cflm/output/TimeSignalVoltage.pdf")
    
    c3 = ROOT.TCanvas("c3", "Histogram", 800, 600)
    hist = ROOT.TH1F("hist", "Edep", 30, 0, 30)

    hist.SetXTitle("Energy deposition(MeV)")
    hist.SetYTitle("Events/{:.3f}".format((30 - 0) / 30))

    with open('raser/cflm/output/TimeSignalEdep.txt', 'r') as file:
         for line in file:
             value = float(line.strip())
             if value != 0:
                hist.Fill(value)

    hist.Draw()
    c3.Update()
    c3.SaveAs('raser/cflm/output/TimeSignalEdep.pdf')
    
def TimeSignalVoltage(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time_v,volt = [],[]

        for line in lines:
            time_v.append(float(line.split()[0])*1e6)
            volt.append(float(line.split()[1])*1e3)

    time_v = numpy.array(time_v ,dtype='float64')
    volt = numpy.array(volt,dtype='float64')

    return time_v,volt

def TimeSignalCurrent(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time_c,curr = [],[]

        for line in lines:
            time_c.append(float(line.split()[0])*1e6)
            curr.append(float(line.split()[1])*1e6)

    time_c = numpy.array(time_c ,dtype='float64')
    curr = numpy.array(curr, dtype='float64')

    return time_c, curr
    