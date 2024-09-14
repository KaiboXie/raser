#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Description: 
    Simulate induced current through BB or CSA amplifier 
@Date       : 2021/09/02 14:11:57
@Author     : tanyuhang
@version    : 1.0
'''

import math
import json

import ROOT

from current.cal_current import CalCurrent

# TODO: rewriting in progress

# CSA and BB amplifier simulation
class Amplifier:
    """Get current after amplifier with convolution, for each reading electrode

    Parameters
    ---------
    my_current : CalCurrent
        The object of CalCurrent, with induced current and time information
    amplifier_name : str
        The name of amplifier, CSA or BB
    mintstep : float
        The readout time step (bin width)

    Attributes
    ---------
    ele : list
        The list of induced current after amplifier
        
    Methods
    ---------
    amplifier_define
        Define parameters and the responce function of amplifier

    sampling_charge
        Sampling the induced current with readout time step

    amplifier_simulation
        Convolute the induced current with the responce function of amplifier

    Last Modified
    ---------
        2024/09/14
    """
    def __init__(self, my_current: CalCurrent, amplifier_name: str, mintstep="50e-12"):
        self.ele = []

        ele_json = "./setting/electronics/" + amplifier_name + ".json"
        with open(ele_json) as f:
            amplifier_parameters = json.load(f)

        self.ele_name = amplifier_parameters['ele_name']
        self.read_ele_num = my_current.read_ele_num
            # each reading electrode has an induced current
        self.amplifier_define(amplifier_parameters)
        self.sampling_charge(my_current, mintstep)
        self.amplifier_simulation()

    def amplifier_define(self, amplifier_parameters: dict):
        """
        Description:
            The parameters of CSA and BB amplifier.
            Details introduction can be got in setting module.
        @Modify:
        ---------
            2021/09/09
        """
        self.CDet = amplifier_parameters['CDet']

        if amplifier_parameters['ele_name'] == 'CSA':
            """ CSA parameter initialization"""
            self.t_rise    = amplifier_parameters['t_rise']
            self.t_fall    = amplifier_parameters['t_fall']
            self.trans_imp = amplifier_parameters['trans_imp']

            t_rise = self.t_rise
            t_fall = self.t_fall
            self.tau_rise = t_rise/2.2*1e-9
            self.tau_fall = t_fall/2.2*1e-9
            if (self.tau_rise == self.tau_fall):
                self.tau_rise *= 0.9
            self.sh_max = 0.0  

            self.fill_amplifier_output = self.fill_amplifier_output_CSA
            self.set_scope_output = self.set_scope_output_CSA

        elif amplifier_parameters['ele_name'] == 'BB':
            """ BB parameter initialization"""
            self.BBW       = amplifier_parameters['BBW']
            self.BBGain    = amplifier_parameters['BBGain']
            self.BB_imp    = amplifier_parameters['BB_imp']
            self.OscBW     = amplifier_parameters['OscBW'] 

            tau_C50 = 1.0e-12*50.*self.CDet          #Oscil. RC
            tau_BW = 0.35/(1.0e9*self.OscBW)/2.2      #Oscil. RC
            tau_BB_RC = 1.0e-12*self.BB_imp*self.CDet     #BB RC
            tau_BB_BW = 0.35/(1.0e9*self.BBW)/2.2    #BB Tau
            self.tau_scope = math.sqrt(pow(tau_C50,2)+pow(tau_BW,2))
            self.tau_BBA = math.sqrt(pow(tau_BB_RC,2)+pow(tau_BB_BW,2))

            self.fill_amplifier_output = self.fill_amplifier_output_BB
            self.set_scope_output = self.set_scope_output_BB

    def sampling_charge(self, my_current: CalCurrent, mintstep: float):
        """ Transform current to charge 
        with changing bin width to oscilloscope bin width
        """
        self.max_num=[]
        self.itot=[]
        for i in range(self.read_ele_num):
            self.max_num.append(my_current.sum_cu[i].GetNbinsX())
            self.itot.append([0.0]*self.max_num[i])

        self.max_hist_num = my_current.n_bin
        self.undersampling = int(float(mintstep)/my_current.t_bin)
        self.time_unit = my_current.t_bin*self.undersampling
        self.CDet_j = 0     # CSA readout mode
        
        self.qtot = [0.0]*self.read_ele_num
        # self.qtot = [0.0]
        # get total charge
        for k in range(self.read_ele_num):
            i=0
            for j in range(0,self.max_hist_num,self.undersampling):
                self.itot[k][i] = my_current.sum_cu[k].GetBinContent(j)
                self.qtot[k] = self.qtot[k] + self.itot[k][i]*self.time_unit
                i+=1

    def amplifier_simulation(self):
        """
        Description:
            CSA and BB amplifier Simulation         
        Parameters:
        ---------
        arg1 : int
            
        @Modify:
        ---------
            2021/09/09
        """
        max_hist_num = int(self.max_hist_num/self.undersampling)

        # Variable Initialization
        if self.ele_name == 'CSA':
            IintTime = 2.0*(self.t_rise+self.t_fall)*1e-9/self.time_unit
            IMaxSh = int(max_hist_num + IintTime)
            self.shaper_out_Q = [0.0]*IMaxSh
        elif self.ele_name == 'BB':
            IintTime = 3.0*self.tau_BBA/self.time_unit
            IMaxSh = int(max_hist_num + IintTime)
            self.Iout_BB_RC = [0.0]*IMaxSh
            self.Iout_C50 = [0.0]*IMaxSh   
            self.BBGraph = [0.0]*IMaxSh

        self.Vout_scope = [0.0]*IMaxSh

        preamp_Q = [] 
        for i in range(self.read_ele_num):
            preamp_Q.append([0.0]*IMaxSh)

        # step for convolution delay
        step = 1

        for k in range(self.read_ele_num):
            for i in range(IMaxSh-step):
                if(i>0 and i <self.max_hist_num-step):
                    preamp_Q[k][i] = 0.0
                    for il in range(i,i+step):
                        preamp_Q[k][i] += self.itot[k][il]*self.time_unit
                elif (i != 0):
                    preamp_Q[k][i]=0.0

        for k in range(self.read_ele_num):
            for i in range(IMaxSh-step):
                if i >= step:
                    dif_shaper_Q = preamp_Q[k][i]
                else:
                    dif_shaper_Q = 0
                for j in range(IMaxSh-i):
                    self.fill_amplifier_output(i, j, dif_shaper_Q)
                self.set_scope_output(i, k)
            self.fill_th1f(k, IMaxSh)

    def fill_amplifier_output_CSA(self, i, j, dif_shaper_Q: float):
        """ Fill CSA out signal, charge"""   
        self.shaper_out_Q[i+j] += self.tau_fall/(self.tau_fall+self.tau_rise) \
                                  * dif_shaper_Q*(math.exp(-j*self.time_unit
                                  / self.tau_fall)-math.exp(
                                  - j*self.time_unit/self.tau_rise))

    def fill_amplifier_output_BB(self, i, j, dif_shaper_Q: float):
        """ Fill BB out signal, current"""   
        self.Iout_C50[i+j] += (dif_shaper_Q)/self.tau_scope \
                                * math.exp(-j*self.time_unit/self.tau_scope)
        self.Iout_BB_RC[i+j] += (dif_shaper_Q)/self.tau_BBA \
                                * math.exp(-j*self.time_unit/self.tau_BBA)

    def set_scope_output_CSA(self, i, k):
        Ci = 3.5e-11  #fF
        Qfrac = 1.0/(1.0+self.CDet*1e-12/Ci)
        Q_max = max(self.shaper_out_Q) if max(self.shaper_out_Q) > 0 else min(self.shaper_out_Q)
        if Q_max == 0.0:
            self.Vout_scope[i] = 0.0
        elif self.CDet_j == 0:
            self.Vout_scope[i] = self.shaper_out_Q[i]*self.trans_imp\
                                    * 1e15*self.qtot[k]*Qfrac/Q_max     
            # self.Vout_scope[i] = self.shaper_out_Q[i]*self.trans_imp/(self.CDet*1e-12) #C_D=3.7pF   
        elif self.CDet_j == 1:
            self.Vout_scope[i] = self.shaper_out_Q[i]*self.trans_imp\
                                    * 1e15*self.qtot[k]/Q_max
            
    def set_scope_output_BB(self, i, k):
        self.BBGraph[i] = 1e3 * self.BBGain * self.Iout_BB_RC[i]
        R_in = 50 # the input impedance of the amplifier
        self.Vout_scope[i] = R_in * self.Iout_C50[i]
 
    def fill_th1f(self, k, IMaxSh):
        """ Change amplifier outputs
            to oscilloscope amplitude [mV]
            and save in the TH1F
        """
        self.ele.append(ROOT.TH1F("electronics %s"%(self.ele_name)+str(k+1), "electronics %s"%(self.ele_name),
                                IMaxSh, 0, IMaxSh*self.time_unit))
        # get the max absolute value of the shaper output
        
        for i in range(IMaxSh):
            self.ele[k].SetBinContent(i,self.Vout_scope[i])
        #Print the max current time of CSA
        V_max = max(self.Vout_scope) if max(self.Vout_scope) > 0 else min(self.Vout_scope)
        t_max = self.Vout_scope.index(V_max)
        print("peak time={:.2e}".format(t_max*self.time_unit))

    def __del__(self):
        pass
