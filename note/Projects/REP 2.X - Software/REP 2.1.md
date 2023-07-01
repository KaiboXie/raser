---
REP: 2.1
Title: SiC PIN Timing simulation 
Author: 谭雨航, 杨涛, 朱霖，李星臣，石航瑞  
Status: implemented
Type: Software
Created: 2021-10-01
Updated: 2023-05-18
---

# SiC PIN Timing simulation 


## Use DEVSIM
[[朱霖]], [[李星臣]], [[石航瑞]] 





### 2023-05-17 

- [[5 FEniCS 介绍]]
- [[6 DEVSIM 介绍]]


### 2023-05-22 & 05-29
-  [x] DEVSIM解一维电场     [[李星臣]]
-  [x] 对一维电场进行插值     [[石航瑞]]
-  [x] 插值后电场导入至RASER     [[石航瑞]]

### 2023-06-05
-   [x] 验证DEVSIM解一维电场的RASER结果     [[石航瑞]]

采用同一参数分别用FEniCS和DEVSIM得到模拟结果，如下图所示：
- FEniCS结果：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230701_shhr_devsim_1d_compare_fenics.png)

- DEVSIM结果
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230701_shhr_devsim_1d_compare_devsim.png)




## Use FEniCS 
[[谭雨航]],  [[杨涛]]

Implemented as: ./run 1.1 






