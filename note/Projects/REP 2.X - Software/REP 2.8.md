---
REP: 2.8
Title: Top-TCT simulation on SiC
Author: 石航瑞, 解凯博
Status: Active
Type: Software
Created: 2023-04-11
Updated: 2023-06-13
Team Report: 2023-06-05
---


# Top-TCT simulation on SiC 

[[石航瑞]], [[解凯博]]
## NGspice
经过 TCT_T1.py 得到 SiC 在激光照射后输出的电流信号 current:e+h ，根据 current:e+h 在描述 T1 电路的文件 paras/T1.cir 的基础上改写输入电流源得到新的可供 ngspice 执行的文件 output/T1_tmp.cir ，执行 output/T1_tmp.cir 即可得到 T1 输出的电压关于时间的数据并保存至 output/t1.raw 供后续使用ROOT画图
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/500V.jpg)

## Irradiation
### Latest
$\Phi = 0$
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_trappingtime_0_result.png)

$\Phi = 3.9e13$
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_trappingtime_3.9e13_result.png)

$\Phi = 7.8e14$
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_trappingtime_7.8e14_result.png)

各点辐照和trapping time 值（横轴辐照采用对数坐标）：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230530_shhr_trappingtime_irradiation_logimage.png)
trapping time 和irradiation的对数成线性关系![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230521_shhr_trappingtime01.png)

## Waveform 
### Latest
#### 下降沿
下降沿模拟和实验相差较大，推测是由于线缆分布电容产生的。下图为添加了1mF后的模拟、实验对照，可以看出在添加了电容后在下降沿处会出现明显的负电压情况。
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230815_top_tct_add_capacitance_compare.png)

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_trappingtime_0_result.png)

### 最新NGspice模拟结果和实验对比
以500V为基准调整激光单脉冲能量为1.215e-11J，使得实验和模拟结果符合良好![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_500V.png)
- 将各电压点实验模拟比对结果展示如下
	- 100V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_100V.png)
	- 200V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_200V.png)
	- 300V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_300V.png)
	- 400V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_400V.png)
	- 500V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_500V.png)
	- 600V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_600V.png)
	- 700V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_700V.png)
	- 800V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_800V.png)
	- 900V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_900V.png)
	- 1000V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_1000V.png)
	- 可以看到在全耗尽（电压大于500V）的情况下，实验模拟结果符合非常好。

### 测量激光单脉冲能量
拟购买Thorlabs：S120VC激光功率探头
| 价格 | 波长范围 | 误差 | 量程 | 355nm 响应 | 1065nm响应 |
| --- | --- | ---|  ---| --- | --- |
| ￥4225.32 | 200-1100nm | 355-5%, 1064-7% | 50nW-50mW | 16.28mA/W | 17.44mA/W |

我们的激光器10Hz，单脉冲在70uJ左右，功率在100uW-700uW之间

PM101: 
https://www.thorlabschina.cn/thorproduct.cfm?partnumber=PM101
Operation manual: 
https://www.thorlabschina.cn/drawings/4d1ac5f6ea8b7605-9CAA2977-9D35-C9D1-3D7B9ECD730FAF1D/PM101-Manual(English).pdf
Software: 
https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=OPM
Operation manual: 
https://www.thorlabs.com/software/MUC/OPM/v5.0/TL_OPM_V5.0_web-secured.pdf

## 理论计算

### 理论估算激光产生信号强度
激光公式$$I_0=I(0, 0, 0)\frac{\omega_0}{\omega (z)}exp{\frac{-2r^2}{\omega^2(z)}}\cdot exp{\frac{-4t^2ln2}{\tau^2}}$$$$I'=I_0\cdot e^{-\alpha z}$$两边对$z$求导可推得：$$dI=-\alpha z\cdot I$$
载流子产生：
$$dN_{e-h pair}dVdt=\alpha dz \frac{I\cdot dS\cdot dt}{h\nu}$$
由Shockley-Ramos：$$I_q(t)=q\vec{v_q}(t)\cdot exp(-\frac{t}{\tau _{eff,e,h}})\cdot \nabla U_\omega(\vec{x_q}(t))$$可得：
$$I_q(t)dt=q\vec{v_q}\nabla U_\omega \cdot exp(-\frac{t}{\tau _{eff,e,h}})\cdot dt= q dU_\omega exp(-\frac{t}{\tau _{eff,e,h}})\cdot(\vec{x_q}(t))$$ 所以：$$\vec{I}_(t_1, t_2) (t_1-t_2)=\Sigma_q\Sigma_t I_q(t)\cdot dt$$
在估计的计算中，计算top-TCT时，可以忽略激光的直径，只考虑时间展宽，将激光简化为z方向和时间两个维度来简化计算，可以得到$$I=I(0, 0, 0)\cdot exp(\frac{-4t^2}{\tau ^2}) \cdot exp(-\alpha z)$$其中$\alpha = 2.1m^{-1},  \tau = 8.1\times 10^{-9}s$
对于载流子产生过程，由于忽略了直径，其化为：$$dN_{e-h}dzdt=\alpha dz\frac{I\cdot dz dt}{h\nu}$$对于S-R定理而言，$q=N_{e-h}\cdot e$，加权场为一维z方向场
根据程序解电场结果，$E(z)\approx 1e7-1e11\cdot z$    (SI)
假定电子漂移受电场作用：$F=Eq$, v=ue
在z处的载流子密度为：$$N(z)=\int \frac{I}{E}\cdot e\cdot dz=\int E_I\cdot exp(\frac{-4(t-\sqrt{\frac{z\cdot m_e}{E\cdot e}})^2}{\tau ^2}) \cdot exp(-\alpha z)\cdot dz$$产生的感应电流为：$$I(t)=\int N(z)e\cdot v\cdot U\cdot dz$$
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230807_top_tct_laser_enengy.png)
实验测得激光平均功率为$7.2\times 10^{-8}W$, 脉冲频率为10Hz, 即单脉冲能量为$7.2\times 10^{-9}J$
代入积分可得$I_{max}=0.016A$, 将该电流进行电子学处理可估计出信号理论峰值约为20V

