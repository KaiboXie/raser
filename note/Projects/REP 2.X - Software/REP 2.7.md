---
REP: 2.7
Title: Irradiation damage in SiC 
Author: 符晨曦
Status: 
Type:  
Created: 2023-04-11
---


# Irradiation damage in SiC 


[[符晨曦]]


## Introduction 

第〇步 在devsim中复现未辐照碳化硅器件的CV与电场
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/nju_pin_reverse_cv.png)

第一步 在devsim中获取辐照后碳化硅器件的CV与电场

目前进度

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/1D_HPK_PIN_irradiation_reverse_c%5E-2v.png)

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/1D_HPK_PIN_irradiation_reverse_electricfield.png)

第二步 将电场信息导入raser主程序，同步缺陷俘获率导致的trapping time改变

第三步 基于电场与trapping time，模拟辐照后器件的电荷收集、时间分辨等信息

## Defect

缺陷对象：具有能级与俘获截面、被辐照剂量和产率所确定的对象，载流子在其上的概率由对应的俘获率/释放率决定。
被俘获的载流子会改变电场。

尚不清楚SiC器件中有哪些缺陷及它们应该符合的模型。

尝试复现Si中的HPTM模型。

## Trapping time

在器件层面考虑辐照损伤，一般考虑碰撞产生的载流子：
1、漂移规律不同，因为电场被俘获载流子改变了；
2、载流子有概率被俘获导致信号丢失。