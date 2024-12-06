import os
import re
import ROOT
import json
import multiprocessing
import subprocess
from . import cflm
from . import get_signal
from . import time_signal
from gen_signal import build_device as bdv
from elec.set_pwl_input import set_pwl_input as pwlin
import random
import array
import math

def main():

    random.seed(3020122)
    
    rand = ROOT.TRandom3()
    average_hit = 1.7
    total_samples = 100000
    hitnumber = []

    for i in range(total_samples):
        hitnumber.append(rand.Poisson(average_hit))
    
    hist = ROOT.TH1F("hist", "One-Dimensional Histogram", 10000, -5, 15)

    for num in hitnumber:
        hist.Fill(num)

    canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)
    hist.Draw()

    canvas.SaveAs("raser/cflm/output/PossionHitData.pdf")

    with open('./setting/absorber/cflm.json', 'r') as p:
         g4_dic = json.load(p)
    
    detector_json = "./setting/detector/"
    with open(os.path.join(detector_json , g4_dic['DetModule'])) as q:
         det_dic = json.load(q)
    
    det_name = det_dic['det_name']
    my_d = bdv.Detector(det_name)

    file = ROOT.TFile("raser/cflm/output/DataFile.root", "READ")
    tree = file.Get("electrons")

    pos, mom, energy = [], [], []
    pos_sel, mom_sel, energy_sel = [], [], []
    TotalHitInfo = []

    manager = multiprocessing.Manager()
    pos_sel = manager.list()
    mom_sel = manager.list()
    energy_sel = manager.list()   
    
    def worker_function_I(queue, lock, j):
       try:
           print(f"运行 loop_solver:{j}")
           result_message = "Execution completed successfully"
           my_g4p = cflm.cflmG4Particles(my_d)
           hitFlag = my_g4p.HitFlag
           if hitFlag:
              pos_sel.append(pos[j])
              mom_sel.append(mom[j])
              energy_sel.append(energy[j])
           else:
                pass
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
    
    for j in range(tree.GetEntries()):     
        with open('./setting/absorber/cflm.json', 'r') as file:
                g4_dic = json.load(file)    
                g4_dic['par_in']      = [pos[j]]
                g4_dic['par_direct']  = [mom[j]]
                g4_dic['par_energy']  = [energy[j]]
                g4_dic['CurrentName'] = f"PossionTimeSignal_{j}_tmp.root"     
                updated_g4_dic = json.dumps(g4_dic, indent=4)
        
        with open('./setting/absorber/cflm.json', 'w') as file:
                
                file.write(updated_g4_dic)
        p = multiprocessing.Process(target=worker_function_I, args=(queue, lock, j))

        p.start()
        p.join()
        while not queue.empty():
            output_info = queue.get() 
            print("队列输出:", output_info)  # 确认输出内容
            if output_info is None:
                print("警告: worker_function_I 返回了 None,可能发生了错误!")

    for k in range(len(pos_sel)):
        TotalHitInfo.append([pos_sel[k], mom_sel[k], energy_sel[k]])
    
    random.shuffle(TotalHitInfo)
    
    sampleNumber = 10
    
    randomhit = random.sample(hitnumber, sampleNumber)
    
    nCount = 0
    with open('raser/cflm/output/PossionHit.txt', 'w') as PossionHitFile:
         for i in range(len(randomhit)):
             if randomhit[i] == 0:
                  PossionHitFile.write(f'{randomhit[i]} {999} {nCount*10}\n')
             else:
                  randomHitInfo = random.sample(TotalHitInfo, randomhit[i])
                  PossionHitFile.write(f'{randomhit[i]} {randomHitInfo} {nCount*10}\n')
             nCount+=1
       
    def worker_function_II(queue, lock, j):
        try:
            print(f"运行 loop_solver:{j}")
            result_message = "Execution completed successfully"
            #get_signal.main()
            cflm.main()
        except Exception as e:
            result_message = f"Error: {e}"
        with lock:
            queue.put(result_message)
  
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    
    HitTimeList = []
    with open('raser/cflm/output/PossionHit.txt', 'r') as Hit_input_file:
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
                   with open('./setting/absorber/cflm.json', 'r') as file:
                            g4_dic = json.load(file)    
                            g4_dic['NumofGun']    = int(hitEvents)
                            g4_dic['par_in']      = pos
                            g4_dic['par_direct']  = mom
                            g4_dic['par_energy']  = energy
                            g4_dic['CurrentName'] = f"PossionTimeSignal_{hitTime}_tmp.root"
                            g4_dic['PosBaseName'] = f"SecondaryParticle_{hitTime}.txt"     
                            updated_g4_dic = json.dumps(g4_dic, indent=4)
                
                   with open('./setting/absorber/cflm.json', 'w') as file:
                        file.write(updated_g4_dic)
    
                   p = multiprocessing.Process(target=worker_function_II, args=(queue, lock, line))
                   p.start()
                   p.join()
                    
                   while not queue.empty():
                        output_info = queue.get() 
                        print("队列输出:", output_info)  # 确认输出内容
                        if output_info is None:
                           print("警告: worker_function 返回了 None,可能发生了错误!")
    
    for count in HitTimeList:
        current_path = f'raser/cflm/output/PossionTimeSignal_{count}_tmp_pwl_current.txt'
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
    
    output_path = "raser/cflm/output"
    pattern = re.compile(r"PossionTimeSignal_(\d+)_tmp_pwl_current.txt")
    
    HitNo, time_tmp, current = [], [], []
    
    for filename in os.listdir(output_path):
        if pattern.match(filename):
           j = int(pattern.match(filename).group(1))
           HitNo.append(j)

    HitNo.sort()

    for i in HitNo:

        file_str = f'raser/cflm/output/PossionTimeSignal_{i}_tmp_pwl_current.txt'

        with open(file_str, 'r') as current_file:
             for line in current_file:
                 columns = line.strip().split(' ')       
                 time_tmp.append(columns[0])
                 current.append(columns[1])

    total_current_path = "raser/cflm/output/PossionTimeSignalTotalCurrent.txt"
    with open(total_current_path, 'w') as output_file:
         for t, c in zip(time_tmp, current):
             output_file.write(f"{t} {c}\n")

    with open('raser/cflm/output/PossionTimeSignalTotalCurrent.txt', 'r') as file:
         lines = file.readlines()
         sorted_lines = sorted(lines, key=lambda x: float(x.split()[0]))

    with open('raser/cflm/output/PossionTimeSignalTotalCurrentSorted.txt', 'w') as file:
        for line in sorted_lines:
            file.write(line)
    
    pwlin(f"raser/cflm/output/PossionTimeSignalTotalCurrentSorted.txt", 'raser/cflm/ucsc.cir', 'raser/cflm/output/')
    subprocess.run([f"ngspice -b -r ./xxx.raw raser/cflm/output/ucsc_tmp.cir"], shell=True)

    time_signal.TimeSignalPlot(
                                 'raser/cflm/output/PossionTimeSignalTotalCurrentSorted.txt',
                                 'raser/cflm/output/Current_test.raw',
                                 'raser/cflm/output/PossionTimeSignalCurrent.pdf',
                                 'raser/cflm/output/PossionTimeSignalVoltage.pdf',
                                 1e9,
                                 100,
                                 2000,
                                 1600
                              )
    
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
               