---
REP: 2.8
Title: Top-TCT simulation on SiC
Author: 石航瑞, 解凯博
Status: Active
Type: Software
Created: 2023-04-11
Updated: 2023-05-04
---


# Top-TCT simulation on SiC 

[[石航瑞]], [[解凯博]]

## Introduction 

## Carriers

## NGspice
经过 TCT_T1.py 得到 SiC 在激光照射后输出的电流信号 current:e+h ，根据 current:e+h 在描述 T1 电路的文件 paras/T1.cir 的基础上改写输入电流源得到新的可供 ngspice 执行的文件 output/T1_tmp.cir ，执行 output/T1_tmp.cir 即可得到 T1 输出的电压关于时间的数据并保存至 output/t1.raw 供后续使用ROOT画图
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/500V.jpg)

## Waveform 
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

## Charge
目前的电荷收集效率比对结果为![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_top_tct_exp_and_sim_compare4_cce.png)

## Irradiation and Trapping time


