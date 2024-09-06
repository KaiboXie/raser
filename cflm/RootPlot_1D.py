import ROOT

data = []
with open('./xxx_100_sic.txt', 'r') as file:
    for line in file:
        columns = line.split()  
        data.append(float(columns[2])) #  X position : 1  // Z position :2 // Y position : 3  #//

h = ROOT.TH1F("histogram", "Z position Distribution", 70, 0, 70)  #//

for value in data:
    h.Fill(value)

h.GetXaxis().SetTitle("Z position (mm)")   #//
h.GetYaxis().SetTitle("Events/bin")

c = ROOT.TCanvas("canvas", "Canvas Title", 800, 600)
h.Draw()

c.SaveAs("RootPlot100sic_Z.png")  #//


c.Draw()
