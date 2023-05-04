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

## Charge

## Irradiation and Trapping time


