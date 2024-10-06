#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   devsim.py
@Time    :   2023/06/04
@Author  :   Henry Stone 
@Version :   1.0
'''
"""
@File    :   Field_to_G4.py
@Time    :   2024/09/30
@Author  :   Sen Zhao
@Version :   2.0
"""
import pickle
import ROOT
import numpy as np

from util.math import *

diff_res = 1e-5 # difference resolution in cm

class DevsimField:
    def __init__(self, device_name, dimension, voltage, contact,read_ele_num):
        self.name = device_name
        self.voltage = voltage # float
        self.dimension = dimension
        self.read_ele_num = int(read_ele_num) 

        

        DopingFile = "./output/field/{}/NetDoping_0V.pkl".format(self.name)
        PotentialFile = "./output/field/{}/Potential_{}V.pkl".format(self.name, self.voltage)
        TrappingRate_pFile = "./output/field/{}/TrappingRate_p_{}V.pkl".format(self.name, self.voltage)
        TrappingRate_nFile = "./output/field/{}/TrappingRate_n_{}V.pkl".format(self.name, self.voltage)
        Weighting_Potential = "./output/field/{}/weightingfield/{}/Potential_{}V.pkl".format(self.name,contact, 1)
        self.set_doping(DopingFile) #self.Doping
        self.set_potential(PotentialFile) #self.Potential, self.x_efield, self.y_efield, self.z_efield
        self.set_trap_p(TrappingRate_pFile) # self.TrappingRate_p
        self.set_trap_n(TrappingRate_nFile) # self.TrappingRate_n
        self.set_w_p(Weighting_Potential) #self.weighting_potential[]

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


    def set_w_p(self,Weighting_PotentialFile):
        try:
            with open(Weighting_PotentialFile,'rb') as file:
                Weighting_PotentialNotUniform=pickle.load(file)
                print("Weighting_Potential file loaded for {}".format(self.name))
                if Weighting_PotentialNotUniform['metadata']['dimension'] < self.dimension:
                    print("Weighting_Potential dimension not match")
                    return
        except FileNotFoundError:
            print("Weighting_Potential file not found, please run field simulation first")
            print("or manually set the Weighting_Potential file")
            return
        
        if Weighting_PotentialNotUniform['metadata']['dimension'] == 1:
            weighting_PotentialUniform = get_common_interpolate_1d(Weighting_PotentialNotUniform)
        elif Weighting_PotentialNotUniform['metadata']['dimension'] == 2:
            weighting_PotentialUniform = get_common_interpolate_2d(Weighting_PotentialNotUniform)
        elif Weighting_PotentialNotUniform['metadata']['dimension'] == 3:
            weighting_PotentialUniform = get_common_interpolate_3d(Weighting_PotentialNotUniform)

        self.weighting_Potential = weighting_PotentialUniform

    
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
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm  
        if self.dimension == 1:
            try:
                E_z = - ((self.Potential(z+diff_res/2) - self.Potential(z-diff_res/2))) / diff_res
            except ValueError:
                try:
                    E_z = - ((self.Potential(z+diff_res) - self.Potential(z))) / diff_res
                except ValueError:
                    try:
                        E_z = - ((self.Potential(z) - self.Potential(z-diff_res))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound z".format(z))
            return (0, 0, E_z)
        
        elif self.dimension == 2:
            try:
                E_z = - ((self.Potential(z+diff_res/2, x) - self.Potential(z-diff_res/2, x))) / diff_res
            except ValueError:
                try:
                    E_z = - ((self.Potential(z+diff_res, x) - self.Potential(z, x))) / diff_res
                except ValueError:
                    try:
                        E_z = - ((self.Potential(z, x) - self.Potential(z-diff_res, x))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound z".format(z))
            try:
                E_x = - ((self.Potential(z, x+diff_res/2) - self.Potential(z, x-diff_res/2))) / diff_res
            except ValueError:
                try:
                    E_x = - ((self.Potential(z, x+diff_res) - self.Potential(z, x))) / diff_res
                except ValueError:
                    try:
                        E_x = - ((self.Potential(z, x) - self.Potential(z, x-diff_res))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound x".format(x))
            try:
                E_y = - ((self.Potential(z, x+diff_res/2) - self.Potential(z, x-diff_res/2))) / diff_res
            except ValueError:
                try:
                    E_y = - ((self.Potential(z, x+diff_res) - self.Potential(z, x))) / diff_res
                except ValueError:
                    try:
                        E_y = - ((self.Potential(z, x) - self.Potential(z, x-diff_res))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound x".format(y))
            try:
                return (E_x, 0, E_z)
            except AttributeError:
                try:
                    return (E_x,E_y,0)
                except AttributeError:
                    return (0,E_y,E_z)
        
        elif self.dimension == 3:
            try:
                E_z = - ((self.Potential(z+diff_res/2, x, y) - self.Potential(z-diff_res/2, x, y))) / diff_res
            except ValueError:
                try:
                    E_z = - ((self.Potential(z+diff_res, x, y) - self.Potential(z, x, y))) / diff_res
                except ValueError:
                    try:
                        E_z = - ((self.Potential(z, x, y) - self.Potential(z-diff_res, x, y))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound z".format(z))
            try:
                E_x = - ((self.Potential(z, x+diff_res/2, y) - self.Potential(z, x-diff_res/2, y))) / diff_res
            except ValueError:
                try:
                    E_x = - ((self.Potential(z, x+diff_res, y) - self.Potential(z, x, y))) / diff_res
                except ValueError:
                    try:
                        E_x = - ((self.Potential(z, x, y) - self.Potential(z, x-diff_res, y))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound x".format(x))
            try:
                E_y = - ((self.Potential(z, x, y+diff_res/2) - self.Potential(z, x, y-diff_res/2))) / diff_res
            except ValueError:
                try:
                    E_y = - ((self.Potential(z, x, y+diff_res) - self.Potential(z, x, y))) / diff_res
                except ValueError:
                    try:
                        E_y = - ((self.Potential(z, x, y) - self.Potential(z, x, y-diff_res))) / diff_res
                    except ValueError:
                        raise ValueError("Point {} might be out of bound y".format(y))
            return (E_x, E_y, E_z)

    def get_w_p(self, x, y, z,i): # used in cal current
        x, y, z = x/1e4, y/1e4, z/1e4 # um to cm
        if self.dimension == 1:
            return self.weighting_Potential(z)
        elif self.dimension == 2:
            return self.weighting_Potential(z, x)
        elif self.dimension == 3:
            return self.weighting_Potential(z, x, y)

    
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
    testField = DevsimField("ITk-Si-strip", 2, -500.0, 4)
    print(testField.get_e_field(100,100,50))