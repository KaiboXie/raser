#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import os
import array
import time
import subprocess
import json
import time

import ROOT

from gen_signal import build_device as bdv
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec import readout as rdo
from elec import ngspice_set_input as ngsip
from elec import ngspice as ng
from .source import TCTTracks
from .save_TTree import save_signal_TTree
from util.output import output, create_path
from gen_signal.draw_save import draw_drift_path, draw_current

def main(kwargs):
    """
    Description:
        The main program of Raser induced current simulation      
    Parameters:
    ---------
    dset : class
        Parameters of simulation
    Function or class:
        Detector -- Define the basic parameters and mesh structure of the detector
        DevsimCal -- Get the electric field and weighting potential 
        Particles -- Electron and hole paris distibution
        CalCurrent -- Drift of e-h pais and induced current
        Amplifier -- Readout electronics simulation
    Modify:
    ---------
        2021/09/02
    """
    start = time.time()

    det_name = kwargs['det_name']
    my_d = bdv.Detector(det_name)
    
    if kwargs['voltage'] != None:
        voltage = float(kwargs['voltage'])
    else:
        voltage = float(my_d.voltage)

    if kwargs['laser'] != None:
        laser = kwargs['laser']
        laser_json = "./setting/laser/" + laser + ".json"
        with open(laser_json) as f:
            laser_dic = json.load(f)
    else:
        # TCT must be with laser
        raise NameError

    if kwargs['amplifier'] != None:
        amplifier = kwargs['amplifier']
    else:
        amplifier = my_d.amplifier

    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, my_d.read_out_contact)
    my_l = TCTTracks(my_d, laser_dic)

    if "strip" in det_name:
        pass
    else: 
        my_current = ccrt.CalCurrentLaser(my_d, my_f, my_l)

    if 'ngspice' in amplifier:
        save_current(my_d, my_current, key=None)
        input_p=ngsip.set_input(my_current, my_d, key=None)
        input_c=','.join(input_p)
        ng.ngspice_t0(input_c, input_p)
        subprocess.run(['ngspice -b -r t0.raw output/T0_tmp.cir'], shell=True)
        ng.plot_waveform()
    else:
        ele_current = rdo.Amplifier(my_current.sum_cu, amplifier)
    
    if kwargs['scan'] != None: #assume parameter alter
        key = my_l.fz_rel
        save_signal_TTree(my_d,key,ele_current,my_f)
        if "planar3D" in my_d.det_model or "planarRing" in my_d.det_model:
            path = "output/" + "pintct/" + my_d.det_name + "/"
        elif "lgad3D" in my_d.det_model:
            path = "output/" + "lgadtct/" + my_d.det_name + "/"
        else:
            raise NameError
    else:
        path = output(__file__, my_d.det_name, my_l.model)
        draw_drift_path(my_d,my_f,my_current,path)
        draw_current(my_d, my_current, ele_current.amplified_current, read_ele_num=my_current.read_ele_num, model=my_l.model, path=path)
        for i in range(my_current.read_ele_num):
            draw_current(my_d, my_current,ele_current.amplified_current,i,ele_current.amplified_current_name,path) # Draw current

        my_l.draw_nocarrier3D(path)
        my_l.draw_nocarrier2D(path)

    print("total time used:%s"%(time.time()-start))

#TODO: move this to calcurrent
def save_current(my_d,my_current,key):
    if "planar3D" in my_d.det_model or "planarRing" in my_d.det_model:
        path = os.path.join('output', 'pintct', my_d.det_name, )
    elif "lgad3D" in my_d.det_model:
        path = os.path.join('output', 'lgadtct', my_d.det_name, )
    create_path(path) 
    L = eval("my_l.{}".format(key))
    #L is defined by different keys
    time = array('d', [999.])
    current = array('d', [999.])
    fout = ROOT.TFile(os.path.join(path, "sim-TCT-current") + str(L) + ".root", "RECREATE")
    t_out = ROOT.TTree("tree", "signal")
    t_out.Branch("time", time, "time/D")
    for i in range(my_current.read_ele_num):
        t_out.Branch("current"+str(i), current, "current"+str(i)+"/D")
        for j in range(my_current.n_bin):
            current[0]=my_current.sum_cu[i].GetBinContent(j)
            time[0]=j*my_current.t_bin
            t_out.Fill()
        t_out.Write()
        fout.Close()

if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {}
    for arg in args:
        key, value = arg.split('=')
        kwargs[key] = value
    main(kwargs)