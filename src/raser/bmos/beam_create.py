#!/usr/bin/env python3 

'''
@Description:
    Create dummy beam information
@Date       : 2025
@Author     : Kaibo Xie
@version    : 2.0
'''

import json
import random
import copy
import os

from ..util.output import output, create_path

def generate_random_par_in(original_data, g4_dic):
    new_data = copy.deepcopy(original_data)

    detector = g4_dic["object"]["binary_compounds"]["detector"]
    detector_position_x = detector["position_x"]
    detector_position_y = detector["position_y"]
    detector_position_z = detector["position_z"]
    detector_side_x = detector["side_x"]
    detector_side_y = detector["side_y"]
    detector_side_z = detector["side_z"]

    BeamInformation = g4_dic["BeamInformation"]
    fluence = BeamInformation["fluence"]
    AreaSideRatioDetectorSide = BeamInformation["AreaSideRatioDetectorSide"]

    beam_side_x = detector_side_x*AreaSideRatioDetectorSide
    beam_side_y = detector_side_y*AreaSideRatioDetectorSide
    beam_side_x_lift = -beam_side_x/2 + detector_position_x
    beam_side_x_right = beam_side_x/2 + detector_position_x
    beam_side_y_lift = -beam_side_y/2 + detector_position_y
    beam_side_y_right = beam_side_y/2 + detector_position_y
    
    sum_particles = int(fluence*beam_side_x*beam_side_y/(10**8))
    
    num_particles = 0
    new_par_in = []
    par_direction = []
    for _ in range(sum_particles):
        x = round(random.uniform(beam_side_x_lift, beam_side_x_right), 10)
        y = round(random.uniform(beam_side_y_lift, beam_side_y_right), 10)
        z = -detector_side_z + detector_position_z
        if abs(x - detector_position_x) <= detector_side_x/2 and abs(y - detector_position_y) <= detector_side_x/2:
            num_particles += 1
            new_par_in.append([x, y, z])
            par_direction.append([0, 0, 1])
    
    if num_particles == 0:
        new_data['par_in'] = [[detector_position_x + detector_side_x, detector_position_y + detector_side_y, detector_position_y + detector_side_y]]
        new_data['par_num'] = 1
        new_data['par_direction'] = [[0, 0, 1]]
    else:
        new_data['par_in'] = new_par_in
        new_data['par_num'] = num_particles
        new_data['par_direction'] = par_direction
    
    return new_data

def beam_create():
    geant4_json = os.getenv("RASER_SETTING_PATH")+"/g4experiment/bmos.json"
    with open(geant4_json) as f:
        g4_dic = json.load(f)
    BeamInformation = g4_dic["BeamInformation"]
    beam_start = BeamInformation["BeamStartNum"]
    beam_num = BeamInformation["BeamNum"]
    pulse_num = BeamInformation["PulesPreBeam"]
    
    with open(os.getenv("RASER_SETTING_PATH")+"/g4experiment/bmos.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for beam in range(beam_start, beam_start + beam_num):
        output_path = os.path.join(output(__file__), 'beam_information', f'beam_{beam}')
        create_path(output_path)
        for pulse in range(pulse_num):
            new_data = generate_random_par_in(data, g4_dic)

            with open(os.path.join(output_path, f'pulse_{pulse}.json'), 'w') as f:
                json.dump(new_data, f, indent=2)
        print(f'beam{beam} created')