---
REP: 1.5
Title: T1 fabrication
Author: 何野 解凯博
Status: Active
Type: Hardware 
Created: 2022-10-01
Updated: 2023-08-10
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
	-  [x] 了解所用β源的特点
		-  [x] β射线从源中出来的位置与源上的标识是否一致
		-  [ ] β射线从源中出来后发散的程度有多大
	-  [x] 使用[[李辉]]已完成的alibava系统测试了解alibava系统
		-  [x] 对比自己实验得到的数据确认数据是否正常
		-  [x] 如何处理获得的数据
	-  [ ] 改进实验重复测试
		-  [x] 将β源放置在sensor背面保证大部分电子可以都穿过sensor
		-  [x] 更改闪烁体的摆放方式和位置，保证触发效率
		-  [x] 将闪烁体置于碳化硅前
	-  [ ] 制作用于FPGA产生的高频大信号的分压板，使信号分压后可用于T1问题的检测


## alibava实验结果
- ### test1
	- 1.5mm NJU-SiC-PIN * 6（未辐照）
	- 实验数据位置：服务器
		/afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230510
	- 未看到信号，触发速度慢
	- 闪烁体放置方式存在问题，应将电路板一面朝下放置

- ### test2
	- 5mm NJU-SiC-PIN * 1（未辐照）
	- 实验数据位置：服务器
		afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230512pm
	- 未看到信号，触发速度慢

- ### test3
	- 较test1、2进行了改进
	- 1.5mm NJU-SiC-PIN * 9（未辐照）
	- 实验数据位置：
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

- ### test4
	- 改变了碳化硅与闪烁体的位置关系，β先经过闪烁体后经过碳化硅
	 ![实验装置_20230717.bmp|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/%E5%AE%9E%E9%AA%8C%E8%A3%85%E7%BD%AE_20230717.bmp)
	- 1.5mm NJU-SiC-PIN * 6（未辐照）
	- 实验数据位置：服务器
		afs/ihep.ac.cn/users/x/xiekaibo/ALIBAVA/data/20230706pm
	- 实验过程中存在问题，实验结果不可靠，需要重复实验

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
![layout.png|775](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/layout.png)

目前T1第一版已经生产完成
	实物图
![T1_v1.0.jpg|575](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_v1.0.jpg)

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
---
### β源
发射的β粒子的能量：
The <sup>90</sup>Sr source emits β particles at 0.546 MeV from <sup>90</sup>Sr and at 2.280 MeV from   <sup>90</sup>Y
β源的活度：
三号厅，5cm×5cm 闪烁体，总测量时间为10分钟，表中结果为每分钟触发数）：
![β源活度2.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%CE%B2%E6%BA%90%E6%B4%BB%E5%BA%A62.png)
β源底部：
![bottom.jpg|450](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/bottom.jpg)
底部中央小孔的边长约为1.5mm~2.5mm

---
### T1板屏蔽罩测试
测试所用的屏蔽罩（导线从T1板test外壳引出，并与包裹着铜箔的屏蔽外壳相连后被接地导线的鳄鱼夹夹住）：
![屏蔽罩+接地2.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E8%94%BD%E7%BD%A9+%E6%8E%A5%E5%9C%B02.jpg)
测试结果（此时低压源已接地）：
未加屏蔽前（以标准差衡量噪声大小）：
![T1_noise_diyayuanjieditiao.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_diyayuanjieditiao.jpg)
加上屏蔽后：![T1_noise_zhaojieditiao.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_zhaojieditiao.jpg)
加上屏蔽罩后对噪声的减小没有影响

---
### 低压源对噪声的影响
低压源的output开启后会引入很大的噪声：
开启低压源前：
![开启低压源前.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%BC%80%E5%90%AF%E4%BD%8E%E5%8E%8B%E6%BA%90%E5%89%8D.jpg)
开启低压源后：
![开启低压源后.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%BC%80%E5%90%AF%E4%BD%8E%E5%8E%8B%E6%BA%90%E5%90%8E.jpg)

