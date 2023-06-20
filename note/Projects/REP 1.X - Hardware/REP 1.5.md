---
REP: 1.5
Title: T1 fabrication
Author: 何野 解凯博
Status: Active
Type: Hardware 
Created: 2022-10-01
Updated: 2023-06-12
---

# 正在进行的工作
-  [x] 使用alibava替代T1做NJU-SiC-PIN的β测试
	-  [x] 制作可以供NJU-SiC-PIN使用的Detector Board
	-  [x] 制作固定Daughter Board和Detector Board的底板(3D打印)
	-  [x] 使用1.5 * 1.5 NJU-SiC-PIN进行β测试采集数据
	-  [x] 使用5 * 5 NJU-SiC-PIN进行β测试采集数据
	-  [ ] 使用金属底板替代塑料底板
	-  [ ] 验证实验测得的噪声是否与之前理论上预估的噪声大小相符
		-  [ ] 将β测试数据中的ADC转成电荷量，与理论上预计的噪声的电荷量大小对比
	-  [ ] 了解所用β源的特点
		-  [x] β射线从源中出来的位置与源上的标识是否一致
		-  [ ] β射线从源中出来后发散的程度有多大
	-  [x] 使用[[李辉]]已完成的alibava系统测试了解alibava系统
		-  [x] 对比自己实验得到的数据确认数据是否正常
		-  [x] 如何处理获得的数据
	-  [ ] 改进实验重复测试
		-  [x] 将β源放置在sensor背面保证大部分电子可以都穿过sensor
		-  [x] 更改闪烁体的摆放方式和位置，保证触发效率
	-  [ ] 制作用于FPGA产生的高频大信号的分压板，使信号分压后可用于T1问题的检测

## alibava实验
- ### test1
	- 1.5mm NJU-SiC-PIN * 6（未辐照）
	- 实验数据位置：服务器
		/afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230510
	- 未看到信号，触发速度慢

- ### test2
	- 5mm NJU-SiC-PIN * 1（未辐照）
	- 实验数据位置：服务器
		afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230512pm
	- 未看到信号，触发速度慢

- ### test3
	- 较test1、2进行了改进
	- 1.5mm NJU-SiC-PIN * 9（未辐照）
	- 实验数据位置：三号厅102电脑
		
	- 仍未看见信号，且触发速度仍非常慢

- ### test3补充实验
	- 目的：找出触发非常慢的原因
	- β源直接置于闪烁体上
		- 触发非常快
	- β源置于支架上，与闪烁体之间只隔有空气
		- 触发比较快
	- 在保证β源与闪烁体相对位置不变，将探测器板上粘有SiC的区域置于中间
		- 触发非常慢
	- test3看不到信号原因猜测：击中SiC的电子无法到达闪烁体触发，产生触发的都是没有经过SiC的电子

## 进度
- [ ] 使用alibava替代T1测试β信号
	-  [x] 使用公版的Detector Board实验（高压滤波做法简单）
		-  [x] 使用1.5mm * 1.5mm NJU-SiC-PIN 阵列
			- 实验数据位置：服务器
			/afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230510
			- 纯噪声
			![capture_20230529100058457.bmp](https://raser-1314796952.cos.ap-beijing.myqcloud.com/capture_20230529100058457.bmp)
			- 可能包含信号
			![capture_20230529100036139.bmp](https://raser-1314796952.cos.ap-beijing.myqcloud.com/capture_20230529100036139.bmp)
			- 未看到信号
		-  [x] 使用5mm * 5mm NJU-SiC-PIN 
			- 实验数据位置：服务器afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230512pm
			- 纯噪声
			![capture_20230529100256146.bmp](https://raser-1314796952.cos.ap-beijing.myqcloud.com/capture_20230529100256146.bmp)
			- 可能包含信号
			![capture_20230529100313584.bmp](https://raser-1314796952.cos.ap-beijing.myqcloud.com/capture_20230529100313584.bmp)
			- 未看到信号
	-  [ ] 使用新设计的Detector Board实验（使用UCSC的高压滤波电路）
		-  [ ] 使用1.5mm * 1.5mm NJU-SiC-PIN 
		-  [ ] 使用5mm * 5mm NJU-SiC-PIN 
- [ ] 找出T1出现问题的原因
	-  [ ] 取得厂家T1出厂测试的测试方法及数据
	-  [ ] 让厂家重新设计并制作新的电路板测试重复β测试
		-  [ ] 在UCSC的布线基础上只将板改为T形并将sensor的焊盘连同周围滤波电容移至T1的末端
	-  [ ] 在T1上用金属屏蔽后和UCSC比较
	-  [ ] 使用合适的快速的信号发生器在T型板上产生信号模拟μ子穿过SiC产生的信号观察T1的输出信号
		-  [ ] 使用FPGA加分压板替代信号发生器



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
- [x] β源活性太低

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
	-  [ ] 与[[杨涛]]论文中使用UCSC得到的数据对比
-  [ ] 取得厂家T1出厂测试的测试方法及数据
-  [ ] 让厂家设计并制作新的电路板测试是否可以看到β信号
       （尽可能不干涉厂家的设计）
	-  [ ] 在UCSC的布线基础上只将板改为T形并将sensor的焊盘连同周围滤波电容移至T的末端
-  [ ] 使用合适的快速的信号发生器在T型板上产生信号模拟μ子穿过SiC产生的信号观察T1的输出信号

### 疑问：
- [ ] 厂家测试得到的T1的噪声较大的结论在没有UCSC作为对比的情况下时如何得到的，标准是什么
