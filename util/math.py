#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Description: 
    Math Objects
@Date       : 2024/09/19 20:57:33
@Author     : Chenxi Fu
@version    : 1.0
'''

import math

import numpy as np
from scipy.interpolate import interp1d as p1d
from scipy.interpolate import interp2d as p2d
from scipy.interpolate import griddata
from scipy.interpolate import LinearNDInterpolator as LNDI
import ROOT

x_bin = 1000
y_bin = 1000
z_bin = 1000

class Vector:
    def __init__(self,a1,a2,a3):
        self.components = [a1,a2,a3]
        
    def cross(self,Vector_b):
        """ Get vector cross product of self and another Vector"""
        o1 = self.components[1]*Vector_b.components[2]-self.components[2]*Vector_b.components[1]
        o2 = self.components[2]*Vector_b.components[0]-self.components[0]*Vector_b.components[2]
        o3 = self.components[0]*Vector_b.components[1]-self.components[1]*Vector_b.components[0]
        return Vector(o1,o2,o3)

    def get_length(self):
        " Return length of self"
        return math.sqrt(self.components[0]*self.components[0]+self.components[1]*self.components[1]+self.components[2]*self.components[2])

    def add(self,Vector_b):
        " Return the sum of two Vectors. eg: [1,2,3]+[1,2,3] = [2,4,6]"
        o1 = self.components[0]+Vector_b.components[0]
        o2 = self.components[1]+Vector_b.components[1]
        o3 = self.components[2]+Vector_b.components[2]
        return Vector(o1,o2,o3)

    def sub(self,Vector_b):
        " Return the subtraction of two Vectors. eg: [1,2,3]-[1,2,3] = [0,0,0]"
        o1 = self.components[0]-Vector_b.components[0]
        o2 = self.components[1]-Vector_b.components[1]
        o3 = self.components[2]-Vector_b.components[2]
        return Vector(o1,o2,o3)
    
    def mul(self,k):
        " Return Vector multiplied by number. eg: 2 * [1,2,3] = [2,4,6]"
        return Vector(self.components[0]*k,self.components[1]*k,self.components[2]*k)


def get_common_interpolate_1d(data):
    values = data['values']
    points = data['points']
    f = p1d(points, values)
    return f

def get_common_interpolate_2d(data):
    values = data['values']
    points_x = []
    points_y = []
    for point in data['points']:
        points_x.append(point[0])
        points_y.append(point[1])
    new_x = np.linspace(min(points_x), max(points_x), x_bin)
    new_y = np.linspace(min(points_y), max(points_y), y_bin)
    new_points = np.array(np.meshgrid(new_x, new_y)).T.reshape(-1, 2)
    new_values = griddata((points_x, points_y), values, new_points, method='linear')
    f = p2d(new_x, new_y, new_values)
    return f

def get_common_interpolate_3d(data):
    values = data['values']
    points_x = []
    points_y = []
    points_z = []
    for point in data['points']:
        points_x.append(point[0])
        points_y.append(point[1])
        points_z.append(point[2])

    new_x = np.linspace(min(points_x), max(points_x), x_bin)
    new_y = np.linspace(min(points_y), max(points_y), y_bin)
    new_z = np.linspace(min(points_z), max(points_z), z_bin)
    new_points = np.array(np.meshgrid(new_x, new_y, new_z)).T.reshape(-1, 3)
    new_values = griddata((points_x, points_y, points_z), values, new_points, method='linear')
    lndi = LNDI(new_points, new_values)
    def f(x, y, z):
        point = [x, y, z]
        return lndi(point)
    return f

def signal_convolution(signal_original: ROOT.TH1F, pulse_responce_function, signal_convolved: ROOT.TH1F):
    so = signal_original
    pr = pulse_responce_function
    sc = signal_convolved
    t_bin = so.GetBinWidth(0) # for uniform bin
    n_bin = so.GetNbinsX()
    for i in range(n_bin):
        so_i = so.GetBinContent(i)
        for j in range(-i,n_bin-i): 
            pr_j = pr(j*t_bin)
            sc.Fill((i+j)*t_bin - 1e-14, so_i*pr_j*t_bin) # 1e-14 resolves float error
