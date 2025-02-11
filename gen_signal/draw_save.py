#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Description: Draw and plot drift path and induced current       
@Date       : 2021/08/31 11:09:40
@Author     : tanyuhang
@version    : 1.0
'''
from array import array
import time

import ROOT
ROOT.gROOT.SetBatch(True)

from util.output import output

TIME_BIN_WIDTH = 50e-12 # need to be consistent with the bin width in CalCurrent

def energy_deposition(my_g4v):
    """
    @description:
        Energy_deposition for multi events of Geant4 simulation
    @param:
        None     
    @Returns:
        None
    @Modify:
        2021/08/31
    """
    c1=ROOT.TCanvas("c1","canvas1",1000,1000)
    h1 = ROOT.TH1F("Edep_device", "Energy deposition in SiC", 100, 0., 0.1)
    for i in range (len(my_g4v.edep_devices)):
        h1.Fill(my_g4v.edep_devices[i])
    g1 = ROOT.TF1("m1","landau",0,0.1)
    h1.Fit(g1,"S")
    print("MPV:%s"%g1.GetParameter(1))
    h1.Draw()
    now = time.strftime("%Y_%m%d_%H%M")
    c1.SaveAs("output/particle/dep_SiC"+"_"+now+"_energy.pdf")
    c1.SaveAs("output/particle/dep_SiC"+"_"+now+"_energy.root")

def draw_scat_angle(evnets_angle,angle,model):
    """Draw scatting angle of events"""
    c1=ROOT.TCanvas("c1","canvas1",1000,1000)
    c1.Divide(1,2)
    c1.cd(1)
    n=len(evnets_angle)
    ROOT.gStyle.SetOptStat(0)
    h1 = ROOT.TH1F("event angle", "Source Angle = "+str(angle), n, 0., n)
    for i in range(n):
        if evnets_angle[i] != None:
            h1.SetBinContent(i,evnets_angle[i])
    h1.GetXaxis().SetTitle(" Event number ")
    h1.GetYaxis().SetTitle(" Scattering Angle ")
    h1.GetXaxis().CenterTitle()
    h1.GetYaxis().CenterTitle() 
    h1.SetLineWidth(2)
    h1.SetLineColor(2)
    h1.Draw("HIST")
    c1.cd(2)
    events = [ evnets_angle[i] for i in range(n) if evnets_angle[i] != None ]
    h2 = ROOT.TH1F("angle distribution", "Source Angle = "+str(angle), 
                   100, 0., max(events))
    for i in range(n):
        if evnets_angle[i] != None:
            h2.Fill(evnets_angle[i])
    h2.GetXaxis().SetTitle(" Scattering Angle ")
    h2.GetYaxis().SetTitle(" number ")
    h2.GetXaxis().CenterTitle()
    h2.GetYaxis().CenterTitle() 
    h2.SetLineWidth(2)
    h2.SetLineColor(2)
    h2.Draw("HIST")    
    c1.SaveAs("scat_angle"+model+".pdf")

def draw_drift_path(my_d,my_g4p,my_f,my_current,path):
    ROOT.gStyle.SetOptStat(0)
    # # ROOT.gROOT.SetBatch(1)
    c1 = ROOT.TCanvas("c", "canvas1", 200, 10, 1500, 2000)
    c1.Divide(1,2)

    if "plugin3D" in my_d.det_model:
        n_bin=[int((my_f.sx_r-my_f.sx_l)/5),
                int((my_f.sy_r-my_f.sy_l)/5),int((my_d.l_z)/10)]
        structure = ROOT.TH3D("","",n_bin[0],my_f.sx_l,my_f.sx_r,
                                    n_bin[1],my_f.sy_l,my_f.sy_r,
                                    n_bin[2],0,my_d.l_z)
    elif "planar3D" in my_d.det_model or "lgad3D" in my_d.det_model or "planarRing" in my_d.det_model:
        n_bin=[int(my_d.l_x/50),int(my_d.l_y/50),int(my_d.l_z)]
        structure = ROOT.TH3D("","",n_bin[0],0,my_d.l_x,
                                    n_bin[1],0,my_d.l_y,
                                    n_bin[2],0,my_d.l_z)
    c1.cd(1)
    ROOT.gPad.SetMargin(0.15, 0.1, 0.1, 0.1)
    for k in range(n_bin[2]):
        for j in range (n_bin[1]):
            for i in range(n_bin[0]):
                if "plugin3D" in my_d.det_model:
                    x_v = (i+1)*((my_f.sx_r-my_f.sx_l)/n_bin[0])+my_f.sx_l
                    y_v = (j+1)*((my_f.sx_r-my_f.sx_l)/n_bin[1])+my_f.sx_l
                    z_v = (k+1)*(my_d.l_z/n_bin[2])
                elif "planar3D" in my_d.det_model or "lgad3D" in my_d.det_model or "planarRing"in my_d.det_model:
                    x_v = (i+1)*(my_d.l_x/n_bin[0])
                    y_v = (j+1)*(my_d.l_y/n_bin[1])
                    z_v = (k+1)*(my_d.l_z/n_bin[2])
                try:
                    x_value,y_value,z_value = my_f.get_e_field(x_v,y_v,z_v)
                    if x_value==0 and y_value==0 and z_value ==0:
                        structure.SetBinContent(i+1,j+1,k+1,1)
                    else:                       
                        structure.SetBinContent(i+1,j+1,k+1,0)
                except RuntimeError:
                    structure.SetBinContent(i+1,j+1,k+1,1)
    structure.SetFillColor(1)
    structure.GetXaxis().SetTitle("x axis [\mum]")
    structure.GetYaxis().SetTitle("y axis [\mum]")
    structure.GetZaxis().SetTitle("z axis [\mum]")
    structure.GetXaxis().CenterTitle()
    structure.GetYaxis().CenterTitle() 
    structure.GetZaxis().CenterTitle() 
    structure.GetXaxis().SetTitleOffset(1.2)
    structure.GetYaxis().SetTitleOffset(1.4)
    structure.GetZaxis().SetTitleOffset(1.0)
    structure.GetXaxis().SetLabelSize(0.08)
    structure.GetYaxis().SetLabelSize(0.08)
    structure.GetZaxis().SetLabelSize(0.08)
    structure.GetXaxis().SetTitleSize(0.08)
    structure.GetYaxis().SetTitleSize(0.08)
    structure.GetZaxis().SetTitleSize(0.08)
    structure.GetYaxis().SetNdivisions(5)
    structure.GetZaxis().SetNdivisions(5)
    structure.Draw("ISO")
    c1.Update()

    mg = ROOT.TMultiGraph("mg","") # graph for page 2
    x_array=array('f')
    y_array=array('f')
    z_array=array('f')
    for hole in my_current.holes:
        n=len(hole.path)
        if(n>0):
            x_array.extend([step[0] for step in hole.path])
            y_array.extend([step[1] for step in hole.path]) 
            z_array.extend([step[2] for step in hole.path])              
            gr_p = ROOT.TPolyLine3D(n,x_array,y_array,z_array)
            gr_p.SetLineColor(2)
            gr_p.SetLineStyle(1)
            gr_p.Draw("SAME")
            gr_2D_p=ROOT.TGraph(n,x_array,z_array)
            gr_2D_p.SetMarkerColor(2)
            gr_2D_p.SetLineColor(2)
            gr_2D_p.SetLineStyle(1)
            mg.Add(gr_2D_p)
            del x_array[:]
            del y_array[:]
            del z_array[:]
    for electron in my_current.electrons:
        m=len(electron.path)
        if(m>0):
            x_array.extend([step[0] for step in electron.path])
            y_array.extend([step[1] for step in electron.path])
            z_array.extend([step[2] for step in electron.path])                
            gr_n = ROOT.TPolyLine3D(m,x_array,y_array,z_array)
            gr_n.SetLineColor(4)
            gr_n.SetLineStyle(1)
            gr_n.Draw("SAME")
            gr_2D_n=ROOT.TGraph(m,x_array,z_array)
            gr_2D_n.SetMarkerColor(4)
            gr_2D_n.SetLineColor(4)
            gr_2D_n.SetLineStyle(1)
            mg.Add(gr_2D_n)
            del x_array[:]
            del y_array[:]
            del z_array[:]
    particle_track = my_g4p.p_steps_current[my_g4p.selected_batch_number]
    n = len(particle_track)
    if(n>0):
        x_array.extend([step[0] for step in particle_track])
        y_array.extend([step[1] for step in particle_track])
        z_array.extend([step[2] for step in particle_track])
        gr = ROOT.TPolyLine3D(n,x_array,y_array,z_array)
        gr.SetLineColor(1)
        gr.SetLineStyle(1)
        gr.SetLineWidth(4)
        gr.Draw("SAME")
        gr_2D=ROOT.TGraph(n,x_array,z_array)
        gr_2D.SetMarkerColor(1)
        gr_2D.SetLineColor(1)
        gr_2D.SetLineStyle(1)
        gr_2D.SetLineWidth(4)
        mg.Add(gr_2D)
        del x_array[:]
        del y_array[:]
        del z_array[:]
    c1.cd(2)
    ROOT.gPad.SetMargin(0.15, 0.1, 0.2, 0.1)
    mg.GetXaxis().SetTitle("x axis [\mum]")
    mg.GetYaxis().SetTitle("z axis [\mum]")
    mg.GetXaxis().CenterTitle()
    mg.GetYaxis().CenterTitle() 
    mg.GetXaxis().SetTitleOffset(1.2)
    mg.GetYaxis().SetTitleOffset(0.8)
    mg.GetXaxis().SetLabelSize(0.08)
    mg.GetYaxis().SetLabelSize(0.08)
    mg.GetXaxis().SetTitleSize(0.08)
    mg.GetYaxis().SetTitleSize(0.08)
    mg.GetYaxis().SetNdivisions(5)
    c1.Update()
    mg.Draw("APL")
    c1.SaveAs(path+'/'+my_d.det_model+"_drift_path.pdf")
    c1.SaveAs(path+'/'+my_d.det_model+"_drift_path.root")
    del c1

def draw_current(my_d, my_current, ele_current, read_ele_num, model, path, tag=""):
    """
    @description:
        Save current in root file
    @param:
        None     
    @Returns:
        None
    @Modify:
        2021/08/31
    """
    c=ROOT.TCanvas("c","canvas1",1600,1300)
    c.cd()
    c.Update()
    c.SetLeftMargin(0.25)
    c.SetTopMargin(0.12)
    c.SetRightMargin(0.15)
    c.SetBottomMargin(0.17)
    ROOT.gStyle.SetOptStat(ROOT.kFALSE)
    ROOT.gStyle.SetOptStat(0)

    #my_current.sum_cu.GetXaxis().SetTitleOffset(1.2)
    #my_current.sum_cu.GetXaxis().SetTitleSize(0.05)
    #my_current.sum_cu.GetXaxis().SetLabelSize(0.04)
    my_current.sum_cu[read_ele_num].GetXaxis().SetNdivisions(510)
    #my_current.sum_cu.GetYaxis().SetTitleOffset(1.1)
    #my_current.sum_cu.GetYaxis().SetTitleSize(0.05)
    #my_current.sum_cu.GetYaxis().SetLabelSize(0.04)
    my_current.sum_cu[read_ele_num].GetYaxis().SetNdivisions(505)
    #my_current.sum_cu.GetXaxis().CenterTitle()
    #my_current.sum_cu.GetYaxis().CenterTitle() 
    my_current.sum_cu[read_ele_num].GetXaxis().SetTitle("Time [s]")
    my_current.sum_cu[read_ele_num].GetYaxis().SetTitle("Current [A]")
    my_current.sum_cu[read_ele_num].GetXaxis().SetLabelSize(0.08)
    my_current.sum_cu[read_ele_num].GetXaxis().SetTitleSize(0.08)
    my_current.sum_cu[read_ele_num].GetYaxis().SetLabelSize(0.08)
    my_current.sum_cu[read_ele_num].GetYaxis().SetTitleSize(0.08)
    my_current.sum_cu[read_ele_num].GetYaxis().SetTitleOffset(1.2)
    my_current.sum_cu[read_ele_num].SetTitle("")
    my_current.sum_cu[read_ele_num].SetNdivisions(5)
    my_current.sum_cu[read_ele_num].Draw("HIST")
    my_current.positive_cu[read_ele_num].Draw("SAME HIST")
    my_current.negative_cu[read_ele_num].Draw("SAME HIST")
    my_current.gain_positive_cu[read_ele_num].Draw("SAME HIST")
    my_current.gain_negative_cu[read_ele_num].Draw("SAME HIST")
    my_current.sum_cu[read_ele_num].Draw("SAME HIST")

    my_current.positive_cu[read_ele_num].SetLineColor(877)#kViolet-3
    my_current.negative_cu[read_ele_num].SetLineColor(600)#kBlue
    my_current.gain_positive_cu[read_ele_num].SetLineColor(617)#kMagneta+1
    my_current.gain_negative_cu[read_ele_num].SetLineColor(867)#kAzure+7
    my_current.sum_cu[read_ele_num].SetLineColor(418)#kGreen+2

    my_current.positive_cu[read_ele_num].SetLineWidth(2)
    my_current.negative_cu[read_ele_num].SetLineWidth(2)
    my_current.gain_positive_cu[read_ele_num].SetLineWidth(2)
    my_current.gain_negative_cu[read_ele_num].SetLineWidth(2)
    my_current.sum_cu[read_ele_num].SetLineWidth(2)
    c.Update()

    if abs(ele_current[read_ele_num].GetMinimum()) > abs(ele_current[read_ele_num].GetMaximum()):
        rightmax = 1.1*ele_current[read_ele_num].GetMinimum()
    else:
        rightmax = 1.1*ele_current[read_ele_num].GetMaximum()

    if rightmax == 0.0:
        n_scale = 0.0
    elif abs(ele_current[read_ele_num].GetMinimum()) > abs(ele_current[read_ele_num].GetMaximum()):
        n_scale = ROOT.gPad.GetUymin() / rightmax
    else:
        n_scale = ROOT.gPad.GetUymax() / rightmax
    
    ele_current[read_ele_num].Scale(n_scale)
    ele_current[read_ele_num].Draw("SAME HIST")
    ele_current[read_ele_num].SetLineWidth(2)   
    ele_current[read_ele_num].SetLineColor(8)
    ele_current[read_ele_num].SetLineColor(2)
    c.Update()

    axis = ROOT.TGaxis(ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin(), 
                       ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(), 
                       min(0,rightmax), max(0,rightmax), 510, "+L")
    axis.SetLineColor(2)
    axis.SetTextColor(2)
    axis.SetTextSize(0.02)
    axis.SetTextFont(40)
    axis.SetLabelColor(2)
    axis.SetLabelSize(0.035)
    axis.SetLabelFont(42)
    axis.SetTitle("Ampl [V]")
    axis.SetTitleFont(40)
    axis.SetTitleOffset(1.2)
    #axis.CenterTitle()
    axis.Draw("SAME HIST") 

    legend = ROOT.TLegend(0.5, 0.2, 0.8, 0.5)
    legend.AddEntry(my_current.negative_cu[read_ele_num], "electron", "l")
    legend.AddEntry(my_current.positive_cu[read_ele_num], "hole", "l")
    legend.AddEntry(my_current.gain_negative_cu[read_ele_num], "gain electron", "l")
    legend.AddEntry(my_current.gain_positive_cu[read_ele_num], "gain hole", "l")
    legend.AddEntry(my_current.sum_cu[read_ele_num], "e+h", "l")
    #legend.AddEntry(ele_current, "electronics", "l")
    legend.SetBorderSize(0)
    # legend.SetTextFont(43)
    legend.SetTextSize(0.08)
    legend.Draw("same")
    c.Update()
    c.SaveAs(path+'/'+model+my_d.det_model+tag+"No_"+str(read_ele_num+1)+"electrode"+"_basic_infor.pdf")
    c.SaveAs(path+'/'+model+my_d.det_model+tag+"No_"+str(read_ele_num+1)+"electrode"+"_basic_infor.root")
    del c

def cce(my_current, path):
    charge=array('d')
    x=array('d')
    for i in range(my_current.read_ele_num):
        x.append(i+1)
        sum_charge=0
        for j in range(my_current.n_bin):
            sum_charge=sum_charge+my_current.sum_cu[i].GetBinContent(j)*my_current.t_bin
        charge.append(sum_charge/1.6e-19)
    print("===========RASER info================\nCollected Charge is {} e\n==============Result==============".format(list(charge)))
    n=int(len(charge))
    c1=ROOT.TCanvas("c1","canvas1",1000,1000)
    cce=ROOT.TGraph(n,x,charge)
    cce.SetMarkerStyle(3)
    cce.Draw()
    cce.SetTitle("Charge Collection Efficiency")
    cce.GetXaxis().SetTitle("elenumber")
    cce.GetYaxis().SetTitle("charge[Coulomb]")
    c1.SaveAs(path+"/cce.pdf")
    c1.SaveAs(path+"/cce.root")

def save_signal_time_resolution(my_d,batch_number,sum_cu,ele_current,my_g4p,start_n):
    """ Save induced current after amplification"""

    output_path = output(__file__, my_d.det_name, 'batch')
    for k in range(ele_current.read_ele_num):
        charge = sum_cu[k].Integral()*TIME_BIN_WIDTH
        charge_str = "_charge=%.2f_"%(charge*1e15)  #fc
        e_dep = "dep=%.5f_"%(my_g4p.edep_devices[batch_number-start_n]) #mv
        output_file = output_path + "/t_" +str(batch_number)+charge_str+e_dep+"events.csv"

        f1 = open(output_file,"w")
        f1.write("time [ns], Amplitude [mV] \n")
        for i in range(ele_current.amplified_current[k].GetNbinsX()):
            f1.write("%s,%s \n"%(i*ele_current.amplified_current[k].GetBinWidth(0),
                                    ele_current.amplified_current[k][i]))
        f1.close()

        print("output_file:%s"%output_file)

    del ele_current
