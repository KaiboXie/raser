#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Description: 
    Simulate induced current through BB or CSA amplifier 
@Date       : 2024/09/22 15:24:33
@Author     : tanyuhang, Chenxi Fu
@version    : 2.0
'''

import math
import json

import ROOT

from current.cal_current import CalCurrent
from util.math import signal_convolution

time_step = 50e-12

class Amplifier:
    """Get current after amplifier with convolution, for each reading electrode

    Parameters
    ---------
    my_current : CalCurrent
        The object of CalCurrent, with induced current and time information

    amplifier_name : str
        The name of amplifier

    time_step : float
        The readout time step (bin width)

    Attributes
    ---------
    ele : list
        The list of induced current after amplifier
        
    Methods
    ---------
    amplifier_define
        Define parameters and the responce function of amplifier

    fill_amplifier_output
        Get the induced current after amplifier

    set_scope_output
        Get the scope output after amplifier

    Last Modified
    ---------
        2024/09/14
    """
    def __init__(self, my_current: CalCurrent, amplifier_name: str, time_step = time_step):
        self.ele = []

        ele_json = "./setting/electronics/" + amplifier_name + ".json"
        with open(ele_json) as f:
            self.amplifier_parameters = json.load(f)

        self.ele_name = self.amplifier_parameters['ele_name']
        self.read_ele_num = my_current.read_ele_num

        self.amplifier_define()
        self.fill_amplifier_output(my_current, time_step)
        self.set_scope_output(my_current)

    def amplifier_define(self):
        """
        Description:
            The parameters, pulse responce function and scope scaling of the amplifier.
            Details introduction can be got in setting module.
        @Modify:
        ---------
            2021/09/09
        """
        CDet = self.amplifier_parameters['CDet']

        if self.amplifier_parameters['ele_name'] == 'CSA':
            """ CSA parameter initialization"""

            mode = 0

            def pulse_responce_CSA(t):
                if t < 0: # step function
                    return 0

                t_rise   = self.amplifier_parameters['t_rise']
                t_fall   = self.amplifier_parameters['t_fall']

                tau_rise = t_rise/2.2*1e-9
                tau_fall = t_fall/2.2*1e-9
                if (tau_rise == tau_fall):
                    tau_rise *= 0.9

                return tau_fall/(tau_fall+tau_rise) * (math.exp(-t/tau_fall)-math.exp(-t/tau_rise))

            def scale_CSA(output_Q_max, input_Q_tot):
                """ CSA scale function"""
                trans_imp = self.amplifier_parameters['trans_imp']
                Ci = 3.5e-11  #fF
                Qfrac = 1.0/(1.0+self.CDet*1e-12/Ci)

                if output_Q_max == 0.0:
                    scale = 0.0
            
                if mode == 0:
                    scale = trans_imp * 1e15 * input_Q_tot * Qfrac / output_Q_max     
                    # scale = trans_imp/(self.CDet*1e-12) #C_D=3.7pF   
                elif mode == 1:
                    scale = trans_imp * 1e15 * input_Q_tot / output_Q_max

                return scale

            self.pulse_responce = pulse_responce_CSA
            self.scale = scale_CSA

        elif self.amplifier_parameters['ele_name'] == 'BB':
            """ BB parameter initialization"""

            mode = "scope"

            def pulse_responce_BB(t):
                if t < 0: # step function
                    return 0
                
                BB_bandwidth = self.amplifier_parameters['BB_bandwidth']
                BB_imp       = self.amplifier_parameters['BB_imp']
                OscBW        = self.amplifier_parameters['OscBW']   
                
                if mode == "scope":
                    tau_C50 = 1.0e-12 * 50. * CDet          #Oscil. RC
                    tau_BW = 0.35 / (1.0e9*OscBW) / 2.2      #Oscil. RC
                    tau_scope = math.sqrt(pow(tau_C50,2)+pow(tau_BW,2))

                    return 1/tau_scope * math.exp(-t/tau_scope)

                elif mode == "RC":
                    tau_BB_RC = 1.0e-12 * BB_imp * CDet     #BB RC
                    tau_BB_BW = 0.35 / (1.0e9*BB_bandwidth) / 2.2    #BB Tau
                    tau_BBA = math.sqrt(pow(tau_BB_RC,2)+pow(tau_BB_BW,2))

                    return 1/tau_BBA * math.exp(-t/tau_BBA)
                
                else:
                    raise NameError(mode,"mode is not defined")
                
            def scale_BB(output_Q_max, input_Q_tot):
                """ BB scale function"""

                if mode == "scope":
                    R_in = 50
                    return R_in

                elif mode == "RC":
                    BBGain = self.amplifier_parameters['BBGain']
                    return BBGain * 1e3
                
            self.pulse_responce = pulse_responce_BB
            self.scale = scale_BB

    def fill_amplifier_output(self, my_current, time_step):
        for i in range(self.read_ele_num):
            sum_cu = my_current.sum_cu[i]
            n_bin = sum_cu.GetNbinsX()
            t_bin = sum_cu.GetBinWidth(0)
            time_duration = n_bin * t_bin
            self.ele.append(ROOT.TH1F("electronics %s"%(self.ele_name)+str(i+1), "electronics %s"%(self.ele_name),
                                int(time_duration/time_step), 0, time_duration))
            self.ele[i].Reset()
            signal_convolution(sum_cu, self.pulse_responce, self.ele[i])
    
    def set_scope_output(self, my_current):
        for i in range(self.read_ele_num):
            sum_cu = my_current.sum_cu[i]
            input_Q_tot = sum_cu.Integral()
            output_Q_max = self.ele[i].GetMaximum()
            self.ele[i].Scale(self.scale(output_Q_max, input_Q_tot))
