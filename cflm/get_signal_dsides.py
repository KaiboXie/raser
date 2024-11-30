#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import os
import array
import time
import multiprocessing
import ROOT
import json
import subprocess

from gen_signal import build_device as bdv
from . import cflm_dsides
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec.set_pwl_input import set_pwl_input as pwlin
from . import time_signal

from util.output import output

import json
def main():
    
    geant4_json = "./setting/absorber/cflm_dsides.json"
    with open(geant4_json) as f:
         g4_dic = json.load(f)

    detector_json = "./setting/detector/"
    with open(os.path.join(detector_json , g4_dic['DetModule'])) as q:
         det_dic = json.load(q)

    start = time.time()

    det_name = det_dic['det_name']
    my_d = bdv.Detector(det_name)
    voltage = det_dic['bias']['voltage']
    amplifier = det_dic['amplifier']

    print(my_d.device)
    print(voltage)
    
    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, det_dic['read_out_contact'], 0)

    def worker_function(queue, lock, i):
       try:
           print(f"运行 loop_solver:{i}")
           result_message = "Execution completed successfully"
           my_g4p = cflm_dsides.cflmdSidesG4Particles(my_d, i)
           if i == 'I':
              hit_flag = my_g4p.HitFlagI
              if hit_flag == 0:
                 print(f"No secondary particles hit the detector{i}")
              else: 
                 my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4p, 0)
           if i == 'II':
              hit_flag = my_g4p.HitFlagII
              if hit_flag == 0:
                  print(f"No secondary particles hit the detector{i}")
              else: 
                  my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4p, 0)

           if 'ngspice' in amplifier:
               save_current(my_current, g4_dic, det_dic['read_out_contact'], i)
               pwlin(f"raser/cflm/output/dSides/{g4_dic['CurrentName'].split('.')[0]}Current_{i}.txt", 'raser/cflm/ucsc.cir', f'raser/cflm/output/dSides/dSidesVoltage_{i}.raw', 'raser/cflm/output/dSides/')
               subprocess.run([f"ngspice -b -r ./xxx.raw raser/cflm/output/dSides/ucsc_tmp.cir"], shell=True)
        
       except Exception as e:
           result_message = f"Error: {e}"
       with lock:
           queue.put(result_message)
  
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    
    for i in ('I', 'II'):
        
        p = multiprocessing.Process(target=worker_function, args=(queue, lock, i))
        p.start()
        p.join()
        while not queue.empty():
            output_info = queue.get() 
            print("队列输出:", output_info)  # 确认输出内容
            if output_info is None:
                print("警告: worker_function 返回了 None,可能发生了错误!")
        
        time_signal.TimeSignalPlot(
                                    f'raser/cflm/output/dSides/PossionTimeSignal_dSidesCurrent_{i}.txt',
                                    f'raser/cflm/output/dSides/dSidesVoltage_{i}.raw',
                                    f'raser/cflm/output/dSides/PossionTimeSignal_dSidesCurrent_{i}.pdf',
                                    f'raser/cflm/output/dSides/dSidesVoltage_{i}.pdf',
                                    1e9,
                                    10,
                                    800,
                                    600
                                  )

def save_current(my_current, g4_dic, read_ele_num, k):

    time = array.array('d', [999.])
    current = array.array('d', [999.])
    fout = ROOT.TFile(os.path.join("raser/cflm/output/dSides/", g4_dic['CurrentName'].split('.')[0])  + ".root", "RECREATE")
    t_out = ROOT.TTree("tree", "signal")
    t_out.Branch("time", time, "time/D")
    for i in range(len(read_ele_num)):
        t_out.Branch("current"+str(i), current, "current"+str(i)+"/D")
        for j in range(my_current.n_bin):
            current[0]=my_current.sum_cu[i].GetBinContent(j)
            time[0]=j*my_current.t_bin
            t_out.Fill()
    t_out.Write()
    fout.Close()
   
    file = ROOT.TFile(os.path.join("raser/cflm/output/dSides", g4_dic['CurrentName'].split('.')[0])  + ".root", "READ")
    tree = file.Get("tree")

    pwl_file = open(os.path.join("raser/cflm/output/dSides", f"{g4_dic['CurrentName'].split('.')[0]}Current_{k}.txt"), "w")

    for i in range(tree.GetEntries()):
       tree.GetEntry(i)
       time_pwl = tree.time
       current_pwl = tree.current0
       pwl_file.write(str(time_pwl) + " " + str(current_pwl) + "\n")
    
    pwl_file.close()
    file.Close()
    