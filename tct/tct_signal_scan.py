#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Description: The main program of Raser induced current simulation      
@Date       : 2024/09/26 15:11:20
@Author     : zhulin
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

from gen_signal import build_device as bdv
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec import readout as rdo
from gen_signal import draw_save
from util.output import output

from .source import TCTTracks


def batch_loop(my_d, my_f, my_g4p, amplifier, g4_seed, total_events, instance_number):
    """
    Description:
        Batch run some events to get time resolution
    Parameters:
    ---------
    start_n : int
        Start number of the event
    end_n : int
        end number of the event 
    detection_efficiency: float
        The ration of hit particles/total_particles           
    @Returns:
    ---------
        None
    @Modify:
    ---------
        2021/09/07
    """
    start_n = instance_number * total_events
    end_n = (instance_number + 1) * total_events

    effective_number = 0
    for event in range(start_n,end_n):
        print("run events number:%s"%(event))
        if len(my_g4p.p_steps[event-start_n]) > 5:
            effective_number += 1
            my_current = ccrt.CalCurrentG4P(my_d, my_f, my_g4p, event-start_n)
            ele_current = rdo.Amplifier(my_current.sum_cu, amplifier)
            draw_save.save_signal_time_resolution(my_d,event,my_current.sum_cu,ele_current,my_g4p,start_n)
            del ele_current
    detection_efficiency =  effective_number/(end_n-start_n) 
    print("detection_efficiency=%s"%detection_efficiency)

def job_main(kwargs):
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
    my_l = TCTTracks(my_d, laser_dic)

    my_current = ccrt.CalCurrentLaser(my_d, my_f, my_l)
    my_current.save_current(my_d, my_l.model)
    if 'ngspice' not in amplifier:
        path = output(__file__, my_d.det_name, my_l.model)
        ele_current = rdo.Amplifier(my_current.sum_cu, amplifier)
        if kwargs['scan'] != None: #assume parameter alter
            # key = my_l.fz_rel
            key = kwargs['job']
            ele_current.save_signal_TTree(path, key)
        else:
            for i in range(my_current.read_ele_num):
                draw_current(my_d, my_current, ele_current.amplified_current, i, ele_current.amplified_current_name, path) # Draw current

            my_l.draw_nocarrier3D(path)
            my_l.draw_nocarrier2D(path)
    print('successfully')

def main(kwargs):
    scan_number = kwargs['scan']
    for i in range(scan_number):
        command = ' '.join(['python3', 'raser', '-b', 'tct signal',sys.argv[3],sys.argv[4], '--job', str(i)] + sys.argv[5:]) # 'raser', '-sh', 'gen_signal'
        # command = ' '.join(['python3', 'raser', 'tct signal',sys.argv[3],sys.argv[4], '--job', str(i)] + sys.argv[5:]) # 'raser', '-sh', 'gen_signal'
        print(command)
        subprocess.run([command], shell=True)
    