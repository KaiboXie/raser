#!/usr/bin/env python3

import sys
import os

import numpy
import ROOT
ROOT.gROOT.SetBatch(True)

from util.output import output

def read_file(file_path,file_name):
    with open(file_path + '/' + file_name) as f:
        lines = f.readlines()
        time,volt = [],[]

        for line in lines:
            time.append(float(line.split()[0])*1e9)
            volt.append(float(line.split()[1])*1e3)

    time = numpy.array(time,dtype='float64')
    volt = numpy.array(volt,dtype='float64')

    return time,volt

def main(elec_name, file_path, key=None):
    if key is None:
        key = ''
    fig_name = os.path.join(file_path, elec_name+key+'.pdf')
    time,volt = [],[]

    time,volt = read_file(file_path, elec_name+key+'.raw')
    length = len(time)
    t_min, t_max = time[0], time[-1]

    ROOT.gROOT.SetBatch()    
    c = ROOT.TCanvas('c','c',700,600)
    c.SetMargin(0.2,0.1,0.2,0.1)
    f1 = ROOT.TGraph(length,time,volt)
    f1.SetTitle(' ')

    f1.SetLineColor(2)
    f1.SetLineWidth(2)

    f1.GetXaxis().SetTitle('Time [ns]')
    f1.GetXaxis().SetLimits(t_min, t_max)
    f1.GetXaxis().CenterTitle()
    f1.GetXaxis().SetTitleSize(0.08)
    f1.GetXaxis().SetLabelSize(0.08)
    f1.GetXaxis().SetNdivisions(5)
    f1.GetXaxis().SetTitleOffset(1)

    f1.GetYaxis().SetTitle('Voltage [mV]')
    f1.GetYaxis().CenterTitle()
    f1.GetYaxis().SetTitleSize(0.08)
    f1.GetYaxis().SetLabelSize(0.08)
    f1.GetYaxis().SetNdivisions(5)
    f1.GetYaxis().SetTitleOffset(1)

    c.cd()
    f1.Draw('AL')
    c.SaveAs(fig_name)

if __name__ == '__main__':
    import sys
    main(sys.argv[1], sys.argv[2])
    
