#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Description: The main program of Raser induced current simulation      
@Date       : 2024/02/20 18:12:26
@Author     : tanyuhang, Chenxi Fu
@version    : 2.0
'''
import sys
import os
import array
import time
import subprocess
import json
import random

import ROOT
ROOT.gROOT.SetBatch(True)
import geant4_pybind as g4b

from . import build_device as bdv
from particle import g4_time_resolution as g4t
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec import readout as rdo
from elec import ngspice_set_input as ngsip
from elec import ngspice as ng
from elec.set_pwl_input import set_pwl_input as pwlin
from .draw_save import energy_deposition, draw_drift_path, draw_current, cce
from util.output import output


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
        voltage = kwargs['voltage']
    else:
        voltage = my_d.voltage

    if kwargs['absorber'] != None:
        absorber = kwargs['absorber']
    else:
        absorber = my_d.absorber

    if kwargs['amplifier'] != None:
        amplifier = kwargs['amplifier']
    else:
        amplifier = my_d.amplifier

    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, my_d.read_out_contact, my_d.irradiation_flux)
    
    g4_seed = random.randint(0,1e7)
    my_g4p = g4t.Particles(my_d, absorber, g4_seed)
    my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4p, 0)

    if 'ngspice' in amplifier:
        save_current(my_d, my_current, key=None)
        '''
        input_p=ngsip.set_input(my_current, my_d, key=None)
        input_c=','.join(input_p)
        ng.ngspice_t0(input_c, input_p)
        subprocess.run(['ngspice -b -r t0.raw output/T0_tmp.cir'], shell=True)
        ng.plot_waveform()    
        '''
        ### For CEPC Fast Luminosity Measurement
        pwlin('output/PIN/NJU-PIN/pwl_current.txt', 'paras/circuit/ucsc.cir', 'output/elec/cflm/')
        subprocess.run(['ngspice -b -r cflm_single_ele.raw output/elec/cflm/ucsc_tmp.cir'], shell=True)
        ####
    else:
        ele_current = rdo.Amplifier(my_current.sum_cu, amplifier)
        now = time.strftime("%Y_%m%d_%H%M%S")
        path = output(__file__, my_d.det_name, now)

        #energy_deposition(my_g4p)   # Draw Geant4 depostion distribution
        draw_drift_path(my_d,my_f,my_current,path)

        for i in range(my_current.read_ele_num):
            draw_current(my_d, my_current, ele_current.amplified_current, i, ele_current.amplified_current_name, path) # Draw current
        if 'strip' in my_d.det_model:
            cce(my_current, path)
    
    del my_f
    end = time.time()
    print("total_time:%s"%(end-start))


# TODO: change this to a method of CalCurrent
def save_current(my_d,my_current,key):
    if key!=None:
        if "planar3D" in my_d.det_model or "planarRing" in my_d.det_model:
            path = os.path.join('output', 'pintct', my_d.det_name, )
        elif "lgad3D" in my_d.det_model:
            path = os.path.join('output', 'lgadtct', my_d.det_name, )
        if os.path.exists(path):
            os.mkdir(path)
        L = eval("my_l.{}".format(key))
        #L is defined by different keys
    elif key==None:
        if "planar3D" in my_d.det_model or "planarRing" in my_d.det_model:
            path = os.path.join('output', 'PIN', my_d.det_name, )
        elif "lgad3D" in my_d.det_model:
            path = os.path.join('output', 'LGAD', my_d.det_name, )
        if not os.path.exists(path):
            os.makedirs(path)

        #L is defined by different keys
    time = array.array('d', [999.])
    current = array.array('d', [999.])
    fout = ROOT.TFile(os.path.join(path, "sim-current")  + ".root", "RECREATE")
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

    ### For CEPC Fast Luminosity Measurement    
    file = ROOT.TFile(os.path.join(path, "sim-current") + ".root", "READ")
    tree = file.Get("tree")

    pwl_file = open(os.path.join(path,"pwl_current.txt"), "w")

    for i in range(tree.GetEntries()):
       tree.GetEntry(i)
       time_pwl = tree.time
       current_pwl = tree.current0
       pwl_file.write(str(time_pwl) + " " + str(current_pwl) + "\n")
    
    pwl_file.close()
    file.Close()
    ###

if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {}
    for arg in args:
        key, value = arg.split('=')
        kwargs[key] = value
    main(kwargs)
    