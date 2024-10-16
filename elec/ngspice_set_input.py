import os
from array import array

import ROOT
ROOT.gROOT.SetBatch(True)

from util.output import output

def set_input(det_name, key=None):
    current=[]
    time=[]
    if key == None:
        key = ""
    path = "output/current/{}".format(det_name)
    myFile = ROOT.TFile(os.path.join(path, "sim-current"+str(key))+".root")

    myt = myFile.tree
    for entry in myt:
       current.append(entry.current0) # current[i], i for electrode number
       time.append(entry.time)
    input_c=[]
    if abs(min(current))>max(current): #set input signal
        c_max=min(current)
        for i in range(0, len(current)):
            if current[i] < c_max * 0.01:
                input_c.append(str(0))
                input_c.append(str(0))
                input_c.append(str(time[i]))
                input_c.append(str(0))
                break
            else:
                current[i]=0
        for j in range(i, len(current)):
            input_c.append(str(time[j]))
            input_c.append(str(current[j]))
            if current[j] > c_max * 0.01:
                break
        input_c.append(str(time[j]))
        input_c.append(str(0))
        input_c.append(str(time[len(time)-1]))
        input_c.append(str(0))
        for k in range(j, len(current)):
            current[i]=0
    else:
        c_max=max(current)
        for i in range(0, len(current)):
            current[i]=0
            if current[i] > c_max * 0.01:
                input_c.append(str(0))
                input_c.append(str(0))
                input_c.append(str(time[i]))
                input_c.append(str(0))
                break
        for j in range(i, len(current)):
            input_c.append(str(time[j]))
            input_c.append(str(current[j]))
            if current[j] < c_max * 0.01:
                break
        input_c.append(str(time[j]))
        input_c.append(str(0))
        input_c.append(str(time[len(time)-1]))
        input_c.append(str(0))
        for k in range(j, len(current)):
            current[i]=0
    in_put=array("d",[0.])
    t=array("d",[0.])
    out_path = output(__file__, det_name)
    fout = ROOT.TFile(os.path.join(out_path, "input"+str(key))+".root", "RECREATE")
    t_out = ROOT.TTree("tree", "signal")
    t_out.Branch("time", t, "time/D")
    t_out.Branch("current", in_put, "current/D")
    n_bin = myt.GetEntries()
    for m in range(n_bin):
        in_put[0]=current[m]
        t[0]=time[m]
        t_out.Fill()
    t_out.Write()
    fout.Close()
    return input_c
