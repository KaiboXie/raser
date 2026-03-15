#!/usr/bin/env python3 

'''
@Description:
    Get the signal induced by dummy beam in BMOS detector
@Date       : 2025
@Author     : Kaibo Xie
@version    : 2.0
'''

import os
import array
import time
import subprocess
import json

import ROOT
ROOT.gROOT.SetBatch(True)
import numpy

from ..device import build_device as bdv
from ..field import devsim_field as devfield
from ..current import cal_current as ccrt
from ..afe.set_pwl_input import set_pwl_input as pwlin
from ..util.output import output, create_path
from . import bmos_g4

def get_signal(geant4_json = os.getenv("RASER_SETTING_PATH")+"/g4experiment/bmos.json", output_path = output(__file__), mode = "single"):

    with open(geant4_json) as f:
         g4_dic = json.load(f)

    detector_json = os.getenv("RASER_SETTING_PATH")+"/detector/"
    with open(os.path.join(detector_json , g4_dic['DetModule'])) as q:
         det_dic = json.load(q)

    start = time.time()

    det_name = det_dic['det_name']
    my_d = bdv.Detector(det_name)
    
    voltage = det_dic['bias']['voltage']
    
    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, my_d.read_out_contact, is_plugin=my_d.is_plugin(), irradiation_flux=my_d.irradiation_flux, bounds=my_d.bound)

    my_g4 = bmos_g4.bmosG4Interaction(my_d, geant4_json)

    tag = f"{g4_dic['par_type']}_{g4_dic['par_energy']}MeV_{g4_dic['par_num']}particle"
    dirname = f"{g4_dic['par_type']}_{g4_dic['par_energy']}MeV"
    CurrentName = g4_dic['CurrentName']
    pwl_name = f"pwl{g4_dic['CurrentName'].split('.')[0]}.txt"
    ngspice_output = f"UCSC_output.raw"

    tmp_path = os.path.join(output_path, "tmp")
    if mode == "single":
        output_path = os.path.join(output_path, dirname)
    elif mode != "beam":
        print("wrong mode!!!!")
        os._exit()
    create_path(tmp_path)
    create_path(output_path)

    amplitudes = []
    for i in range(len(my_g4.p_steps_current)):
        my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4, i)

        save_current(my_current, tmp_path, CurrentName, pwl_name, 1)

        pwlin(os.path.join(tmp_path, pwl_name), 'src/raser/bmos/ucsc.cir', os.path.join(output_path, ngspice_output), tmp_path)
        subprocess.run([f"ngspice -b -r ./xxx.raw {os.path.join(tmp_path, 'ucsc_tmp.cir')}"], shell=True)
        time_v, volt = read_file_voltage(output_path, ngspice_output)
        amplitudes.append(max(abs(volt)))

    save_amplitudes(output_path, amplitudes, tag, dirname)

    end = time.time()
    print("total_time:%s"%(end - start))

    del my_current
    del my_g4
    del my_f
    del my_d

    return max(volt)

def save_current(my_current, output_path, root_name, pwl_name, read_ele_num):
    time = array.array('d', [999.])
    current = array.array('d', [999.])

    fout = ROOT.TFile(os.path.join(output_path, root_name), "RECREATE")
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
   
    file = ROOT.TFile(os.path.join(output_path, root_name), "READ")
    tree = file.Get("tree")

    pwl_file = open(os.path.join(output_path, pwl_name), "w")

    for i in range(tree.GetEntries()):       
        tree.GetEntry(i)
        time_pwl = tree.time
        current_pwl = tree.current0
        pwl_file.write(str(time_pwl) + " " + str(current_pwl) + "\n")
    
    pwl_file.close()
    file.Close()

def read_file_voltage(file_path, file_name):
    with open(os.path.join(file_path, file_name)) as f:
        lines = f.readlines()
        time_v,volt = [],[]

        for line in lines:
            time_v.append(float(line.split()[0])*1e9)
            volt.append(float(line.split()[1])*1e3)

    time_v = numpy.array(time_v ,dtype='float64')
    volt = numpy.array(volt,dtype='float64')

    return time_v, volt

def save_amplitudes(output_path, signal, tag, dirname):
    ROOT.gROOT.SetBatch(True)
    file = ROOT.TFile(os.path.join(output_path, f"amplitudes_{tag}.root"), "RECREATE")
    amplitudes = ROOT.TTree("tree", "amplitudes")
    amp =array.array('d', [0.0])
    amplitudes.Branch("amplitudes", dirname, "amplitudes/D")

    for sig in signal:
        amp[0] = sig
        amplitudes.Fill()

    amplitudes.Write()
    file.Close()