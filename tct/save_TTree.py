import os
from array import array

import ROOT
ROOT.gROOT.SetBatch(True)

from util.output import create_path

def save_signal_TTree(my_d,key,ele_current,my_f):
    if "planar3D" in my_d.det_model or "planarRing" in my_d.det_model:
        path = os.path.join("output", "pintct", my_d.det_name, "data",)
    elif "lgad3D" in my_d.det_model:
        path = os.path.join("output", "lgadtct", my_d.det_name, "data",)
    create_path(path) 
    for j in range(ele_current.read_ele_num):
        volt = array('d', [999.])
        time = array('d', [999.])
        if ele_current.read_ele_num==1:
            fout = ROOT.TFile(os.path.join(path, "sim-TCT") + str(key) + ".root", "RECREATE")
        else:
            fout = ROOT.TFile(os.path.join(path, "sim-TCT") + str(key)+"No_"+str(j)+".root", "RECREATE")
        t_out = ROOT.TTree("tree", "signal")
        t_out.Branch("volt", volt, "volt/D")
        t_out.Branch("time", time, "time/D")
        for i in range(ele_current.CSA_ele[j].GetNbinsX()):
            time[0]=i*ele_current.time_unit
            volt[0]=ele_current.CSA_ele[j][i]
            t_out.Fill()
        t_out.Write()
        fout.Close()
