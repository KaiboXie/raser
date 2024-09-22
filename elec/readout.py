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

from util.math import signal_convolution
from util.output import output

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
    def __init__(self, currents: list[ROOT.TH1F], amplifier_name: str, time_step = time_step):
        self.amplified_current = []

        ele_json = "./setting/electronics/" + amplifier_name + ".json"
        with open(ele_json) as f:
            self.amplifier_parameters = json.load(f)

        self.amplified_current_name = self.amplifier_parameters['ele_name']
        self.read_ele_num = len(currents)

        self.amplifier_define()
        self.fill_amplifier_output(currents, time_step)
        self.set_scope_output(currents)

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
                    return 0.0
            
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

    def fill_amplifier_output(self, currents: list[ROOT.TH1F], time_step):
        for i in range(self.read_ele_num):
            cu = currents[i]
            n_bin = cu.GetNbinsX()
            t_bin = cu.GetBinWidth(0)
            time_duration = n_bin * t_bin
            self.amplified_current.append(ROOT.TH1F("electronics %s"%(self.amplified_current_name)+str(i+1), "electronics %s"%(self.amplified_current_name),
                                int(time_duration/time_step), 0, time_duration))
            self.amplified_current[i].Reset()
            signal_convolution(cu, self.pulse_responce, self.amplified_current[i])
    
    def set_scope_output(self, currents: list[ROOT.TH1F]):
        for i in range(self.read_ele_num):
            cu = currents[i]
            input_Q_tot = cu.Integral()
            output_Q_max = self.amplified_current[i].GetMaximum()
            self.amplified_current[i].Scale(self.scale(output_Q_max, input_Q_tot))

def main(label):
    '''main function for readout.py to test the output of the given amplifier'''

    my_th1f = ROOT.TH1F("my_th1f", "my_th1f", 200, 0, 10e-9)
    # input signal: square pulse
    for i in range(21, 41):
        my_th1f.SetBinContent(i, 1e-5)

    ele = Amplifier([my_th1f], label)

    c=ROOT.TCanvas("c","canvas1",1000,1000)
    my_th1f.Draw("HIST")

    origin_max = my_th1f.GetMaximum()
    amp_max = ele.amplified_current[0].GetMaximum()
    ratio = origin_max/amp_max
    ele.amplified_current[0].Scale(ratio)
    ele.amplified_current[0].Draw("SAME HIST")
    
    path = output(__file__, label)
    c.SaveAs(path+'/'+label+'_test.pdf')

if __name__ == '__main__':
    import sys
    main(sys.argv[1])