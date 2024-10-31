import json
import ROOT
ROOT.gROOT.SetBatch(True)

def main():

    geant4_json = "./raser/cflm/cflm.json"
    with open(geant4_json) as f:
         g4_dic = json.load(f)

    data_X, data_Y, data_Z, particle_list = [], [], [], []
    NoParticle = 0

    X_low = g4_dic['object']['binary_compounds']['position_x'] - 10
    X_up = g4_dic['object']['binary_compounds']['position_x'] + 10
    X_bin = 20

    Y_low = -g4_dic['object']['binary_compounds']['side_x']/2    ## because of rotation
    Y_up = g4_dic['object']['binary_compounds']['side_x']/2
    Y_bin = g4_dic['object']['binary_compounds']['side_x']

    Z_low = 0
    Z_up = g4_dic['object']['binary_compounds']['side_z']
    Z_bin = g4_dic['object']['binary_compounds']['side_z']

    with open(f"raser/cflm/output/{PosBaseName}", 'r') as file:
         for line in file:
             columns = line.split()  
             data_X.append(float(columns[1])) #  X position : 1  // Z position :2 // Y position : 3  #//
             data_Y.append(float(columns[3]))
             data_Z.append(float(columns[2]))
             particle_list.append(columns[0])
             NoParticle += 1 

    hx = FillHist("hx", "X position distribution", X_bin, X_low, X_up, data_X)
    hy = FillHist("hy", "Y position distribution", Y_bin, Y_low, Y_up, data_Y)
    hz = FillHist("hz", "Z position distribution", Z_bin, Z_low, Z_up, data_Z)

    c1 = ROOT.TCanvas("c1", "X position distribution", 800, 600)
    c2 = ROOT.TCanvas("c2", "Y position distribution", 800, 600)
    c3 = ROOT.TCanvas("c3", "Z position distribution", 800, 600)

    c1.cd()
    hx.Draw()
    c1.SaveAs(f"{g4_dic['PosBaseName'].split('.')[0]}_X_position_distribution.png")

    c2.cd()
    hy.Draw()
    c2.SaveAs(f"{g4_dic['PosBaseName'].split('.')[0]}_Y_position_distribution.png")

    c3.cd()
    hz.Draw()
    c3.SaveAs(f"{g4_dic['PosBaseName'].split('.')[0]}_Z_position_distribution.png")

def FillHist(hx, title, nbins, low, up, data):
   
    h = ROOT.TH1F(hx, title,nbins, low, up)
    for value in data:
        h.Fill(value)
    h.GetXaxis().SetTitle(f"{title}(mm)")   #//
    h.GetYaxis().SetTitle("Event/{:.3f}".format((up - low) / nbins)) 

    return h
