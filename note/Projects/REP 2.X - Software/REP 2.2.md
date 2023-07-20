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




