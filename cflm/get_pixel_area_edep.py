import ROOT

def main():

    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)

    i_j_label, edep = [], []
    
    file = ROOT.TFile('raser/cflm/output/pixelArea/dividedAreaEdep.root')
    tree = file.Get("DetectorID")

    for m in range(tree.GetEntries()):
       tree.GetEntry(m)
       i_tmp = tree.i
       j_tmp = tree.j
       i_j_label.append([i_tmp, j_tmp])
       edep.append(tree.Edep)
    
    file.Close()
   
    h1 = ROOT.TH2F("hist", "Heatmap", 40, 0, 40, 10, -5, 5)
    for n in range(len(i_j_label)):
            h1.Fill(i_j_label[n][1], i_j_label[n][0], edep[n])
    c1 = ROOT.TCanvas("canvas", "Heatmap", 1600, 800)
    h1.GetYaxis().SetTitle("Detector_ID_Y")
    h1.GetXaxis().SetTitle("Detector_ID_Z")
    h1.Draw("colz") 
    c1.SaveAs("raser/cflm/output/pixelArea/singleEdep.pdf")

if __name__ == "__main__":
    main()