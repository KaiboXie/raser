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

def get_current_max(file_path):
    current = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            current.append(float(columns[1])*1e6)
    currentMax = max(current) 
    return currentMax

def main():
    
    nCount = 0
    detectorID, currentMax = [], []

    file_path = './raser/cflm/output/pixelArea'

    pattern = re.compile(r"DevidedAreaCurrent_(-?\d+)_(\d+).txt")
    for filename in os.listdir(file_path):
        if pattern.match(filename):
           nCount+=1
           m = int(pattern.match(filename).group(1))
           n = int(pattern.match(filename).group(2))
           detectorID.append([m, n])
           currentMax.append(get_current_max(os.path.join(file_path, f'DevidedAreaCurrent_{m}_{n}.txt')))

           time_c, curr = [], []

           time_c, curr = read_file_current(file_path, f'DevidedAreaCurrent_{m}_{n}.txt')
           length_c = len(time_c)

           ROOT.gROOT.SetBatch()
                
           c1 = ROOT.TCanvas('c','c', 800, 600)
            
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
    
           h1 = ROOT.TH2F("hist", "Heatmap of max currrent", 40, 0, 40, 10, -5, 5)

           for n in range(len(detectorID)):
               h1.Fill(detectorID[n][1], detectorID[n][0], currentMax[n])

           c2 = ROOT.TCanvas("canvas", "Heatmap of max currrent", 1600, 800)
    
           h1.GetYaxis().SetTitle("Detector_ID_Y")
           h1.GetXaxis().SetTitle("Detector_ID_Z")
           h1.Draw("colz")

           ROOT.gStyle.SetOptStat(0)

           c2.SaveAs("raser/cflm/output/pixelArea/pixel_currentMax.pdf")
    print(nCount)

if __name__ == '__main__':
    main()