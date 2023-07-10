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
## 像素探测器仿真
- [ ]  参考allpix2
	- [ ] 同样为探测器仿真软件，也使用已有的软件来完成部分功能，不过简化了接口使得用户更方便使用
- [ ] 布局像素仿真代码架构
	- [x] 目前想法：（废弃）
		- [x] Pixel为父类，根据未来可能出现的具体设计子类Pixel，比如我要的是TAICHU3
		- [x] Pixel类最主要的构造部分应当是 Geometry和Dopping， 使用json和setting模块作为输入参数，同时要留有给Geant4以及DEVISM的接口作为几何/边界条件。（或许DEVISM是直接通过setting来联系的不需要和这个模块有交互？）
	- [ ] 优先考虑在已有代码中增加一部分：
		- [ ] 在Particle类中增加输入参数判断项，来执行各自的探测器仿真，利于维护
		- [ ] 从利于维护的角度来说，在已有文件函数或类中增加一部分（使用if判断输入参数隔离环境）>增加一个类>增加一个文件
		- [ ] 在自己的部分中，如果存在不需要执行的判断句，弹出报错（raise）比直接pass更加利于维护
- [ ] RASER模块理解
	- [x] 示例：
		my_f = raser.FenicsCal(my_d,dset.fenics)            -> 载流子漂移模块，目前正在改用Devsim，该部分初始化了边界条件
		my_g4p = raser.Particles(my_d, my_f, dset)        -> 初始化Geant4, 并且生成了原初电离的粒子信息的文件
	        my_current = raser.CalCurrentG4P(my_d, my_f, my_g4p, 0)   ->尚未了解，应当是使用g4数据和载流子漂移方程生成文件
	        ele_current = raser.Amplifier(my_current, dset.amplifier)       ->尚未了解，应当是根据外部电路和上一步文件给出最终想要的数据
	- [x] Setting: 使用json文件作为输入，在该模块下整理为可以被后续模块使用的部分
	- [x] Geant4：提过简单的接口给用户，来运行G4
	- [ ] Devsim：比较关键的部分，处理载流子漂移，现在还未实现三维,[[DEVSIM操作手册]]
		- [ ] 理论部分：载流子漂移[[6 DEVSIM 介绍]]，以及
		- [ ] 代码部分：初始化中读取参数构造边界条件，并且提供电场电势函数供CalCurrent部分使用
	- [ ]  CalCurrent:
	- [ ] Amp:




