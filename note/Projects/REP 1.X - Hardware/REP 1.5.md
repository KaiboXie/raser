---
REP: 1.5
Title: T1 fabrication
Author: 何野 解凯博
Status: Active
Type: Hardware 
Created: 2022-10-01
Updated: 2023-05-04
---

# 正在进行的工作
-  [x] 使用alibava替代T1做NJU-SiC-PIN的β测试
	-  [x] 制作可以供NJU-SiC-PIN使用的Detector Board（已完成制作，厂商已快递发出）
	-  [ ] 制作固定Daughter Board和Detector Board的底板（已完成设计，待加工）

# T1 inventory
|Number|Status|Location|Movement|
|---|---|---|---|
|1|未辐照的5mm SiC PIN|B107|-|
|2|3.9E13质子辐照的5mm SiC PIN|B107|-|
|3|2.4E14质子辐照的5mm SiC PIN|B107|-|
|4|7.8E14质子辐照的5mm SiC PIN|B107|-|




# T1 fabrication

[[何野]]

- [ ] T1第一版的设计、生产
	设计：基于UCSC的读出电路，更改了图中R1的值和电路的形状（正方形→T型）
	目的：应用于散裂中子源的质子束流上，传感器选用NJU的5mm×5mm的SiC PIN
	
	原理图
![UCSC_simulation_circuit.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSC_simulation_circuit.png)

	布线
![layout.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/layout.png)

目前T1第一版已经生产完成
	实物图
![T1_v1.0.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_v1.0.jpg)

LTspice仿真结果：
	输入信号：10μA的脉冲电流
	![input.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230206143912.png)
	输出信号：
	![output.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230206143644.png)
	

- [ ] T1第一版的测试
	- [ ] 355nm激光
		未辐照5mm的SiC PIN测试结果：
		测试环境：
		使用355nm激光 top扫描探测器中心位置 电路板直接连接示波器读出
		![laser_TCT.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/laser_TCT.jpg)


		100V时波形：
		![0_100V.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/100V.png)
		分布：
		![100.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/100.png)
		
		测试结果：对于355nm激光，能正常工作
	- [ ] β源
		- [ ] 测试环境：三号厅，Sr90β源，电路板连接20dB主放进行读出
			
			测试结果：在电压加到500V时，放置β源后，T型板不能看到β源的信号
			需要排查T型板不能看到β信号的原因，并解决问题
			
			- [ ] T型板噪声信号的采集
			是否由于噪声过大导致观测不到信号
			![T1noise.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1noise.png)
			- [ ] 快速的信号发生器在T型板上产生的信号（计划进行）
			模拟一个快速的信号观测电路的响应

[[解凯博]]

## 现存问题：
- [ ] T1在β测试中无信号

---

## 可能的原因：
- [ ] 信噪比低
	- [ ] 加工工艺
	- [ ] 布线设计
- [ ] 抗干扰能力差
- [ ] sensor在激光照射后有损伤
- [ ] 电路板本身存在问题（硬件损坏）（存疑）
- [ ] 电路板对高频信号的处理能力弱
- [ ] β源活性太低

---

## 实验结果
### 1、电路空载测试（无信号输入）
#### T1和UCSC不接主放直接连接示波器噪声对比
T1：
![T1不接主放.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/T1%E4%B8%8D%E6%8E%A5%E4%B8%BB%E6%94%BE.png)
UCSC：
![UCSC不接主放.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/UCSC%E4%B8%8D%E6%8E%A5%E4%B8%BB%E6%94%BE.png)
刻度：1mV/div      100ns/div
==空载时的T1的噪声略高于UCSC==
### T1和UCSC通过主放后噪声对比
T1：
![T1接主放.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/T1%E6%8E%A5%E4%B8%BB%E6%94%BE.png)
UCSC：
![UCSC接主放.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/UCSC%E6%8E%A5%E4%B8%BB%E6%94%BE.png)
刻度：9mV/div      2.5ns/div
==主放会放大噪声==

UCSC不接主放通电前后噪声无法观察到任何变化
由此可以认为
==UCSC不会引入新的噪声==
T1的噪声略高于UCSC
==T1电路会引入新的噪声==

### T1与UCSC均受手机信号干扰
![手机干扰.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/%E6%89%8B%E6%9C%BA%E5%B9%B2%E6%89%B0.png)
将手机放在电路附近时非常容易观测到

#### 实验结论
T1在空载状态下就会引入新的噪声，UCSC则不会

### 后续计划
-  [ ] 重复T1β测试
	-  [ ] 对未辐照SiC-PIN的T1板进行β测试，取得信号波形数据
	-  [ ] 与杨涛论文中使用UCSC得到的数据对比
-  [ ] 取得厂家T1出厂测试的测试方法及数据
-  [ ] 让厂家设计并制作新的电路板测试是否可以看到β信号
       （尽可能不干涉厂家的设计）
	-  [ ] 在UCSC的布线基础上只将板改为T形并将sensor的焊盘连同周围滤波电容移至T的末端
-  [ ] 使用合适的快速的信号发生器在T型板上产生信号模拟μ子穿过SiC产生的信号观察T1的输出信号

### 疑问：
- [ ] 厂家测试得到的T1的噪声较大的结论在没有UCSC作为对比的情况下时如何得到的，标准是什么
