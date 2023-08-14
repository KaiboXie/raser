---
REP: 2.2
Title: 3D 4H-SiC Timing simulation 
Author: 谭雨航
Status: implemented
Type: Software
Created: 2021-10-01
Updated: 2023-04-25
---

# 3D 4H-SiC Timing simulation

[[谭雨航]]

Implemented as: ./run 1.1.5 


### 2023-07 DEVSIM解二维电场计划
参考nju_pin_5mm_2Dmesh.py及杨涛博士的Node.py、DriftDiffusion.py、Physics.py、Initial.py等，完善devsim_solve.py 或新写devsim_solve_2D.py
1. 实现基本框架（Material、Doping、Meshing、Solver）
2. 调整或增加物理边界条件、初始解等
3. 与FEniCS结果对比（与 2. 循环迭代）

### 2023-07-24
-  [x] 实现DEVSIM解2D电场的流程，并求解C-V     [[赵森]]
-  [x] 实现DEVSIM解2D PN结的事例，熟悉二维DEVSIM的实现流程     [[石航瑞]]
-  [x] 完善调用DEVSIM电场结果的接口     [[李星臣]]


### 2023-08-14
-  [x] 加密网格，得到符合物理的电场图   [[赵森]]、[[符晨曦]]、[[李星臣]]、[[石航瑞]]
[ 增加PN结/PIN的电场图]
[增加用二维DEVSIM解出的在x轴方向上的电场曲线图]
[增加PIN的航瑞的一维电场曲线图]
-  [x] 在PN结例程基础上，得到CV曲线图，跑通程序框架   [[赵森]]
[增加pn结cv曲线]
本周计划：
-  [ ] 在PN结例程基础上修改为Sicar1器件，求解其二维电场分布
- 





