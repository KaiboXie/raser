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
