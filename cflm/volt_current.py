#!/usr/bin/env python3
import sys
import json

import ROOT
ROOT.gROOT.SetBatch(True)
import numpy


def read_file_voltage(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time_v,volt = [],[]

        for line in lines:
            time_v.append(float(line.split()[0])*1e9)
            volt.append(float(line.split()[1])*1e3)

    time_v = numpy.array(time_v ,dtype='float64')
    volt = numpy.array(volt,dtype='float64')

    return time_v,volt

def read_file_current(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time_c,curr = [],[]

        for line in lines:
            time_c.append(float(line.split()[0])*1e9)
            curr.append(float(line.split()[1])*1e6)

    time_c = numpy.array(time_c ,dtype='float64')
    curr = numpy.array(curr, dtype='float64')

    return time_c, curr


def main():
    file_path = './raser/cflm/output'
    
    geant4_json = "./setting/absorber/cflm.json"
    with open(geant4_json) as f:
         g4_dic = json.load(f)

    file_name_v = g4_dic['CurrentName'].split('.')[0] + '.raw'
    file_name_c = g4_dic['CurrentName'].split('.')[0] + '_pwl_current.txt'

    time_v, volt, time_c, curr = [], [], [], []

    time_v, volt = read_file_voltage(file_path,file_name_v)
    length_v = len(time_v)
    time_c, curr = read_file_current(file_path,file_name_c)
    length_c = len(time_c)


    ROOT.gROOT.SetBatch()
        
    c = ROOT.TCanvas('c','c',4000,2000)
    
    pad1 = ROOT.TPad("pad1", "pad1", 0.05, 0.05, 0.45, 0.95)
    pad2 = ROOT.TPad("pad2", "pad2", 0.55, 0.05, 0.95, 0.95)

    pad1.Draw()
    pad2.Draw()
    
    pad1.cd()
    f1 = ROOT.TGraph(length_c, time_c, curr)
    f1.SetTitle(' ')
    f1.SetLineColor(2)
    f1.SetLineWidth(2)
    f1.GetXaxis().SetTitle('Time [ns]')
    f1.GetXaxis().SetLimits(0,10)
    f1.GetXaxis().CenterTitle()
    f1.GetXaxis().SetTitleSize(0.05)
    f1.GetXaxis().SetTitleOffset(0.8)
    f1.GetYaxis().SetTitle('Current [uA]')
    f1.GetYaxis().SetLimits(0,-5)
    f1.GetYaxis().CenterTitle()
    f1.GetYaxis().SetTitleSize(0.07)
    f1.GetYaxis().SetTitleOffset(0.7)
    f1.Draw('AL')
    pad1.Update()

    pad2.cd()
    f2 = ROOT.TGraph(length_v, time_v, volt)
    f2.SetTitle(' ')
    f2.SetLineColor(2)
    f2.SetLineWidth(2)
    f2.GetXaxis().SetTitle('Time [ns]')
    f2.GetXaxis().SetLimits(0,10)
    f2.GetXaxis().CenterTitle()
    f2.GetXaxis().SetTitleSize(0.05)
    f2.GetXaxis().SetTitleOffset(0.8)
    f2.GetYaxis().SetTitle('Voltage [mV]')
    f2.GetYaxis().SetLimits(0,-5)
    f2.GetYaxis().CenterTitle()
    f2.GetYaxis().SetTitleSize(0.07)
    f2.GetYaxis().SetTitleOffset(0.7)
    f2.Draw('AL')
    pad2.Update()


    c.SaveAs(f"Current_Voltage_{g4_dic['CurrentName'].split('.')[0]}.pdf")
    
