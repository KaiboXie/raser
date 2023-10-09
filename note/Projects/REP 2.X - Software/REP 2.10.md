---
REP: 2.10
Title: SiC in nuclear fusion
Author: 李星臣 石航瑞
Status: 
Type: Software
Created: 2023-04-11
---


# SiC in nuclear fusion 

[[李星臣]] [[石航瑞]] 

- 4GeV mu-
![d54f68f04885f81a03a96de3320a0ad.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/d54f68f04885f81a03a96de3320a0ad.png)
![ec3d4f4fd35b55f1225e33556c5aa29.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/ec3d4f4fd35b55f1225e33556c5aa29.png)

- 80MeV proton
![5e16a1842cadb2e2be9de73c9e28e86.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/5e16a1842cadb2e2be9de73c9e28e86.png)
![b36eb31096c00fd897358ef42d4d034.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/b36eb31096c00fd897358ef42d4d034.png)

- 1.6GeV proton
![a25b2488701f4adf3d6616c2a9125a8.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/a25b2488701f4adf3d6616c2a9125a8.png)
![6ebf4760bd2eeaea7dd99f95abe3327.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/6ebf4760bd2eeaea7dd99f95abe3327.png)


# beta simulation on SiC

## Introduction

## Waveform
初步结果为：![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230505_shhr_beta_simulation_1.png)

## Particle and Signal

[[2023-03-13-TEAM]]
-  [x] 增大模拟事件量获得gamma粒子在sic中的能量沉积
-  [ ] si strip初步
	-  [x] 了解熟悉当前raser中构建电场部分代码
	-  [x] 阅读相关文献
	-  [x] 初步确定如何在raser中构建多电极
[[2023-03-20-TEAM]]
-  [x] 不同能量gamma和e-在sic中能量沉积分布 ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p1.png)
-  [x] 1.33MeV gamma的能量沉积分布和峰值电压分布          ![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p2.png)  ![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p3.png)
-  [x] 峰值电流在5mV附近的波形和载流子漂移路径                ![350](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p4.png) ![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p5.png)
	- SIC: 30um, Ni: 0.1um, 环境：真空,  电压：500V, Gamma粒子能量沉积事例数：500-1000/1e6