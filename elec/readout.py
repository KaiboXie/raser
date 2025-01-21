#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Description: 
    Simulate induced current through Broad_Band or Charge_Sensitive amplifier 
@Date       : 2024/09/22 15:24:33
@Author     : tanyuhang, Chenxi Fu
@version    : 2.0
'''

import math
import csv
import json
from array import array
import os

import ROOT
ROOT.gROOT.SetBatch(True)

from util.math import signal_convolution
from util.output import output

class Amplifier:
    """Get current after amplifier with convolution, for each reading electrode

    Parameters
    ---------
    currents : list[ROOT.TH1F]
        The ROOT.TH1F objects of induced current with time information

    amplifier_name : str
        The name of the amplifier

    CDet : None | float
        The capacitance of the detector

    Attributes
    ---------
    amplified_current : list[ROOT.TH1F]
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
    def __init__(self, currents: list[ROOT.TH1F], amplifier_name: str, CDet = None):
        self.amplified_current = []

        ele_json = "./setting/electronics/" + amplifier_name + ".json"
        with open(ele_json) as f:
            self.amplifier_parameters = json.load(f)

        self.amplified_current_name = self.amplifier_parameters['ele_name']
        self.read_ele_num = len(currents)

        self.amplifier_define(CDet)
        self.fill_amplifier_output(currents)
        self.set_scope_output(currents)

    def amplifier_define(self, CDet):
        """
        Description:
            The parameters, pulse responce function and scope scaling of the amplifier.
            Details introduction can be got in setting module.
        @Modify:
        ---------
            2021/09/09
        """
        if CDet is None:
            CDet = self.amplifier_parameters['CDet']

        if self.amplifier_parameters['ele_name'] == 'Charge_Sensitive':
            """ Current Sensitive Amplifier parameter initialization"""

            mode = 0

            def pulse_responce_Charge_Sensitive(t):
                if t < 0: # step function
                    return 0

                t_rise   = self.amplifier_parameters['t_rise']
                t_fall   = self.amplifier_parameters['t_fall']

                tau_rise = t_rise/2.2*1e-9
                tau_fall = t_fall/2.2*1e-9
                if (tau_rise == tau_fall):
                    tau_rise *= 0.9

                return tau_fall/(tau_fall+tau_rise) * (math.exp(-t/tau_fall)-math.exp(-t/tau_rise))

            def scale_Charge_Sensitive(output_Q_max, input_Q_tot):
                """ Current Sensitive Amplifier scale function"""
                trans_imp = self.amplifier_parameters['trans_imp']
                Ci = 3.5e-11  #fF
                Qfrac = 1.0/(1.0+CDet*1e-12/Ci)

                if output_Q_max == 0.0:
                    return 0.0
            
                if mode == 0:
                    scale = trans_imp * 1e15 * input_Q_tot * Qfrac / output_Q_max     
                    # scale = trans_imp/(self.CDet*1e-12) #C_D=3.7pF   
                elif mode == 1:
                    scale = trans_imp * 1e15 * input_Q_tot / output_Q_max

                return scale

            self.pulse_responce_list = [pulse_responce_Charge_Sensitive]
            self.scale = scale_Charge_Sensitive

        elif self.amplifier_parameters['ele_name'] == 'Broad_Band':
            """ Broad Bandwidth Amplifier (Charge Sensitive Amplifier) parameter initialization"""

            mode = "scope"

            def pulse_responce_Broad_Band(t):
                if t < 0: # step function
                    return 0
                
                Broad_Band_Bandwidth = self.amplifier_parameters['Broad_Band_Bandwidth']
                Broad_Band_Imp       = self.amplifier_parameters['Broad_Band_Imp']
                OscBW        = self.amplifier_parameters['OscBW']   
                
                if mode == "scope":
                    tau_C50 = 1.0e-12 * 50. * CDet          #Oscil. RC
                    tau_BW = 0.35 / (1.0e9*OscBW) / 2.2      #Oscil. RC
                    tau_scope = math.sqrt(pow(tau_C50,2)+pow(tau_BW,2))

                    return 1/tau_scope * math.exp(-t/tau_scope)

                elif mode == "RC":
                    tau_Broad_Band_RC = 1.0e-12 * Broad_Band_Imp * CDet     #Broad_Band RC
                    tau_Broad_Band_BW = 0.35 / (1.0e9*Broad_Band_Bandwidth) / 2.2    #Broad_Band Tau, Rf*Cf?
                    tau_Broad_Band = math.sqrt(pow(tau_Broad_Band_RC,2)+pow(tau_Broad_Band_BW,2))

                    return 1/tau_Broad_Band * math.exp(-t/tau_Broad_Band)
                
                else:
                    raise NameError(mode,"mode is not defined")
                
            def scale_Broad_Band(output_Q_max, input_Q_tot):
                """ Broad Bandwidth Amplifier (Charge Sensitive Amplifier) scale function"""

                if mode == "scope":
                    R_in = 50
                    return R_in

                elif mode == "RC":
                    Broad_Band_Gain = self.amplifier_parameters['Broad_Band_Gain'] # kOhm ?
                    return Broad_Band_Gain * 1e3
                
            self.pulse_responce_list = [pulse_responce_Broad_Band]
            self.scale = scale_Broad_Band

        elif self.amplifier_parameters['ele_name'] == 'ABCStar_fe':
            """ ABCStar Front-end Amplifier parameter initialization"""

            def pulse_responce_ABCStar_fe_input(t):
                if t < 0:
                    return 0
                input_res = self.amplifier_parameters['input_res']
                return 1/(1e-12*CDet) * math.exp(-t/(1e-12*CDet*input_res))
            
            def pulse_responce_ABCStar_fe_RCfeedback(t):
                if t < 0:
                    return 0
                input_res = self.amplifier_parameters['input_res']
                Cf = self.amplifier_parameters['Cf']
                Rf = self.amplifier_parameters['Rf']
                tau_amp = 1e-12 * Cf * input_res
                tau_f = 1e-12 * Cf * Rf
                return 1/tau_amp * math.exp(-t/tau_f)
            
            def scale_ABCStar_fe(output_Q_max, input_Q_tot):
                """ ABCStar Front-end Amplifier scale function"""
                return 1000.0 # V to mV
            
            self.pulse_responce_list = [pulse_responce_ABCStar_fe_input, pulse_responce_ABCStar_fe_RCfeedback]
            self.scale = scale_ABCStar_fe


    def fill_amplifier_output(self, currents: list[ROOT.TH1F]):
        for i in range(self.read_ele_num):
            cu = currents[i]
            self.amplified_current.append(ROOT.TH1F("electronics %s"%(self.amplified_current_name)+str(i+1), "electronics %s"%(self.amplified_current_name),
                                cu.GetNbinsX(),cu.GetXaxis().GetXmin(),cu.GetXaxis().GetXmax()))
            self.amplified_current[i].Reset()
            signal_convolution(cu, self.amplified_current[i], self.pulse_responce_list)
    
    def set_scope_output(self, currents: list[ROOT.TH1F]):
        for i in range(self.read_ele_num):
            cu = currents[i]
            input_Q_tot = cu.Integral()
            output_Q_max = self.amplified_current[i].GetMaximum()
            self.amplified_current[i].Scale(self.scale(output_Q_max, input_Q_tot))

    def save_signal_TTree(self, path, key):
        if key == None:
            key = ""
        for j in range(self.read_ele_num):
            volt = array('d', [0.])
            time = array('d', [0.])
            if self.read_ele_num==1:
                fout = ROOT.TFile(os.path.join(path, "amplified-current") + str(key) + ".root", "RECREATE")
            else:
                fout = ROOT.TFile(os.path.join(path, "amplified-current") + str(key)+"No_"+str(j)+".root", "RECREATE")
            t_out = ROOT.TTree("tree", "signal")
            t_out.Branch("volt", volt, "volt/D")
            t_out.Branch("time", time, "time/D")
            for i in range(self.amplified_current[j].GetNbinsX()):
                time[0]=i*self.amplified_current[j].GetBinWidth(i)
                volt[0]=self.amplified_current[j][i]
                t_out.Fill()
            t_out.Write()
            fout.Close()
        for j in range(self.read_ele_num):
            if self.read_ele_num==1:
                # 打开 ROOT 文件
                root_file = ROOT.TFile(os.path.join(path, "amplified-current") + str(key) + ".root", "READ")
                # 创建 CSV 文件名
                csv_file_name = os.path.join(path, "amplified-current") + str(key) + ".csv"
            else:
                # 打开 ROOT 文件
                root_file = ROOT.TFile(os.path.join(path, "amplified-current") + str(key)+"No_"+str(j)+".root", "READ")
                # 创建 CSV 文件名
                csv_file_name = os.path.join(path, "amplified-current") + str(key)+"No_"+str(j) + ".csv"
            # 获取 ROOT 文件中的 TTree
            tree = root_file.Get("tree")
            if tree:
                print(tree)
                print(tree.GetListOfBranches())
            # 打开 CSV 文件，使用 'w' 模式表示写入
            with open(csv_file_name, mode='w', newline='') as file:
                writer = csv.writer(file)  # 创建 CSV writer 对象
                # 写入 CSV 文件的表头（字段名）
                header = [branch.GetName() for branch in tree.GetListOfBranches()]
                writer.writerow(header)
                # 遍历 TTree 中的数据，将数据写入 CSV 文件
                for event in tree:
                    data = [event.GetLeaf(branch.GetName()).GetValue() for branch in tree.GetListOfBranches()]
                    writer.writerow(data)

def main(label):
    '''main function for readout.py to test the output of the given amplifier'''

    my_th1f = ROOT.TH1F("my_th1f", "my_th1f", 600, 0, 30e-9)
    # input signal: square pulse
    for i in range(21, 41):
        my_th1f.SetBinContent(i, 2e-6) # A

    ele = Amplifier([my_th1f], label)

    c=ROOT.TCanvas("c","canvas1",1000,1000)
    my_th1f.Draw("HIST")

    origin_max = my_th1f.GetMaximum()
    amp_max = ele.amplified_current[0].GetMaximum()
    print("amp_max =",amp_max,'mV')

    ratio = origin_max/amp_max
    ele.amplified_current[0].Scale(ratio)
    ele.amplified_current[0].Draw("SAME HIST")

    path = output(__file__, label)
    c.SaveAs(path+'/'+label+'_test.pdf')

if __name__ == '__main__':
    import sys
    main(sys.argv[1])