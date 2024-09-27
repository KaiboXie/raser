#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Description: The main program of Raser induced current simulation      
@Date       : 2024/09/26 15:11:20
@Author     : tanyuhang, Chenxi Fu
@version    : 2.0
'''
import sys
import os
import array
import time
import subprocess
import ROOT

from field import build_device as bdv
from particle import g4simulation as g4s
from field import devsim_field as devfield
from current import cal_current as ccrt
from elec import readout as rdo
from elec import ngspice_set_input as ngsip
from elec import ngspice as ng

from . import draw_save
from util.output import output

import json

import random

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
        voltage = float(kwargs['voltage'])
    else:
        voltage = float(my_d.voltage)

    if kwargs['absorber'] != None:
        absorber = kwargs['absorber']
    else:
        absorber = my_d.absorber

    if kwargs['amplifier'] != None:
        amplifier = kwargs['amplifier']
    else:
        amplifier = my_d.amplifier

    my_f = devfield.DevsimField(my_d.device, my_d.dimension, voltage, my_d.read_ele_num, my_d.l_z)

    path = output(__file__, my_d.det_name, 'batch')
    if "plugin" in my_d.det_model:
        draw_save.draw_ele_field(my_d,my_f,"xy",my_d.det_model,my_d.l_z*0.5,path)
    else:
        draw_save.draw_ele_field_1D(my_d,my_f,path)
        draw_save.draw_ele_field(my_d,my_f,"xz",my_d.det_model,my_d.l_y*0.5,path)

    geant4_json = "./setting/absorber/" + absorber + ".json"
    with open(geant4_json) as f:
        g4_dic = json.load(f)
    total_events = int(g4_dic['total_events'])

    job_number = kwargs['job']
    instance_number = job_number

    g4_seed = instance_number * total_events
    my_g4p = g4s.Particles(my_d, absorber, g4_seed)
    batch_loop(my_d, my_f, my_g4p, amplifier, g4_seed, total_events, instance_number)
    del my_g4p

def main(kwargs):
    scan_number = kwargs['scan']
    for i in range(scan_number):
        command = ' '.join(['python3', 'raser', '-b', 'gen_signal', '--job', str(i)] + sys.argv[3:]) # 'raser', '-sh', 'gen_signal'
        print(command)
        subprocess.run([command], shell=True)