import os
import re
import ROOT
import json
import multiprocessing
import subprocess
from . import cflm_dsides
from . import get_signal_dsides
from . import time_signal
from gen_signal import build_device as bdv
from elec.set_pwl_input import set_pwl_input as pwlin
import random
import array
import math
import statistics

def main():
    
    random.seed(3020122)
    
    rand = ROOT.TRandom3()
    average_hit = 3.4
    total_samples = 100000
    hitnumber = []

    for i in range(total_samples):
        hitnumber.append(rand.Poisson(average_hit))
    std_dev = statistics.stdev(hitnumber)
    
    hist = ROOT.TH1F("hist", "One-Dimensional Histogram", 10000, -5, 15)

    for num in hitnumber:
        hist.Fill(num)

    canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)
    hist.Draw()

    canvas.SaveAs("raser/cflm/output/dSides/PoiTimeSignal/PossionHitData.pdf")
    
    with open('./setting/absorber/cflm_dsides.json', 'r') as p:
         g4_dic = json.load(p)
    
    detector_json = "./setting/detector/"
    with open(os.path.join(detector_json, g4_dic['DetModule'])) as q:
         det_dic = json.load(q)
    
    det_name = det_dic['det_name']
    my_d = bdv.Detector(det_name)

    file = ROOT.TFile("raser/cflm/output/DataFile.root", "READ")
    tree = file.Get("electrons")

    pos, mom, energy = [], [], []
    TotalHitInfo = [] 
    
    for i in range(tree.GetEntries()):

        tree.GetEntry(i)
        pos.append([tree.pos_x, tree.pos_y, tree.pos_z])
        mom.append([tree.px, tree.py, tree.pz])
        energy.append(tree.s_energy) 

    for k in range(len(pos)):
        TotalHitInfo.append([pos[k], mom[k], energy[k]])
    
    random.shuffle(TotalHitInfo)
    
    #sampleNumber = 268*3+16
    
    sampleNumber = 10
    
    randomhit = random.sample(hitnumber, sampleNumber)
    '''
    # create time label
    time_label  = []
    for i in range(268):     #268 is the number of bunch for half ring
        time_label.append(i*600)   #round1 finish
    for j in range(268):
        time_label.append(330000+j*600)  #round2 finish
    for k in range(268):
        time_label.append(660000+k*600)  #round3 finish
    for l in range(16):
        time_label.append(990000+l*600)  #10us bunch

    random.shuffle(time_label)
    '''

    nCount = 0
    with open('raser/cflm/output/dSides/PoiTimeSignal/PossionHit.txt', 'w') as PossionHitFile:      
         for i in range(len(randomhit)):
             if randomhit[i] == 0:
                  PossionHitFile.write(f'{randomhit[i]} {999} {nCount*10}\n')
             else:
                  randomHitInfo = random.sample(TotalHitInfo, randomhit[i])
                  PossionHitFile.write(f'{randomhit[i]} {randomHitInfo} {nCount*10}\n')
             nCount+=1
    
    def worker_function(queue, lock, j):
        try:
            print(f"运行 loop_solver:{j}")
            result_message = "Execution completed successfully"
            get_signal_dsides.main()
        except Exception as e:
            result_message = f"Error: {e}"
        with lock:
            queue.put(result_message)
  
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    
    HitTimeList = []
    with open('raser/cflm/output/dSides/PoiTimeSignal/PossionHit.txt', 'r') as Hit_input_file:
         for line in Hit_input_file:
              pos, mom, energy = [], [], []
              match = re.match(r'(\d+) (\[.*\]) (\d+)', line)
              if match:
                   hitEvents = match.group(1)
                   pos_mom_energy = match.group(2)
                   pos_mom_energy_list = eval(pos_mom_energy)
                   hitTime = int(match.group(3))
                   HitTimeList.append(hitTime)
                   if int(hitEvents) == 0:
                        print('No hit events')
                   else:
                        for ele in pos_mom_energy_list:
                            pos.append(ele[0])
                            mom.append(ele[1])
                            energy.append(ele[2])
                   with open('./setting/absorber/cflm_dsides.json', 'r') as file:
                            g4_dic = json.load(file)    
                            g4_dic['NumofGun']    = int(hitEvents)
                            g4_dic['par_in']      = pos
                            g4_dic['par_direct']  = mom
                            g4_dic['par_energy']  = energy
                            g4_dic['CurrentName'] = f"PoiTimeSignal/PoiTimeSignal_{hitTime}.root"
                            g4_dic['PosBaseName'] = f"SecondaryParticle_{hitTime}.txt"     
                            updated_g4_dic = json.dumps(g4_dic, indent=4)
                
                   with open('./setting/absorber/cflm_dsides.json', 'w') as file:
                        file.write(updated_g4_dic)
    
                   p = multiprocessing.Process(target=worker_function, args=(queue, lock, line))
                   p.start()
                   p.join()
                    
                   while not queue.empty():
                        output_info = queue.get() 
                        print("队列输出:", output_info)  # 确认输出内容
                        if output_info is None:
                           print("警告: worker_function 返回了 None,可能发生了错误!")
    
    
    HitTimeList = [0, 10, 20, 40, 50, 60, 70, 80, 90]    ################ it should be deleted for the entire run ############################

    for count in HitTimeList:
        for i in ('I', 'II'):
            current_path = f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignal_{count}_Current_{i}.txt'
            with open(current_path, 'r') as file_oldtxt:      
                 lines = file_oldtxt.readlines()
                 new_lines = []
                 for line in lines:
                     parts = line.split()  
                     if len(parts) > 0:
                        txttime = float(parts[0])  
                        txttime_new = txttime + count*1e-9  
                        new_line = str(txttime_new) + ' ' + ' '.join(parts[1:])  
                        new_lines.append(new_line)
            with open(current_path, 'w') as file_newtxt:
                 for line in new_lines:
                     file_newtxt.write(line + '\n')
    
    output_path = "raser/cflm/output/dSides/PoiTimeSignal/"
    
    pattern_I = re.compile(r"PoiTimeSignal_(\d+)_Current_I.txt")
    pattern_II = re.compile(r"PoiTimeSignal_(\d+)_Current_II.txt")
    
    HitNo_I, time_tmp_I, current_I = [], [], []
    HitNo_II, time_tmp_II, current_II = [], [], []

    for filename in os.listdir(output_path):
        if pattern_I.match(filename):
            j = int(pattern_I.match(filename).group(1))
            HitNo_I.append(j)
        elif pattern_II.match(filename):
            k = int(pattern_II.match(filename).group(1))
            HitNo_II.append(k)

    HitNo_I.sort()
    HitNo_II.sort()
    
    for i in HitNo_I:
        file_str = f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignal_{i}_Current_I.txt'
        with open(file_str, 'r') as current_file:
            for line in current_file:
                columns = line.strip().split(' ')       
                time_tmp_I.append(columns[0])
                current_I.append(columns[1])
        total_current_path_I = "raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrent_I.txt"
        with open(total_current_path_I, 'w') as output_file:
             for t, c in zip(time_tmp_I, current_I):
                 output_file.write(f"{t} {c}\n")

    for i in HitNo_II:
        file_str = f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignal_{i}_Current_II.txt'
        with open(file_str, 'r') as current_file:
            for line in current_file:
                columns = line.strip().split(' ')       
                time_tmp_II.append(columns[0])
                current_II.append(columns[1])
        total_current_path_II = "raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrent_II.txt"
        with open(total_current_path_II, 'w') as output_file:
             for t, c in zip(time_tmp_II, current_II):
                 output_file.write(f"{t} {c}\n")
    
    for k in ('I', 'II'):
        with open(f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrent_{k}.txt', 'r') as file:
            lines = file.readlines()
            sorted_lines = sorted(lines, key=lambda x: float(x.split()[0]))

        with open(f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrentSorted_{k}.txt', 'w') as file:
            for line in sorted_lines:
                file.write(line)
    
        pwlin(
                f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrentSorted_{k}.txt', 
                'raser/cflm/ucsc.cir',
                f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalVoltage_{k}.raw',
                'raser/cflm/output/dSides/PoiTimeSignal/'
              )
        
        subprocess.run([f"ngspice -b -r ./xxx.raw raser/cflm/output/dSides/PoiTimeSignal/ucsc_tmp.cir"], shell=True)

        time_signal.TimeSignalPlot(
                                    f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrent_{k}.txt',
                                    f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalVoltage_{k}.raw',
                                    f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalCurrent_{k}.pdf',
                                    f'raser/cflm/output/dSides/PoiTimeSignal/PoiTimeSignalTotalVoltage_{k}.pdf',
                                    1e9,
                                    100,
                                    2000,
                                    1600
                                  )
    
    digsignal = []
    print("***************************************************")
    for p in range(sampleNumber):
        time_lab = p*10
        if (not os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) and (not os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))):
           digsignal.append([time_lab, 0])
        
        elif (os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) and (not os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))):
            volt_I = []
            with open(os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) as volt_file_I:
                for line in volt_file_I:
                    columns = line.split()  
                    volt_I.append(float(columns[1]))
            volt_I_max = max(volt_I)
            if volt_I_max > 5e-3:
               digsignal.append([time_lab, 1])
            else:
               digsignal.append([time_lab, 0]) 
        elif (not os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) and (os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))):
            volt_II = []
            with open(os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))) as volt_file_II:
                for line in volt_file_II:
                    columns = line.split()  
                    volt_II.append(float(columns[1]))
            volt_II_max = max(volt_II)
            if volt_II_max > 5e-3:
               digsignal.append([time_lab, 1])
            else:
               digsignal.append([time_lab, 0])
        elif (os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) and (os.path.exists(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))):
            volt_I, volt_II = [], []
            with open(os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_I.raw'))) as volt_file_I:
                for line in volt_file_I:
                    columns = line.split()  
                    volt_I.append(float(columns[1]))
            volt_I_max = max(volt_I)
            with open(os.path.join(os.path.join(output_path, f'PoiTimeSignal_{time_lab}_Voltage_II.raw'))) as volt_file_II:
                for line in volt_file_II:
                    columns = line.split()  
                    volt_II.append(float(columns[1]))
            volt_II_max = max(volt_II)
            if volt_I_max > 5e-3 or volt_II_max > 5e-3:
               digsignal.append([time_lab, 1])
            else:
               digsignal.append([time_lab, 0])
        
    graph = ROOT.TGraph()
    for q in range(len(digsignal)):
        graph.SetPoint(q, digsignal[q][0], digsignal[q][1])
 
    c3 = ROOT.TCanvas("canvas", "Scatter Plot", 800, 600)

    graph.SetMarkerStyle(20)  
    graph.SetMarkerSize(1.5)  
    graph.SetMarkerColor(ROOT.kBlack) 
    graph.Draw("AP")
    graph.GetXaxis().SetTitle("Time(ns)")
    graph.GetYaxis().SetTitle("Signal")

    c3.SaveAs("raser/cflm/output/dSides/PoiTimeSignal/DigSignal.pdf")

    '''
    time_interval = 600
    time_window = time_interval * sampleNumber
    total_number_time_window = 480*1e-6/(time_window*1e-9)  # 480us / xxx ns
    
    nsig_time_window = 0
   
    for filename in os.listdir(output_path):
        current = []
        if pattern.match(filename):
           with open(os.path.join(output_path, filename), 'r') as time_cuurrent_file:
               lines = time_cuurrent_file.readlines()
               for line in lines:
                   current.append(float(line.split(' ')[1].strip()))
           if  all( ele == 0 for ele in current ):
               pass
           else:
               nsig_time_window+=1

    N = total_number_time_window * nsig_time_window * 1.7
    prec = 1/math.sqrt(N)

    print('The precision in 1ms:', prec)
    '''