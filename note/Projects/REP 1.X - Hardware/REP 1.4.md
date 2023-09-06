---
REP: 1.4
Title: 4H-SiC PIN Fabrication（IHEP）
Author: 王科琪，何野，史欣，王聪聪*
Status: Active
Type: Hardware
Created: 2022-10-01
Updated: 2023-06-25
---

## Overview 
idea
    - [ ]  [[REP 0.11]]
Hardware 
	-  [x] SiC PIN [[REP 1.4]]
-  [x] Software 
	-  [x] Simulation: [[REP 2.5]]	
	
- Publication  
   - [ ] 

# 4H-SiC PIN  Fabrication

[[张希媛]]

4H-SiC PIN 外延片的制备——物理所

![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230424091343.png)

硬件支持：[[REP 1.4]]
-  [x] 寄送1.5mm x 1.5mm 做DLTS
-  [x] 询问DLTS结果
-  [x] 辐照实验  

DLTS 4H-SiC PIN 辐照前测试结果

![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605100015.png)


![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605100213.png)
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605100512.png)
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230605100655.png)
-  [x] 重复测试1.5x1.5mm 样品的IV，CV和原有数据进行比（6个样品）
          
CV结果：
            
![ea31d8f2b8766526dcf1714325fcc1a.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/ea31d8f2b8766526dcf1714325fcc1a.jpg)

IV结果：
![irradiation_IV_0626.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/irradiation_IV_0626.png)
第二次测漏电流增大的情况：
![compare_IV_i5_230626.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/compare_IV_i5_230626.png)

![compare_IV_e3_230626.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/compare_IV_e3_230626.png)


总结：IV曲线基本一致的样品为四片，有两片漏电流较大。部分样品电流在600V以上突然增加，二次测量发现其漏电流有了明显的增加。与5mmx5mm的样品相比，1.5mmx1.5mm的样品在漏电流增加之前相对较小。[[REP 1.1]]

- [x] 准备辐照计划
![dfa00cdf54d21eecae794c047261852.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/dfa00cdf54d21eecae794c047261852.jpg)

- [ ] 辐照后DLTS测试，观察其缺陷类型和缺陷浓度，俘获截面的变化，寄送样品给邹老师
- [ ] 调研文献，给出辐照前后深能级缺陷的分析，和测试结果相结合，安排[[李再一]]做一个报告
- [ ] 在仿真工作中，根据测试结果更新其缺陷信息如缺陷浓度和俘获截面，并更新其IV，CV仿真结果
- [ ] 辐照前样品的电荷收集 
- [ ] 辐照后样品的电荷收集，研究辐照造成的深能级缺陷对其电荷收集性能的影响
- [ ] 辐照前样品的时间分辨测试 beta源测试
- [ ]  辐照后样品的时间分辨测试 beta源测试，研究辐照造成的深能级缺陷对其时间分辨性能的影响
