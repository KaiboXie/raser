---
REP: 1.2
Title: SICAR1 Fabrication
Author: 张希媛,王聪聪,何野,王科琪
Status: Active
Todo: 测试小器件IV和CV（王科琪 何野）
Type: Hardware 
Created: 2022-10-01
Updated: 2023-06-19
---


- [ ] SICAR1.1 Timing Results📅 2023-11-20
	- [ ] Get ready for the timing measurement 📅 2023-11-09


# SICAR1 Fabrication（第一次）

[[张希媛]], [[王聪聪]]


## Overview 

- SICAR1 Run1 （已完成）
   - [ ] 测试IV和CV，分析数据[[何野]]
   - [ ] 分析和整理欧姆接触电阻率，可以重新测试，测量小器件的IV和CV[[王科琪]]
   - [ ] 分析完IV和CV后7月初完成划片准备测试电荷收集和时间分辨[[何野]] 
   - [ ] 测试和整理电荷收集，俘获时间等参数，撰写论文 [[[[何野]]]]（8月29日之前完成）
   - [ ] 测试时间分辨[[[[王科琪]]]]（8月29日之前完成）
- SICAR1 Run2  （已完成）
   - 钝化层厚度=500nm，流片工艺进行了优化。
   - 8月18日完成N电极制作，并进行退火（7月29日之前完成）[[王科琪]]
   - 8月31日前完成第二次流片 [[王科琪]]
   - 9月10日前完成欧姆接触电阻率测试 [[王科琪]]
   - 测试完欧姆接触电阻率后进行划片，测试单个器件的IV、CV等电学特性。[[何野]] [[王科琪]]
   - 用源和激光测试电荷收集、时间分辨等。
   - 环形电极SICAR激光测试完以后，进行石墨烯转移，测试电学性能、电荷收集。
- SICAR1 Run3  （11月）
   - 测量SICAR1 Run1时间分辨。
   - 根据电荷收集效率和时间分辨测试条件确定第三版光刻版图形大小。
   - 设计第三版光刻版。
- Open Tasks 
  - 减小漏电流设计（保护环设计等查找论文）
-  [x] Presentation
	-  [ ]   The 42nd RD50 Workshop 

## 第一次流片1mm器件 IV和CV测试
[[何野]] [[王科琪]]



--- 
### 第一次流片5mm×5mm器件 IV和CV测试
[[何野]]， [[解凯博]]
#### 不同尺寸器件的IV测试、取数、作图
- 测试环境
	- B106探针台
	- 电源：Keithley 2470 source meter
	- sensor正面接地，背面加高压
	- 扫描设置：电流限制105$\mu A$，间隔5s
	- 反向偏压范围(0,250V)，步长1V
	- 正向偏压范围(0,50V)，步长20mV
---
- IV性能的仿真
![SICAR1-IV](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605101520.png)
---
- SICAR1-1-1 
	- 尺寸: 5000$\mu m$ × 5000$\mu m$
	- 版图：![bantu1-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103752.png)
	- 图片：![SICAR1-1-1|400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605095855.png)
	- 反向偏压：![SICAR1-1-1R](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605101712.png)
	- 正向偏压：![SICAR1-1-1F](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605101834.png)
	- 器件导通，反向偏压下漏电流大致符合预期
- SICAR1-2-2
	- 尺寸: 1000$\mu m$ × 1000$\mu m$
	- 版图：![bantu1-2-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103838.png)
	- 图片：![SICAR1-2-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605102733.png)
	- 反向偏压：![SICAR1-2-2R](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605102855.png)
	- 正向偏压：![SICAR1-2-2F](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605102928.png)
	- 器件导通，反向偏压下漏电流低于预期
- SICAR1-3-8
	- 尺寸：1000$\mu m$ × 1000$\mu m$
	- 版图：![bantu1-3-8](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103950.png)
	- 图片：![SICAR1-3-8](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103536.png)
	- 反向偏压：![SICAR1-3-8R](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103604.png)
	- 正向偏压：![SICAR1-3-8](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605103631.png)
	- 器件导通，反向偏压下漏电流低于预期
