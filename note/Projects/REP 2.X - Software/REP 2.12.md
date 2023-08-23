---
REP: 2.12
Title: telescope 
Author: 周嘉奇
Status: 
Type: Software
Created: 2023-04-05
---


# TELESCOPE

[[周嘉奇]]

---
## Overview
- 仿真
    -  [x] 构建简易的Geant4模型
        -  [x] 三个Si片，都设定成灵敏探测器，设定粒子源，发射粒子
        -  [x] 读出简易的探测器响应，即粒子在探测器内部的能量沉积和位置信息
    -  [x] 计算位置分辨
        -  [x] 计算两侧Si片某一维度击中信息的平均值，与中心Si片的这一维度的击中信息比较得出一维位置分辨
        -  [x] 将位置分辨计算细化到三维
    -  [x] 升级三个Si片
        -  [x] 中心升级成Si Strip
        -  [x] 两侧借鉴Si Pin升级成Pixel
    -  [x] 径迹重建
    -  [ ] 模拟探测器读出入射粒子产生的电流信号，从而判断粒子的信息
        -  [ ] 电荷载流子在探测器上的初始沉积
        -  [ ] 载流子的传播
        -  [ ] 电流信号的读出
---
## Introduction 
---
## Current progress
---
- 模拟了1.1.1的图并了解其结构
- 学习了python和geant4，了解了raser的架构
- 初始代码
    - 画出120Gev的π+介子经过七片si材料的板的geant4的图![fig.png|360](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/QQ%E5%9B%BE%E7%89%8720230619102829.png)
    - 输出粒子和次级粒子每一个step的位置信息和能量沉积![位置.png|600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BD%8D%E7%BD%AE.png) 
- 改进代码
    - 具体是建立三个Si片，都设定成灵敏探测器，这样可以只输出粒子在探测器内部的信息，优化了输出；优化了可视化图形的颜色![vis.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/vis.png)
    - 设定粒子源并发射粒子，读出简易的探测器响应，即粒子在探测器内部的能量沉积和位置信息![output.png|1150](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/output.png)
- 位置分辨
    通过计算m1,m2中的击中信息的平均值，与si strip的击中信息比较得出位置分辨 (需要通过升级探测器来改进)![位置分辨(粗糙).png|1200](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BD%8D%E7%BD%AE%E5%88%86%E8%BE%A8.png)
- 升级Si片
    - 将三个Si片改进成5×5的小Si片，以此来改进位置分辨的算法![三视图.png|1100](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/QQ%E5%9B%BE%E7%89%8720230619104344.png)
- 位置分辨的改进
    击中信息不再采用Geant4理论计算的结果，而是通过判断粒子击中的si片，输出si片的中心位置，加上si片半宽的误差来输出击中信息![|450](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/5%C3%975.png)![|1000](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BA%8C%E7%BB%B4%E4%BD%8D%E7%BD%AE%E5%88%86%E8%BE%A8.png)
- 径迹重建
    根据除DUT外所有探测器的击中位置信息，用最小二乘法拟合这些三维空间数据点来得出拟合直线，计算出直线在DUT的位置信息，与DUT的击中信息比较进一步得出位置分辨
    直线方程采用的形式：x = k1 * z + b1；y = k2 * z + b2，具体可见一篇最小二乘法的参考文献：https://www.doc88.com/p-8189740853644.html（文献公式有误，2应该替换为n，n为三维空间数据点的个数）![|800](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E9%87%8D%E5%BB%BA.png)
---





