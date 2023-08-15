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
-  [x] 在PN结例程基础上，得到CV曲线图，跑通程序框架   [[赵森]]

本周计划：
-  [ ] 在PN结例程基础上修改为Sicar1器件，求解其二维电场分布

作者的pn结已经没有问题
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2%E7%BB%B4pn%E7%BB%93.png)

一维作者devsim手册中的结果：

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%BD%9C%E8%80%851%E7%BB%B4pn%E7%BB%93%E6%89%8B%E5%86%8C%E5%9B%BE.png)

证明：电场x方向上趋势相同，物理正确
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/pn%E7%BB%93%E7%89%A9%E7%90%86.png)

pn结对称分布的掺杂：
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2%E7%BB%B4pn%E7%94%B5%E5%9C%BA.png)

nju-pin的电场分布：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/njudoping.png)

验证电场。njupin
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/devsim1%E7%BB%B4%E7%94%B5%E5%9C%BA.png)


二维使用1v附近观察：
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/2D%E7%BB%93%E6%9E%9C.png)
x方向电场拟合较好


基于复合物理的电场，建立简单pn结
cv曲线不再是直线：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/cvpn%E7%BB%93.png)