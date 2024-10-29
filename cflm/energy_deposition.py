import ROOT
import json

def main():

    up = 70
    low = 0
    nbins = 70

    geant4_json = "./setting/absorber/cflm.json"
    with open(geant4_json) as f:
         g4_dic = json.load(f)

    file = ROOT.TFile(f"raser/cflm/output/{g4_dic['EdepBaseName']}")
    tree = file.Get("cflm")
    branch = tree.GetBranch("Edetector")

    data = []

    for event in tree:
        value = branch.GetLeaf("Edetector").GetValue()
        data.append(value)

    histogram = ROOT.TH1F("histogram", "Histogram of Energy deposition", nbins, low, up)

    histogram.SetXTitle("Energy deposition(MeV)")
    histogram.SetYTitle("Events/{:.3f}".format((up - low) / nbins))

    for value in data:
        histogram.Fill(value)

    c = ROOT.TCanvas("c", "c", 800, 600)

    histogram.Draw()
    c.SaveAs(f"raser/cflm/output/{g4_dic['EdepBaseName'].split('.')[0]}.png")

