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
-  [ ] 仿真
    -  [x] 构建简易的Geant4模型
        -  [x] 三个Si片，都设定成灵敏探测器，设定粒子源，发射粒子
        -  [x] 读出简易的探测器响应，即粒子在探测器内部的能量沉积和位置信息
    -  [x] 计算位置分辨
        -  [x] 计算两侧Si片某一维度击中信息的平均值，与中心Si片的这一维度的击中信息比较得出一维位置分辨
        -  [x] 将位置分辨计算细化到三维
    -  [ ] 升级三个Si片
        -  [ ] 中心升级成Si Strip
        -  [ ] 两侧借鉴Si Pin升级成Pixel
    -  [ ] 径迹重建，优化算法
---
## Introduction 

---
## Current Tasks
基于Geant4 画出某能量的某种单粒子经过两块telescope的图。（如NIMA 901(2018)164-172 中的图6）
 
---
## Current progress
---
- 模拟了1.1.1的图并了解其结构
- 学习了python和geant4，了解了raser的架构
- 初始代码
    - 画出120Gev的π+介子经过七片si材料的板的geant4的图![fig.png|600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/fig.png)
    - 输出粒子和次级粒子每一个step的位置信息和能量沉积![位置.png|800](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BD%8D%E7%BD%AE.png) 
- 改进代码
    - 具体是建立三个Si片，都设定成灵敏探测器，这样可以只输出粒子在探测器内部的信息，优化了输出；优化了可视化图形的颜色![vis.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/vis.png)
    - 设定粒子源并发射粒子，读出简易的探测器响应，即粒子在探测器内部的能量沉积和位置信息![output.png|1150](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/output.png)
- 位置分辨
    - 通过计算m1,m2中的击中信息的平均值，与si strip的击中信息比较得出位置分辨 (需要通过升级探测器来改进)![位置分辨(粗糙).png|1200](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BD%8D%E7%BD%AE%E5%88%86%E8%BE%A8.png)
---





