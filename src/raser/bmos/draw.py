#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@Date       : 2023
@Author     : Ye He, Kaibo Xie
@version    : 2.0
'''

import os
import json
import ROOT
ROOT.gROOT.SetBatch(True)
import numpy

from ..util.output import output, create_path

def readfile(path, root_name): 
    file = ROOT.TFile(os.path.join(path, root_name), "READ")
    tree = file.Get("tree")

    amplitudes = []
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        amplitudes.append(tree.amplitudes)

    file.Close()
    return amplitudes

def data(root_path, root_name):
    file_name = os.path.splitext(root_name)[0]
    amplitudes = readfile(root_path, root_name)

    return amplitudes, file_name

def DrawHis(amplitudes, file_name):
    c = ROOT.TCanvas( 'c', 'c', 8000, 6000 )
    c.cd()
    minsignal = float(min(amplitudes))
    maxsignal = float(max(amplitudes))
    print(minsignal, maxsignal)
    binnum = 50
    binwidth = (maxsignal - minsignal)/binnum
    wave_graph = ROOT.TH1F('','', binnum + 2, minsignal - binwidth, maxsignal + binwidth)
    for amplitude in amplitudes:
        wave_graph.Fill(amplitude)

    f1 = ROOT.TF1("f1", "landau")
    wave_graph.Fit(f1)

    wave_graph.SetTitle(file_name)
    wave_graph.SetLineColor(1)
    wave_graph.SetLineWidth(2)

    wave_graph.GetXaxis().SetTitle('mV')
    wave_graph.GetXaxis().SetTitleSize(0.05)
    wave_graph.GetXaxis().SetTitleOffset(0.9)

    wave_graph.GetYaxis().SetTitle('events')
    wave_graph.GetYaxis().SetTitleSize(0.05)
    wave_graph.GetYaxis().SetTitleOffset(0.9)

    wave_graph.Draw()
    maxevent = wave_graph.GetMaximum()

    latex = ROOT.TLatex(0.4*minsignal + 0.6*maxsignal, 0.7*maxevent, f"MPV:{round(f1.GetParameter(1), 3)}mV")
    latex.SetTextSize(0.05)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.Draw()

    create_path(os.path.join(output(__file__), 'histogram', 'pdf'))

    c.SaveAs(os.path.join(output(__file__), 'histogram', 'pdf', f"{file_name}.pdf"))

def DrawHistogram():
    geant4_json = os.getenv("RASER_SETTING_PATH")+"/g4experiment/bmos.json"
    with open(geant4_json) as f:
        g4_dic = json.load(f)
    tag = f"{g4_dic['par_type']}_{g4_dic['par_energy']}MeV"
    root_path = os.path.join(output(__file__), tag)
    root_names = [i for i in os.listdir(root_path) if "amplitudes" in i]

    for root_name in root_names:
        amplitudes, file_name = data(root_path, root_name)
        DrawHis(amplitudes, file_name)

    c = ROOT.TCanvas( 'c', 'c', 8000, 6000)
    his = []
    for i in range(len(root_names)):
        c.cd()
        amplitudes, file_name = data(root_path, root_names[i])
        # DrawHis(amplitudes, file_name)
        his.append(ROOT.TH1F('','', 150, 0, 1500))

        for amplitude in amplitudes:
            his[i].Fill(amplitude)

        his[i].Draw("same")
        his[i].Fit("landau")

        his[i].SetTitle(tag)
        his[i].SetLineColor(1)
        his[i].SetLineWidth(2)

        his[i].GetXaxis().SetTitle('mV')
        his[i].GetXaxis().SetTitleSize(0.05)
        his[i].GetXaxis().SetTitleOffset(0.9)

        his[i].GetYaxis().SetTitle('events')
        his[i].GetYaxis().SetTitleSize(0.05)
        his[i].GetYaxis().SetTitleOffset(0.9)
        his[i].GetYaxis().SetRangeUser(0, 150)

    create_path(os.path.join(output(__file__), 'histogram', 'pdf'))
    c.SaveAs(os.path.join(output(__file__), 'histogram', 'pdf', f"amplitudes_{tag}_all.pdf"))
    
def read_file_voltage(file_path, file_name):
    with open(os.path.join(file_path, file_name)) as f:
        lines = f.readlines()
        time_v,volt = [],[]

        for line in lines:
            time_v.append(float(line.split()[0])*1e9)
            volt.append(float(line.split()[1])*1e3)

    time_v = numpy.array(time_v ,dtype='float64')
    volt = numpy.array(volt,dtype='float64')

    return time_v, volt

def read_file_current(file_path, file_name):
    with open(os.path.join(file_path, file_name)) as f:
        lines = f.readlines()
        time_c,curr = [],[]

        for line in lines:
            time_c.append(float(line.split()[0])*1e9)
            curr.append(float(line.split()[1])*1e6)

    time_c = numpy.array(time_c ,dtype='float64')
    curr = numpy.array(curr, dtype='float64')

    return time_c, curr

def DrawSignal():
    geant4_json = os.getenv("RASER_SETTING_PATH")+"/g4experiment/bmos.json"
    with open(geant4_json) as f:
        g4_dic = json.load(f)
    tag = f"{g4_dic['par_type']}_{g4_dic['par_energy']}MeV_{g4_dic['par_num']}particle"
    dirname = f"{g4_dic['par_type']}_{g4_dic['par_energy']}MeV"
    pwl_name = f"pwl{g4_dic['CurrentName'].split('.')[0]}.txt"
    ngspice_output = f"UCSC_output.raw"
    file_path = os.path.join(output(__file__), dirname)
    output_path = os.path.join(output(__file__), "signal", "pdf")
    create_path(output_path)

    file_name_v = ngspice_output
    file_name_c = pwl_name

    time_v, volt, time_c, curr = [], [], [], []

    time_v, volt = read_file_voltage(file_path,file_name_v)
    length_v = len(time_v)
    time_c, curr = read_file_current(os.path.join(output(__file__), "tmp"),file_name_c)
    length_c = len(time_c)

    ROOT.gROOT.SetBatch()
    c = ROOT.TCanvas('c','c',4000,2000)
    
    pad1 = ROOT.TPad("pad1", "pad1", 0.05, 0.05, 0.45, 0.95)
    pad2 = ROOT.TPad("pad2", "pad2", 0.55, 0.05, 0.95, 0.95)

    pad1.Draw()
    pad2.Draw()
    
    pad1.cd()
    f1 = ROOT.TGraph(length_c, time_c, curr)
    f1.SetTitle("Detector output")
    f1.SetLineColor(2)
    f1.SetLineWidth(2)
    f1.GetXaxis().SetTitle('Time [ns]')
    f1.GetXaxis().SetLimits(0,10)
    f1.GetXaxis().CenterTitle()
    f1.GetXaxis().SetTitleSize(0.05)
    f1.GetXaxis().SetTitleOffset(0.8)
    f1.GetYaxis().SetTitle('Current [uA]')
    # f1.GetYaxis().SetLimits(0,-5)
    f1.GetYaxis().CenterTitle()
    f1.GetYaxis().SetTitleSize(0.07)
    f1.GetYaxis().SetTitleOffset(0.7)
    f1.Draw('AL')
    pad1.Update()

    pad2.cd()
    f2 = ROOT.TGraph(length_v, time_v, volt)
    f2.SetTitle("UCSC output")
    f2.SetLineColor(2)
    f2.SetLineWidth(2)
    f2.GetXaxis().SetTitle('Time [ns]')
    f2.GetXaxis().SetLimits(0,10)
    f2.GetXaxis().CenterTitle()
    f2.GetXaxis().SetTitleSize(0.05)
    f2.GetXaxis().SetTitleOffset(0.8)
    f2.GetYaxis().SetTitle('Voltage [mV]')
    # f2.GetYaxis().SetLimits(0,-5)
    f2.GetYaxis().CenterTitle()
    f2.GetYaxis().SetTitleSize(0.07)
    f2.GetYaxis().SetTitleOffset(0.7)
    f2.Draw('AL')
    pad2.Update()

    c.SaveAs(os.path.join(output_path, f"signal_{tag}.pdf"))