低压源接地测试（三号厅，T1板的输出噪声经过了主放的放大）：
低压源未接地：
![T1_noise_diyayuanweijiedi.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_diyayuanweijiedi.jpg)
低压源接地：
![T1_noise_diyayuanjieditiao.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_diyayuanjieditiao.jpg)
低压源接地后噪声标准差减小，虽然减小的极少

---
### T1整体噪声分析
三号厅，噪声由T1的输出口经主放放大后呈现在示波器上，以标准差衡量噪声大小
高压源+低压源同时接入到T1板上
![T1_noise_gaoyayuan.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_gaoyayuan.jpg)
若以最大值来衡量噪声
![噪声最大值.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%99%AA%E5%A3%B0%E6%9C%80%E5%A4%A7%E5%80%BC.jpg)
T1整体噪声FFT分析结果：
同时将高压源与低压源接入到T1板上，利用NumPy库进行噪声的FFT变换，选用的窗口为汉明窗![T1_noise_FFT.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_FFT.jpg)
在信号波形允许的情况下，或许可以通过增加滤波电路来滤去部分噪声

---
### T1噪声来源分析
T1仅接入低压源时的噪声：
![T1_noise_diyayuanjieditiao.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_noise_diyayuanjieditiao.jpg)
UCSC仅接入低压源时的噪声:
![UCSC_noise_diya.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSC_noise_diya.jpg)
若以三倍标准差作为噪声的最大值，则T1与UCSC噪声最大值之差=（6.68-3.37）×3=9.93mV，与以前将噪声最大值作为衡量噪声的标准所得的结果大致一致
以最大值衡量噪声时，UCSC与T1噪声对比：
![噪声最大值对比.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%99%AA%E5%A3%B0%E6%9C%80%E5%A4%A7%E5%80%BC%E5%AF%B9%E6%AF%94.jpg)
因此可以认为T1的噪声水平比UCSC大的原因是T1的低压部分产生了较多的噪声，具体原因尚不明确，或许是反馈电阻的更改使得噪声增加，具体原因需要后续通过实验验证。

## T1放大倍数研究
[[李再一]]
- 在α源测试中，分别使用T1和UCSC读出板收集同一个sensor的电荷收集
- 理论上两种读出板会收集到相同的电荷量
- 100V反向偏压，T1收集到155.8fC电荷，信号幅值276.7mV
![T1_100V_230814.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_100V_230814.png)
- UCSC收集到240.6fC电荷，信号幅值730.8mV
![UCSC_100V_230814.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSC_100V_230814.png)
- 考虑到T1和UCSC结构不同，α粒子在空气中能损较大，T1实验中有额外的8mm空气，能损接近1MeV，所以电荷收集的差异在合理范围内
- 结论：不能证明T1电荷放大倍数不足
---
- 假设T1和UCSC电荷放大倍数相同，比较波形幅度差异
- T1收集到169.4fC电荷时，波形幅值为317.4mV
![T1_450V_230814.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_450V_230814.png)
- UCSC收集到108.4fC电荷时，波形幅值为353.4mV
![PIN3_100V_230814.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/PIN3_100V_230814.png)
- UCSC收集到电荷量远小于T1时，波形幅值却大于T1
- 结论：相同电荷收集量，UCSC输出信号电压幅值大于T1
---
- T1读出板的电压放大倍数小于UCSC
- 可能是T1看不到β源信号的原因之一
- 反应在波形上：UCSC信号更“尖”，T1信号更“胖”
- UCSC 240.6fC波形
![UCSCwfm_230814.png|525](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSCwfm_230814.png)
- T1 155.8fC波形
![T1wfm_230814.png|525](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1wfm_230814.png)
- UCSC 108.4fC波形
![UCSC_PIN3_100V_230814.png|525](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSC_PIN3_100V_230814.png)
