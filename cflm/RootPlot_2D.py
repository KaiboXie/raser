import  ROOT
from array import array

X_position = []
Z_position = []
colors = []
column = []

def RootPlot_2D():
    c1 = ROOT.TCanvas("c1", "Hit position distribution", 200, 10, 700, 500)
    mg = ROOT.TMultiGraph()
    gr1 = ROOT.TGraph()
    gr2 = ROOT.TGraph()
    gr3 = ROOT.TGraph()
    gr4 = ROOT.TGraph()

    with open('raser/cflm/xxx_200_air.txt', 'r') as file:
        for line in file:
            columns = line.split()
            column.append(columns[0])  
            X_position.append(float(columns[1])) 
            Z_position.append(float(columns[2]))
            if columns[0] == 'gamma':
                colors.append(ROOT.kGreen)
            elif columns[0] == 'e-':
                colors.append(ROOT.kRed)
            elif columns[0] == 'e+':
                colors.append(ROOT.kBlue)
            else:
                colors.append(ROOT.kBlack)

    for i in range(len(X_position)):
        particle = column[i]
        if particle == 'gamma':
            gr1.SetMarkerStyle(20)
            gr1.SetMarkerColor(ROOT.kBlack)
            gr1.SetPoint(i, X_position[i], Z_position[i])
        elif particle == 'e-':
            gr2.SetMarkerStyle(22)
            gr2.SetMarkerColor(ROOT.kBlack)
            gr2.SetPoint(i, X_position[i], Z_position[i])
        elif particle == 'e+':
            gr3.SetMarkerStyle(24)
            gr3.SetMarkerColor(ROOT.kBlack)
            gr3.SetPoint(i, X_position[i], Z_position[i])
        else:
            gr4.SetMarkerStyle(28)
            gr4.SetMarkerColor(ROOT.kBlack)
            gr4.SetPoint(i, X_position[i], Z_position[i])

    mg.Add(gr1)
    mg.Add(gr2)
    mg.Add(gr3)
    mg.Add(gr4)

    mg.GetXaxis().SetTitle("X position (mm)")
    mg.GetYaxis().SetTitle("Z position (mm)")

    mg.Draw("AP")

    legend = ROOT.TLegend(0.7, 0.2, 0.9, 0.4)
    legend.AddEntry(gr1, "#gamma", "p").SetMarkerColor(ROOT.kGreen)
    legend.AddEntry(gr2, "e^{-}", "p").SetMarkerColor(ROOT.kRed)
    legend.AddEntry(gr3, "e^{+}", "p").SetMarkerColor(ROOT.kBlue)
    legend.AddEntry(gr4, "Other", "p").SetMarkerColor(ROOT.kBlack)

    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetTextSize(0.03)

    legend.Draw()


    c1.SaveAs("RootPlot100air_2D.png")