- SICAR1-4-1-1
	- 尺寸：1000$\mu m$ × 1000$\mu m$
	- 版图：![bantu1-4-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605104755.png)
	- 图片：![SICAR1-4-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605104748.png)
	- 反向偏压：![SICAR1-4-1-1R](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605104841.png)
	- 正向偏压：![SICAR1-4-1-1F](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605104921.png)
	- 器件导通，反向偏压下漏电流低于预期
- SICAR1-5-1-2
	- 尺寸：1000$\mu m$ × 1000$\mu m$
	- 版图：![bantu1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605104948.png)
	- 图片：![SICAR1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605105012.png)
	- 反向偏压：![SICAR1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605105115.png)
	- 正向偏压：![SICAR1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605105141.png)
	- 器件导通，反向偏压下漏电流低于预期
- 五个器件的反向漏电流密度：![density](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605110734.png)
	- 大尺寸器件（SICAR1-1-1）的漏电流较高
	- 小尺寸器件的IV曲线比较相似，且漏电流水平较低
---
#### 不同尺寸器件的CV测试、取数、作图
- 测试环境
	- B002探针台
	- 电源：Keithley 2410 source meter
	- LCR：Keysight E4980A
	- sensor正面接地，背面加高压
	- 扫描设置：电流限制100$\mu A$，反向偏压范围(0,200V)，间隔5s
---
- CV性能的仿真
 ![CV](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605111400.png)
- $V_{GL}$：130V
- $V_{FD}$：400V
---
- SICAR1-1-1
	- CV曲线：![CV1-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112000.png)
	- 1/$C^{2}$ -V曲线：![C2V1-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112039.png)
	- $V_{GL}$：75V
	- $V_{FD}$：≈140V
- SICAR1-2-2
	- CV曲线：![CV1-2-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112113.png)
	- 1/$C^{2}$ -V曲线：![C2V1-2-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112233.png)
	- $V_{GL}$：65V
	- $V_{FD}$：≈200V
- SICAR1-3-8
	- CV曲线：![CV1-3-8](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112317.png)
	- 1/$C^{2}$ -V曲线：![C2V1-3-8](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112342.png)
	- $V_{GL}$：81V
	- $V_{FD}$：＞200V
- SICAR1-4-1-1
	- CV曲线：![CV1-4-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112430.png)
	- 1/$C^{2}$ -V曲线：![C2V1-4-1-1](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112452.png)
	- $V_{GL}$：83V
	- $V_{FD}$：＞200V
- SICAR1-5-1-2
	- CV曲线：![CV1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112604.png)
	- 1/$C^{2}$ -V曲线：![C2V1-5-1-2](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605112531.png)
	- $V_{GL}$：77V
	- $V_{FD}$：＞200V
- 可以看出以上器件都有$V_{GL}$与$V_{FD}$（是LGAD），但是与设计的预期差别较大
---
- 5mm器件的IV、CV （new）
	- IV
		- 反向![RD50_IV_R.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RD50_IV_R.png)
		- 正向![RD50_IV_F.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RD50_IV_F.png)
	- CV
		- ![RD50_CV.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RD50_CV.png)
		- 1/$C^{2}$-V![RD50_C2V.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RD50_C2V.png)
	- 耗尽区宽度：![depth_compare.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/depth_compare.png)




---
- 5mm器件的IV、CV （old）
	- IV
		- 反向![5mmIVR](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091132.png)
		- 正向![5mmIVF](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091243.png)
	- CV
		- ![5mmCV](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091344.png)
		- 1/$C^{2}$-V![5mmC2V](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091418.png)
		- 耗尽区深度![depth](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091506.png)
		- 掺杂浓度![doping](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612091617.png)
		- 耗尽电压![Vfd](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230612092429.png)
---
### 第一次欧姆接触测试
[[何野]]
### 直径1000μm SICAR的IV\CV测试
[[王科琪]]
测试器件选择：
第一次流片中第一片的SICAR1-8-6
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/5c2d8368c6024dc582418bb0bf0b9ce.jpg)
- IV测试环境
	- B106探针台
	- 电源：Keithley 2470 source meter
	- sensor正面加高压（负），背面接地
	- 扫描设置：电流限制105$\mu A$，间隔1s
	- 反向偏压范围(0,600V)，步长1V
	- 数据位置：/scratchfs/bes/wangkeqi/wangkeqi/SICAR1.1.8
	- 创建新的位置：/publicfs/atlas/atlasnew/silicondet/itk/raser/wangkeqi/sicar1.1.8
	- 转换.csv成.root：
  > raser root sicar1.1.8

