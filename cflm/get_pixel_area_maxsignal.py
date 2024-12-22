#!/usr/bin/env python3
import os
import ROOT
import numpy
import re

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

def read_file_voltage(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time_v,volt = [],[]

        for line in lines:
            time_v.append(float(line.split()[0])*1e9)
            volt.append(float(line.split()[1])*1e3)

    time_v = numpy.array(time_v ,dtype='float64')
    volt = numpy.array(volt, dtype='float64')

    return time_v, volt

def get_current_max(file_path):
    current = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            current.append(float(columns[1])*1e6)
    currentMax = max(current) 
    return currentMax

def get_voltage_max(file_path):
    voltage = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            voltage.append(float(columns[1])*1e3)
    voltageMax = max(voltage) 
    return voltageMax

def main():
    
    nCount_curr = 0
    nCount_volt = 0
    detectorID_curr, detectorID_volt, currentMax, voltageMax = [], [], [], []

    file_path = './raser/cflm/output/pixelArea/1'

    pattern_curr = re.compile(r"DevidedAreaCurrent_(-?\d+)_(\d+).txt")
    pattern_volt = re.compile(r"PixelVoltage_(-?\d+)_(\d+).raw")
    
    for filename in os.listdir(file_path):
        if pattern_curr.match(filename):
           nCount_curr+=1
           m = int(pattern_curr.match(filename).group(1))
           n = int(pattern_curr.match(filename).group(2))
           detectorID_curr.append([m, n])
           currentMax.append(get_current_max(os.path.join(file_path, f'DevidedAreaCurrent_{m}_{n}.txt')))

           time_c, curr = [], []

           time_c, curr = read_file_current(file_path, f'DevidedAreaCurrent_{m}_{n}.txt')
           length_c = len(time_c)

           ROOT.gROOT.SetBatch()
                
           c1 = ROOT.TCanvas('c1','c1', 800, 600)
            
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

           c1.SaveAs(os.path.join(file_path, f'DevidedAreaCurrent_{m}_{n}.pdf'))
        
        if pattern_volt.match(filename):
           nCount_volt+=1
           j = int(pattern_volt.match(filename).group(1))
           k = int(pattern_volt.match(filename).group(2))
           detectorID_volt.append([j, k])
           voltageMax.append(get_voltage_max(os.path.join(file_path, f'PixelVoltage_{j}_{k}.raw')))

           time_v, volt = [], []

           time_v, volt = read_file_voltage(file_path, f'PixelVoltage_{j}_{k}.raw')
           length_v = len(time_v)

           ROOT.gROOT.SetBatch()
                
           c3 = ROOT.TCanvas('c3','c3', 800, 600)
            
           f3 = ROOT.TGraph(length_v, time_v, volt)
           f3.SetTitle(' ')
           f3.SetLineColor(2)
           f3.SetLineWidth(2)
           f3.GetXaxis().SetTitle('Time [ns]')
           f3.GetXaxis().SetLimits(0,10)
           f3.GetXaxis().CenterTitle()
           f3.GetXaxis().SetTitleSize(0.05)
           f3.GetXaxis().SetTitleOffset(0.8)
           f3.GetYaxis().SetTitle('Voltage [mV]')
           f3.GetYaxis().SetLimits(0,-5)
           f3.GetYaxis().CenterTitle()
           f3.GetYaxis().SetTitleSize(0.07)
           f3.GetYaxis().SetTitleOffset(0.7)
           f3.Draw('AL')

           c3.SaveAs(os.path.join(file_path, f'PixelVoltage_{j}_{k}.pdf'))
    
    h1 = ROOT.TH2F("h1", "Heatmap of max currrent", 40, 0, 40, 10, -5, 5)

    for n in range(len(detectorID_curr)):
        h1.Fill(detectorID_curr[n][1], detectorID_curr[n][0], currentMax[n])

    c2 = ROOT.TCanvas("c2", "Heatmap of max currrent", 1600, 800)
    
    h1.GetYaxis().SetTitle("Detector_ID_Y")
    h1.GetXaxis().SetTitle("Detector_ID_Z")
    h1.Draw("colz")

    ROOT.gStyle.SetOptStat(0)

    c2.SaveAs("raser/cflm/output/pixelArea/pixel_currentMax.pdf")
    
    h2 = ROOT.TH2F("h2", "Heatmap of max voltage", 40, 0, 40, 10, -5, 5)

    for n in range(len(detectorID_volt)):
        h2.Fill(detectorID_volt[n][1], detectorID_volt[n][0], voltageMax[n])

    c4 = ROOT.TCanvas("c4", "Heatmap of max voltage", 1600, 800)
    
    h2.GetYaxis().SetTitle("Detector_ID_Y")
    h2.GetXaxis().SetTitle("Detector_ID_Z")
    h2.Draw("colz")

    ROOT.gStyle.SetOptStat(0)

    c4.SaveAs("raser/cflm/output/pixelArea/pixel_voltageMax.pdf")
    
    print(nCount_curr)
    print(nCount_volt)

if __name__ == '__main__':
    main()