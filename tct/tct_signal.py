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
ROOT.gROOT.SetBatch(True)

from gen_signal import build_device as bdv
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec import readout as rdo
from .laser import LaserInjection
from util.output import output, create_path
from gen_signal.draw_save import draw_current

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

    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, my_d.read_out_contact, my_d.irradiation_flux)
    my_l = LaserInjection(my_d, laser_dic)

    my_current = ccrt.CalCurrentLaser(my_d, my_f, my_l)
    path = output(__file__, my_d.det_name, my_l.model)
    my_current.save_current(path, my_l.model)

    ele_json = "./setting/electronics/" + amplifier + ".json"
    ele_cir = "./setting/electronics/" + amplifier + ".cir"
    if os.path.exists(ele_json):
        # use convolution
        ele_current = rdo.Amplifier(my_current.sum_cu, amplifier)
        if kwargs['scan'] != None: #assume parameter alter
            key = my_l.fz_rel
            ele_current.save_signal_TTree(path, key)
        else:
            for i in range(my_current.read_ele_num):
                draw_current(my_d, my_current, ele_current.amplified_current, i, ele_current.name, path) # Draw current

            my_l.draw_nocarrier3D(path)
            my_l.draw_nocarrier2D(path)
    elif os.path.exists(ele_cir):
        # use ngspice
        from elec import ngspice_set_input
        from elec import ngspice_set_tmp_cir
        from elec import ngspice_get_fig
        input_p = ngspice_set_input.set_input(path, my_l.model)
        input_c=','.join(input_p)
        ngspice_set_tmp_cir.ngspice_set_tmp_cir(input_c, path, amplifier, my_l.model)
        subprocess.run(['ngspice -b {}/{}{}_tmp.cir'.format(path, amplifier, my_l.model)], shell=True)
        ngspice_get_fig.main(amplifier, path, my_l.model)
    else:
        raise NameError(amplifier)
    
    print("total time used:%s"%(time.time()-start))

if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = {}
    for arg in args:
        key, value = arg.split('=')
        kwargs[key] = value
    main(kwargs)