Saved as
> /publicfs/atlas/atlasnew/silicondet/itk/raser/wangkeqi/sicar1.1.8/sicar1.1.8.root

   
-  将.root数据文件画出可视化图片
    > raser draw sicar1.1.8

Saved as
> /afs/ihep.ac.cn/users/w/wangkeqi/raser/output/fig

![sicar1.1.8-1_iv.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1.1.8-1_iv.png)

![sicar1.1.8_iv.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1.1.8_iv.png)

- CV测试环境
	- B002探针台
	- 电源：Keithley 2410 source meter
	- LCR：Keysight E4980A
	- sensor正面加高压（负），背面接地
	- 扫描设置：电流限制100$\mu A$，间隔5s
	- 反向偏压范围(0,400V)，步长1V
    
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/f55366b43ce7ae38d63964c9401c6d1.png)

    ![sicar1.1.8_cv.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1.1.8_cv.png)

# Log 
1、欧姆接触电阻率测试（最优欧姆接触）**何野测试，科琪分析**

- [ ] P电极金属Ni/Ti/Al=60/30/80nm，不同退火温度800℃、950℃、1050℃（最高温度）欧姆接触电阻率。
     ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/compare.png)
- [ ] 相同退火温度（1050℃）不同金属的欧姆接触电阻率（Ni/Ti/Al=60/30/80nm，Ni/Ti/Al=60/20/100nm，Ni/Ti/Al=50/15/80nm）

2、温度对Sicar1电学性能影响研究（工作电压、暗电流、电阻率结电容等）

- [ ] 不同尺寸器件和相同尺寸不同金属条件IV测试（以便优化器件尺寸）**何野测试分析**

- [ ] 正反向IV趋势判断器件好坏（工作电压）

- [ ] 反向IV暗电流测试（避光测试IV，反向电流与电压公式关系判断暗电流，分析不同器件暗电流规律，重点）

3、CV测试 **何野测试分析**

- [ ] 电阻率、面积、工作电压和结电容的关系

- [ ]  求势垒高度和有效掺杂浓度、时间分辨和开启电压。

注释：何野（根据**Radiation hardness characterization of low gain avalanche** **detector prototypes for the high granularity timing detector**论文得到IV-CV测量研究的一些数据）

4、电荷收集和时间分辨研究

- [ ] 电荷收集和时间分辨测试（何野+谢凯博测试）




# SICAR1 Fabrication(第二次)

[[张希媛]], [[王聪聪]]

## 芯片制作
### 光刻版1.0设计（M1、M2、M3、M4）
[[王科琪]]
- 整体效果：
    ![photolithography.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography.png)
- M1
    ![M1.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/7014bb4b7ac4846c4677685ea976e33.png)
- M2
    ![M2.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/24d01f4c8216f032963ad5bf83012c0.png)
- M3
    ![M3.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/74c68ea12c0d1f5b3ad4f171863d8e7.png)
- M4钝化层
    ![M4.png |400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3e5f112e22f4965936333807e059b48.png)

### sicar1第二次流片工艺
[[何野]] , [[解凯博]]

# Schedule 
| 时间 | 1号晶圆 | 2号晶圆 |
| : - : | : - : | : - : | 
| 2023-04-03 | | | 光刻显影P电极（M2）| 光刻显影P电极（M2）|
| 2023-04-04 | | | 电子束蒸发 金属剥离 | 电子束蒸发 金属剥离 |
| 2023-04-06 | 淀积N电极、退火 | 淀积N电极、退火 | 淀积N电极、退火 | 淀积N电极、退火 |
| 2023-04-07 | PECVD淀积钝化层 | PECVD淀积钝化层 | PECVD淀积钝化层 | PECVD淀积钝化层 |
# Log 