>模拟中使用激光能量为$1.2\times 10^{-11}J$, 信号峰值强度约为$0.5V$

### 理论估计CCE
在工作电压下，电荷近似被全部收集。实验用355nm激光单光子能量为：$E=h\nu=3.49eV$, 碳化硅禁带宽度为3.2eV, 可认为一个光子激发一对载流子。那么激发载流子总数为：
$$N=\frac{E_{pulse}}{E}=1.29\times 10^{10}$$
其电荷收集为$Q=2.063nC$
实验上电荷收集由经过了放大器放大的电压信号积分而来, 对该理论值进行类似的电子学处理
$$Q'=Q*Gain/R=825.2nC$$式中Gain为放大器放大倍率，R为示波器电阻值。
实验上的电荷收集为20.57nC，二者相差约40倍


## Charge

电荷收集效率比对
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_cce_compare_result.png)
不同辐照下电荷收集
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_cce_result.png)
3.9e13
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_3.9e13_th1f_result.png)
iv：
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230612_shhr_rd50_iv_result.png)





# History

## irradiation

对于不同的辐照损伤，目前使用trapping time在程序中进行模拟。通过模拟结果与实验比对(辐照剂量分别为0, 3.9e13, 7.8e14 ; 模拟上采用的trapping time 分别为：8.9ns, 0.79ns, 0.06ns)
3.9e13:
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230521_shhr_trappingtime_compare_3.9e13.png)

7.8e14
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230521_shhr_trappingtime_compare_7.8e14.png)

## cce
电荷收集效率比对结果为![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_cce.png)
>采用NGspice处理后波形（波形输入）；更新时间：23.05.05

### 
- 原有BB电子学参数下的电荷收集效率![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230403_cce_shhr_01.png)
- 发现之前设置的激光入场时间和整体时间分辨存在问题，需要更改参数设置，预计更改完成后模拟波形与实验能符合更好。
>更新时间：23.04.03
## 之前的计算

在实验上：$I=60A$, $80A-69.86\mu J$
代入数据计算可得：$I(t)_{max}\approx50\mu A$,  $E=1e-11J$
								$I(t)_{max}\approx90A$， $E=60e-6J$
raser模拟结果：$I_{max}=150\mu A$
>此处计算结果为极板上的感应电流，并非实际产生的信号，需经过电子学处理，但由于raser模拟结果与实验相差不大，就将计算结果与raser程序中极板上感应电流（即e+h）进行比较
- 可以看出模拟结果在数量级上没有问题

### ngspice处理后波形（三角波输入）
- ngspice处理后100V-1000V各电压点波形与实验对照（输入为三角波）
	- 100V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_100.png)
	- 200V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_200.png)
	- 300V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_300.png)
	- 400V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_400.png)
	- 500V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_500.png)
	- 600V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_600.png)
	- 700V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_700.png)
	- 800V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_800.png)
	- 900V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_900.png)
	- 1000V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cut_1000.png)

### BB电子学调整

- 以500V下作为基准进行电子学参数调整![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_500v.png)
	所采用电子学参数为"BBGain" : 2.52, 
					 "BB_imp" : 80,

- 依据上述电子学给出100V-1000V的电荷收集效率以及各点波形对照图
	- CCE![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_cce_shhr_02.png)
	- 100V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_100v.png)
	- 200V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_200v.png)
	- 300V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_300v.png)
	- 400V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_400v.png)
	- 500V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_500v.png)
	- 600V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_600v.png)
	- 700V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_700v.png)
	- 800V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_800v.png)
	- 900V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_900v.png)
	- 1000V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230406_shhr_sim_exp_compare_1000v.png)

- ngspice100V-1000V各电压点波形对照以及电荷收集效率
	- CCE![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_cce.png)
	- 100V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_100v.png)
	- 200V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_200v.png)
	- 300V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_300v.png)
	- 400V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_400v.png)
	- 500V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_500v.png)
	- 600V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_600v.png)
	- 700V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_700v.png)
	- 800V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_800v.png)
	- 900V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_900v.png)
	- 1000V![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2304010_shhr_sim_exp_compare_ngspice_1000v.png)

### 0320
将激光时间展宽由原先350ps改为现在的10ns，电子学参数改为：
"BBW" : 0.66,
"BBGain" : 4.4,
"BB_imp" : 175
模拟与实验数据波形图如下所示：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/top_tct_sim_exp_compare_230327_result.png)
可以看出上升沿的符合程度相较于之前有了明显上升。

### 0313
调整程序中电子学参数后，模拟与实验数据图形比对如下图所示：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230318_top_tct_exp_and_sim_compare_result.png)
数据来源于何野最新采集的top-tct扫描数据，模拟的电子学参数为：
"BBW" : 0.66,
"BBGain" : 1.4,
"BB_imp" : 185

### 0206
- 调整后模拟与实验图形比对如下图所示：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230209_top_tct_exp_and_sim_compare_result.png)
- 其中使用的BB电子学参数为：
	- "CDet" : 30,
	  "BBW" : 0.66,
	  "BBGain" : 43,
	  "BB_imp" : 400,
	  "OscBW" : 20
- 由于BB电子学只能修改曲线的下降沿，所以图像上下降沿的比对较吻合，上升沿相差较大
