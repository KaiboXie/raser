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

def generate_random_par_in(original_data, num_particles=None):
    """生成随机粒子初始位置坐标"""
    new_data = copy.deepcopy(original_data)
    
    num_particles = 16
    
    new_par_in = []
    par_direction = []
    
    for _ in range(num_particles):
        x = round(random.uniform(-100, 100), 10)
        y = round(random.uniform(-100, 100), 10)
        z = -100.0
        new_par_in.append([x, y, z])
        par_direction.append([0, 0, 1])
    
    new_data['par_in'] = new_par_in
    new_data['par_num'] = num_particles
    new_data['par_direction'] = par_direction
    return new_data

def beam_create():
    beam_num = 500
    pulse_num = 2500

    data = {
        "geant4_model": "bmos",
        "object": {
            "binary_compounds": {
                "detector": {
                    "name": "detector",
                    "material_1": "Si",
                    "material_2": "C",
                    "compound_name": "SiC",
                    "density": 3.2,
                    "natoms_1": 50,
                    "natoms_2": 50,
                    "side_x": 5000,
                    "side_y": 5000,
                    "side_z": 100,
                    "colour": [0, 0.5, 0.8],
                    "position_x": 0,
                    "position_y": 0,
                    "position_z": 0
                }
            }
        },
        "g4_vis": "False",
        "world_type": "G4_Galactic",
        "world_size": 25000,
        "BeamOn": 1,
        "maxstep": 2,
        "par_num": 16,
        "par_type": "proton",
        "par_energy": 1600,
        "par_in": [[-1, 1, -100], [0, 1, -100], [1, 1, -100], [-1, 0, -100], [0, 0, -100], [1, 0, -100], [-1, -1, -100], [-1, -1, -100], [1, -1, -100], [2, 2, -100]],
        "par_direction": [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        "maxStep": 0.5,
        "DetModule": "NJU-PiN-bmos.json",
        "vis": 0,
        "CurrentName": "Current.root"
    }

    for beam in range(beam_num):
        output_path = os.path.join(output(__file__), 'beam_information', f'beam_{beam}')
        create_path(output_path)
        for pulse in range(pulse_num):
            new_data = generate_random_par_in(data)

            with open(os.path.join(output_path, f'pulse_{pulse}.json'), 'w') as f:
                json.dump(new_data, f, indent=2)