---
REP: 2.13
Title: DEVSIM 4H-SiC LGAD 2D 仿真开发
Author: 杨涛，赵森
Status: in progress
Type: Software
Created: 2023-4-28
Updated: 
---


# 3D-SiC SIMULATION
[[赵森]]
## 有限元方法

### 有限元方法介绍
有限元分析是利用数学近似的方法对真实物理系统（几何和载荷工况）进行模拟，将真实物理系统分割为简单而又相互作用的单元，从而用有限数量的未知量去逼近无限未知量的真实系统的一种方法。
有限单元法的基本思想是将问题的求解域划分为一系列的单元，单元之间仅靠节点相连。一般来说，有限元方法可以解决离散系统和连续系统两类问题。划分的单元要求形状简单，便于求解。


### 有限元方法步骤

1）建立真实几何模型   2)划分并优化网格   3）建立微分方程及边界条件  4）求解并进行数据处理
其中最重要的步骤是网格质量，一般来说，网格大小为器件线度的1/12。网格分为结构网格和非结构网格，结构网格为六面体，非结构网格为四面体。由于网格较难划分，因此出现了波前法，以及德式三角形法等算法加速非结构网格划分。

# 有限元方法器件仿真
````js
devsim.node_solution(device=device, region=region, name="Az")
````

使用泊松方程计算每一个有限元节点上的点电势
````js
devsim.edge_from_node_model(device=device, region=region, node_model="Az")
````

读取有限元上的节点电势
````js
devsim.edge_model(device=device, region=region, name="delAz",equation="(Az@n1 - Az@n0) * EdgeInverseLength")
````

电势是电场的负梯度，计算电势

## 遇到计算机问题
1.由于devsim自身电场模拟存在问题，导致指数项出现溢出。解决方法就要从用户身份转化为开发者，自己完善C++代码。
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E6%BA%A2%E5%87%BA%E6%8F%90%E7%A4%BA.png)
2.方形网格devsim无法计算。会出现devsim fatal。