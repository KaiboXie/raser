---
REP: 0.17
Title: 碳化硅探测器与（BJT）集成提高sensor的电流输出
Author: 解凯博 王聪聪 史欣 
Status: Active
Type: Idea
Created: 2023-05-04
Updated: 2023-08-21
---
# SICAR1集成 

 [[王聪聪]] [[史欣]] [[解凯博]] [[黄英杰]] [[吴思语]]

## Overview 

- 查阅文献
   - [ ] 碳化硅的集成 [[解凯博]] [[黄英杰]]
   
   - [ ] 硅探测器的集成 [[吴思语]]
## Patents 
专利：碳化硅探测器与双极晶体管（BJT）集成芯片设计与应用
# 想法来源
[[2023-02-27-JC157]]
有团队在研究SiC的晶体管刻蚀

## 优势
- 将BJT与sensor刻蚀在同一块可以在放大信号的同时减少放大电路引入的噪声，提高信噪比
- 将BJT集成在sensor上可以实现更高的集成度，减小电路的尺寸和复杂度

## 4H-SiC基础BJT结构
- 使用比较多的有两种结构
- 第一种器件结构
![BJT1.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT1.png)
High Current Gain 4H-SiC NPN Bipolar Junction Transistors 2003 器件 电流增益55 有器件制备方法

![BJT2.png|618](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT2.png)
The Simulation Study of Gaussian-doped Base 4H-SiC Bipolar Junction Transistor 2009 仿真

- 第二种器件结构
![BJT3.png|858](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT3.png)
Fabrication and characterization of 4H SiC bipolar junction transistor with double base epilayer 2012 器件 有器件制备方法

![BJT4.png|582](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT4.png)
A High Current Gain 4H-SiC NPN Power Bipolar Junction Transistor 2003 器件 有器件制备方法

![BJT5.png|610](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT5.png)
A novel 4H-SiC lateral bipolar junction transistor structure with high voltage and high current gain 2013 仿真

![BJT6.png|546](https://raser-1314796952.cos.ap-beijing.myqcloud.com/BJT6.png)
Improved Current Gain in 4H-SiC BJTs Passivated with Deposited Oxides Followed by Nitridation 2011 器件 电流增益86