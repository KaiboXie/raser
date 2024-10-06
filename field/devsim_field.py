#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   devsim.py
@Time    :   2023/06/04
@Author  :   Henry Stone, Sen Zhao
@Version :   2.0
'''

import pickle
import ROOT
import numpy as np

from util.math import *

diff_res = 1e-5 # difference resolution in cm

class DevsimField:
    def __init__(self, device_name, dimension, voltage, read_out_contacts):
        self.name = device_name
        self.voltage = voltage
        self.dimension = dimension
        self.read_ele_num = int(len(read_out_contacts)) 

        DopingFile = "./output/field/{}/NetDoping_0V.pkl".format(self.name)
        PotentialFile = "./output/field/{}/Potential_{}V.pkl".format(self.name, self.voltage)
        TrappingRate_pFile = "./output/field/{}/TrappingRate_p_{}V.pkl".format(self.name, self.voltage)
        TrappingRate_nFile = "./output/field/{}/TrappingRate_n_{}V.pkl".format(self.name, self.voltage)
        WeightingPotentialFiles = []
        for contact in read_out_contacts:
            WeightingPotentialFiles.append("./output/field/{}/weightingfield/{}/Potential_{}V.pkl".format(self.name,contact, 1))
        self.set_doping(DopingFile) #self.Doping
        self.set_potential(PotentialFile) #self.Potential, self.x_efield, self.y_efield, self.z_efield
        self.set_trap_p(TrappingRate_pFile) # self.TrappingRate_p
        self.set_trap_n(TrappingRate_nFile) # self.TrappingRate_n
        self.set_w_p(WeightingPotentialFiles) #self.weighting_potential[]

    def set_doping(self, DopingFile):
        try:
            with open(DopingFile,'rb') as file:
                DopingNotUniform=pickle.load(file)
                print("Doping file loaded for {}".format(self.name))
                if DopingNotUniform['metadata']['dimension'] < self.dimension:
                    print("Doping dimension not match")
                    return
        except FileNotFoundError:
            print("Doping file not found, please run field simulation first")
            print("or manually set the doping file")
            return
        
        if DopingNotUniform['metadata']['dimension'] == 1:
            DopingUniform = get_common_interpolate_1d(DopingNotUniform)
        elif DopingNotUniform['metadata']['dimension'] == 2:
            DopingUniform = get_common_interpolate_2d(DopingNotUniform)
        elif DopingNotUniform['metadata']['dimension'] == 3:
            DopingUniform = get_common_interpolate_3d(DopingNotUniform)

        self.Doping = DopingUniform

    def set_potential(self, PotentialFile):
        try:
            with open(PotentialFile,'rb') as file:
                PotentialNotUniform=pickle.load(file)
                print("Potential file loaded for {}".format(self.name))
                if PotentialNotUniform['metadata']['dimension'] < self.dimension:
                    print("Potential dimension not match")
                    return
        except FileNotFoundError:
            print("Potential file not found, please run field simulation first")
            print("or manually set the potential file")
            return
        
        if PotentialNotUniform['metadata']['dimension'] == 1:
            PotentialUniform = get_common_interpolate_1d(PotentialNotUniform)
        elif PotentialNotUniform['metadata']['dimension'] == 2:
            PotentialUniform = get_common_interpolate_2d(PotentialNotUniform)
        elif PotentialNotUniform['metadata']['dimension'] == 3:
            PotentialUniform = get_common_interpolate_3d(PotentialNotUniform)

        self.Potential = PotentialUniform


    def set_w_p(self,WeightingPotentialFiles):
        self.WeightingPotential = []
        for i in range(self.read_ele_num):
            WeightingPotentialFile = WeightingPotentialFiles[i]
            try:
                with open(WeightingPotentialFile,'rb') as file:
                    WeightingPotentialNotUniform=pickle.load(file)
                    print("Weighting_Potential file loaded for {}".format(self.name))
                    if WeightingPotentialNotUniform['metadata']['dimension'] < self.dimension:
                        print("Weighting_Potential dimension not match")
                        return
            except FileNotFoundError:
                print("Weighting_Potential file not found, please run field simulation first")
                print("or manually set the Weighting_Potential file")
                return
            
            if WeightingPotentialNotUniform['metadata']['dimension'] == 1:
                WeightingPotentialUniform = get_common_interpolate_1d(WeightingPotentialNotUniform)
            elif WeightingPotentialNotUniform['metadata']['dimension'] == 2:
                WeightingPotentialUniform = get_common_interpolate_2d(WeightingPotentialNotUniform)
            elif WeightingPotentialNotUniform['metadata']['dimension'] == 3:
                WeightingPotentialUniform = get_common_interpolate_3d(WeightingPotentialNotUniform)

            self.WeightingPotential.append(WeightingPotentialUniform)
    
    def set_trap_p(self, TrappingRate_pFile):
        try:
            with open(TrappingRate_pFile,'rb') as file:
                TrappingRate_pNotUniform=pickle.load(file)
                print("TrappingRate_p file loaded for {}".format(self.name))
                if TrappingRate_pNotUniform['metadata']['dimension'] < self.dimension:
                    print("TrappingRate_p dimension not match")
                    return
        except FileNotFoundError:
            print("TrappingRate_p file not found, please run field simulation first")
            print("or manually set the hole trapping rate file")
            return
        
        if TrappingRate_pNotUniform['metadata']['dimension'] == 1:
            TrappingRate_pUniform = get_common_interpolate_1d(TrappingRate_pNotUniform)
        elif TrappingRate_pNotUniform['metadata']['dimension'] == 2:
            TrappingRate_pUniform = get_common_interpolate_2d(TrappingRate_pNotUniform)
        elif TrappingRate_pNotUniform['metadata']['dimension'] == 3:
            TrappingRate_pUniform = get_common_interpolate_3d(TrappingRate_pNotUniform)

        self.TrappingRate_p = TrappingRate_pUniform
    
    def set_trap_n(self, TrappingRate_nFile):
        try:
            with open(TrappingRate_nFile,'rb') as file:
                TrappingRate_nNotUniform=pickle.load(file)
                print("TrappingRate_n file loaded for {}".format(self.name))
                if TrappingRate_nNotUniform['metadata']['dimension'] != self.dimension:
                    print("TrappingRate_n dimension not match")
                    return
        except FileNotFoundError:
            print("TrappingRate_n file not found, please run field simulation first")
            print("or manually set the electron trapping rate file")
            return
        
        if TrappingRate_nNotUniform['metadata']['dimension'] == 1:
            TrappingRate_nUniform = get_common_interpolate_1d(TrappingRate_nNotUniform)
        elif TrappingRate_nNotUniform['metadata']['dimension'] == 2:
            TrappingRate_nUniform = get_common_interpolate_2d(TrappingRate_nNotUniform)
        elif TrappingRate_nNotUniform['metadata']['dimension'] == 3:
            TrappingRate_nUniform = get_common_interpolate_3d(TrappingRate_nNotUniform)

        self.TrappingRate_n = TrappingRate_nUniform
        

    # DEVSIM dimension order: x, y, z
    # RASER dimension order: z, x, y

    def get_doping(self, x, y, z):
        '''
            input: position in um
            output: doping in cm^-3
        '''
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.Doping(z)
        elif self.dimension == 2:
            return self.Doping(z, x)
        elif self.dimension == 3:
            return self.Doping(z, x, y)
    
    def get_potential(self, x, y, z):
        '''
            input: position in um
            output: potential in V
        '''
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.Potential(z)
        elif self.dimension == 2:
            return self.Potential(z, x)
        elif self.dimension == 3:
            return self.Potential(z, x, y)
    
    def get_e_field(self, x, y, z):
        '''
            input: position in um
            output: intensity in V/um
        ''' 
        x, y, z = x / 1e4, y / 1e4, z / 1e4  # um to cm
        diff_resolutions = [(diff_res / 2, diff_res / 2), (diff_res, 0), (0, diff_res)]

        def calculate_e(component, *args):
            for diff1, diff2 in diff_resolutions:
                try:
                    return -((self.Potential(*(a + diff1 for a in args)) -
                            self.Potential(*(a - diff2 for a in args))) / diff_res)
                except ValueError:
                    continue
            raise ValueError(f"Point {args} might be out of bound {component}")

        if self.dimension == 1:
            E_z = calculate_e('z', z)
            return (0, 0, E_z)

        elif self.dimension == 2:
            E_z = calculate_e('z', z, x)
            E_x = calculate_e('x', z, x)
            return (E_x, 0, E_z)

        elif self.dimension == 3:
            E_z = calculate_e('z', z, x, y)
            E_x = calculate_e('x', z, x, y)
            E_y = calculate_e('y', z, x, y)
            return (E_x, E_y, E_z)

    def get_w_p(self, x, y, z, i): # used in cal current
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.WeightingPotential[i](z)
        elif self.dimension == 2:
            return self.WeightingPotential[i](z, x)
        elif self.dimension == 3:
            return self.WeightingPotential[i](z, x, y)

    
    def get_trap_e(self, x, y, z):
        '''
            input: position in um
            output: electron trapping rate in s^-1     
        '''
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.TrappingRate_n(z)
        
        elif self.dimension == 2:
            return self.TrappingRate_n(z, x)
        
        elif self.dimension == 3:
            return self.TrappingRate_n(z, x, y)
    
    def get_trap_h(self, x, y, z):
        '''
            input: position in um
            output: hole trapping rate in s^-1     
        '''
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.TrappingRate_p(z)
        elif self.dimension == 2:
            return self.TrappingRate_p(z, x)
        elif self.dimension == 3:
            return self.TrappingRate_p(z, x, y)


if __name__ == "__main__":
    pass