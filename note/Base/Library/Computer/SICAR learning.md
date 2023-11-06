简单说一下pyroot绘制折线图：
--
import  导入库
- 导入数据：
g_1 = ROOT.TGraph("./SRH.csv","%lf,%lf")函数名 = 折线图绘制（"文件名"，"放参数1，放参数2")
设置
- 曲线设置：
g_1.SetNameTitle("")设置绘制曲线标题
g_1.SetLineWidth(2)设置线宽
g_1.SetLineColor(ROOT.kGray+3)设置线条颜色
g_1.SetMarkerColor(ROOT.kGray+3)设置标记颜色
g_1.SetMarkerStyle(21)设置标记风格(21以后是实心的，1-20有的是空心的，有的是花的)
g_1.SetMarkerSize(1)设置标记尺寸
- 坐标轴设置：
g_1.GetXaxis().SetRangeUser(-5,805)X轴范围
g_1.GetXaxis().SetTitle("Reverse Bias Voltage [V]")X轴中心标题
g_1.GetXaxis().CenterTitle()X轴小标题
g_1.GetXaxis().SetTitleOffset(1.4)设置标题偏移
g_1.GetXaxis().SetTitleSize(0.05)小标题尺寸
g_1.GetXaxis().SetLabelSize(0.05)标记尺寸
g_1.GetXaxis().SetNdivisions(505)
Y轴同理
设置1条曲线即可，其他的可以用("SAME")
- 设置画布：
c = ROOT.TCanvas("c","c",500,500)设置画布c
c.SetLeftMargin(0.22)左间距
c.SetBottomMargin(0.16)底部间距
- 设置图例
legend = ROOT.TLegend(0.25+0.3,0.2,0.6+0.27,0.5) 图例尺寸
legend.SetTextSize(0.03)    图例文本尺寸
legend.AddEntry(g_1,"EH_{ 6/7}- N_{ t} = 0 cm^{-3}")   图例名.添加图例项目（曲线名，"希望起的名字"）
上下标符合Markdone语言，可自行搜索
- 绘制
c.cd()绘制画布
c.SetLogy()
g_1.Draw()绘制曲线，("双引号中间可以加入参数")
legend.Draw("SAME")绘制图例（"和上文一样"）
c.SaveAs("./EH67-Nt.pdf")保存为pdf文件。
- 基本内容这些，其他内容可以从[[ROOT]]官网手册查询