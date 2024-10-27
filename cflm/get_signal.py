#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import os
import array
import time
import subprocess
import ROOT

from gen_signal import build_device as bdv
from . import cflm
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec.set_pwl_input import set_pwl_input as pwlin

from util.output import output

import json

import re
import numpy

def get_signal():

    geant4_json = "./setting/absorber/cflm.json"
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

    my_g4p = cflm.cflmG4Particles(my_d)
    print(f'***************************************************** {my_g4p.HitFlag} ************************************************')
    if my_g4p.HitFlag == 0:
       print("No secondary particlees hit the detector")
    else:
        my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4p, 0)

        if 'ngspice' in amplifier:
            save_current(my_d, my_current, g4_dic, my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, det_dic['read_out_contact'], 0))

            pwlin(f"raser/cflm/output/{g4_dic['CurrentName'].split('.')[0]}_pwl_current.txt", 'raser/cflm/ucsc.cir', 'raser/cflm/output/')
            subprocess.run([f"ngspice -b -r ./xxx.raw raser/cflm/output/ucsc_tmp.cir"], shell=True)
        
    del my_f
    end = time.time()
    print("total_time:%s"%(end-start))
    
def save_current(my_d, my_current, g4_dic, read_ele_num):

    time = array.array('d', [999.])
    current = array.array('d', [999.])
    fout = ROOT.TFile(os.path.join("raser/cflm/output/", g4_dic['CurrentName'].split('.')[0])  + ".root", "RECREATE")
    t_out = ROOT.TTree("tree", "signal")
    t_out.Branch("time", time, "time/D")
    for i in range(read_ele_num):
        t_out.Branch("current"+str(i), current, "current"+str(i)+"/D")
        for j in range(my_current.n_bin):
            current[0]=my_current.sum_cu[i].GetBinContent(j)
            time[0]=j*my_current.t_bin
            t_out.Fill()
    t_out.Write()
    fout.Close()
   
    file = ROOT.TFile(os.path.join("raser/cflm/output/", g4_dic['CurrentName'].split('.')[0])  + ".root", "READ")
    tree = file.Get("tree")

    pwl_file = open(os.path.join("raser/cflm/output/", f"{g4_dic['CurrentName'].split('.')[0]}_pwl_current.txt"), "w")

    for i in range(tree.GetEntries()):
       tree.GetEntry(i)
       time_pwl = tree.time
       current_pwl = tree.current0
       pwl_file.write(str(time_pwl) + " " + str(current_pwl) + "\n")
    
    pwl_file.close()
    file.Close()