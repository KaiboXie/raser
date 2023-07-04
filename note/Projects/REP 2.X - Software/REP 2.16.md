---
REP: 2.16
Title: TAICHU3 Beam Test Simulation
Author: 胡一鸣
Status: Active
Type: Hardware 
Created: 2023-06-09
Updated: 2023-06-27
---

# TAICHU3 Beam Test Simulation 
[[胡一鸣]]
TAICHU3是多层硅像素顶点径迹探测器，目前已经完成了两次TestBeam, 对芯片/原型的分辨率都已经有了较为全面的实验结果
- [ ] 2022/12第一次Telescope主要是为了测量芯片层面的分辨率等特性，选用了几块芯片垂直摆放测量其分辨率
- [ ] 2023/04第二次则将芯片按原型摆放，得到的数据更加接近实际情况
- [ ] 两次实验均重点研究了响应阈值对分辨率的影响，该部分可能能在仿真模拟中做些内容
(TAICHU3原型)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/taichu3_PROTOTYPE.PNG)
(TAICHU3第二次测试分辨率vs阈值)
![resolution.PNG](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/resolution.PNG)
- [ ] 分辨率预期
	芯片像素的尺寸为 25um* 25um，对应的径迹分辨率应当是$$25um/\sqrt[2]{12} \approx 7um$$
	不过由于charge sharing 导致一个hit可能有多个像素有信号，实际的分辨率理应比7um更好

- [ ] Charge sharing与Clustersize
	- [ ] Charge sharing：
		Charge sharing, quite simply, is the sharing of charges among capacitors.
		对于硅像素探测器而言，即一次粒子入射，有多个像素电子学信号超过阈值。
		Charge sharing并不一定是件坏事，实际上它还能提高我们的精度，（不是绝对的）
	- [ ] Clustersize
		Charge sharing会导致多个像素有信号，在我们实验数据中，以1-2像素为主，绝大部分情况限制在4像素以内。我们将由一个hit产生的像素着火数量称为clustersize
		有时一个时钟内可能会有多个粒子击中芯片，每个hit有各自的cluster, 极少数情况下这些cluster难以区分，但大部分情况下不是这种情况
该图为单个芯片每个事件像素着火数量，近似等于clustersize（单电子入射），有更好的图片以后找到了再上传
![clustersize.PNG](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/clustersize.PNG)
下面我做了个简单的示意图，展示为什么会以1-4 clustersize为主![cluster_from.PNG](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/cluster_from.PNG)

---
- [ ]  参考allpix2
- [ ] 布局像素仿真代码架构
	- [ ] 建立一套可以复用的，OOP的架构
	- [ ] 目前想法：
		- [ ] Pixel为父类，根据未来可能出现的具体设计子类Pixel，比如我要的是TAICHU3
		- [ ] Pixel类最主要的构造部分应当是 Geometry和Dopping， 使用json和setting模块作为输入参数，同时要留有给Geant4以及DEVISM的接口作为几何/边界条件。（或许DEVISM是直接通过setting来联系的不需要和这个模块有交互？）




