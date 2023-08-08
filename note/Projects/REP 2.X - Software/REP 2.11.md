---
REP: 2.11
Title: Si strip simulation 
Author: 李星臣
Status: 
Type: Software
Created: 2023-04-11
---


# Si strip simulation 

[[李星臣]]

任务列表：
	1. strip表面红外激光扫描，研究位置分辨；
	2. RASER添加strip功能，研究strip电极与间隙宽度对位置分辨的影响；
	3. 辐照后红外激光测收集电荷，估算俘获时间；
	4. RASER模拟加入俘获时间贡献，通过改变俘获时间，模拟、测试辐照后位置分辨。

## Introduction 
硅微条探测器具有极好的位置分辨率，近年来，世界各大高能物理实验室几乎都采用它作为顶点探测器
目前进行的实验目标是根据ams上硅微条的参数来进行粒子入射模拟和top-tct模拟


## ITK Strip 红外扫描进展
- 接线电极：129-237
- 噪声
	![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/noise.png)
- 对焦：图为纵坐标各channel10000次峰值采样概率最大的值，横坐标为channel，可以看出，激光中心在256channel侧外部，焦点Z<33000
	![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/30000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/31000.png)
	![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/32000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/33000.png)
	![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/34000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/34000.png)
	![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/35000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/36000.png)
	![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/37000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/38000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/39000.png)![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/40000.png)
- 线断了，需重新打线
- 又臭又长的alibava说明书中发现的聚焦功能![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/focus.png)

## 激光强度测量
- 波长设为355与375nm几乎无区别，==高带宽读出与低带宽读出差别明显==，70A和80A差距较小，60A功率显著下降，整体激光强度均小于说明书中参数
- 60A                                                                                                                                                                ![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/60A%20low%20bandwidth.png)![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/60A%20high%20bandwidth.png)
- 70A                                                                                                                                 ![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/70A%20low%20bandwidth.png)  ![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/70A%20high%20bandwidth.png)
- 官方注释![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/bandwidth2.png)




## AMS parameter and Signal

|电极宽度|间隙宽度|厚度|
|---|---|---|
|60um|50um|100um|
- 加权场设置        
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/E.png)
- 电荷收集效率随粒子入射位置变化关系图
![|700](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/canvas.png)
- 总电荷收集效率（8为同一情况下平板电极电荷收集效率）
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/360cce.png)

![700](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/360.png)
红光tct批量扫描未完成（掉作业）





# 当前进度

-  [ ] strip红光tct批量扫描
-  [ ] fenics电场更改
[[2023-05-06-TEAM]]
- 粒子入射位置距电极(60um)（50um）中心距离变化时电荷收集效率的变化（同样情况平板电极电荷收集效率视为100%）![|700](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/canvas.png)
- strip加入红光（660）tct单个示例（批量在跑中）![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/laser.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.1eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.2eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.3eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.4eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.5eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/E.png)
- 收缩加权场边界未能实现

[[2023-04-17-TEAM]]
-  [x] 优化geant4模块
- Si Strip 下一步方向（除了研究重荷对产生信号的影响以外还有没有其他可研究的方向，si strip的实验数据都会有啥）(载流子浓度影响复合？)
[[2023-04-10-TEAM]]
-  [x] si strip模拟中计算电荷收集效率
-  [x] 画图
- 7电极电场电势和加权场![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/feild.png)
- 电极中心间距110um，电极60um，在第四个电极中心到第四个空隙中心取五个点（360um,375um,390um,402.5um,415um）计算电荷收集效率（最后一个电极为同一粒子入射时平板电极的电荷收集效率）![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/360cce.png)![350](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/360.png)![340](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/375.png)![340](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/390.png)![340](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/402.5.png)![340](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/415.png)
- 电子从330um（顶）-440um（底）斜入射电荷收集效率![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/330-440.png)![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/drift_path.png)

[[2023-04-03-TEAM]]
-  [x] 将fenics解加权场改为二维
-  [x] 完成fenics解strip多电极加权场设置
-  [x] 完成多电极分别产生感应电流设置
-  [x] 完成多电极同时读出设置
-  [x] 画图

- 完成了strip功能
- 用法![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/strip%E7%94%A8%E6%B3%95.png)
- 5电极时加权场分布和电场![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E7%94%B5%E5%9C%BA%E5%8A%A0%E6%9D%83%E5%9C%BA.png)
- ![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E7%94%B5%E5%9C%BA%E5%BC%BA%E5%BA%A6.png)
- 第三个电极和第四个电极中间射入，各电极电流和漂移路径（每个电极宽60um，间隔50um）![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F1.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F2.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F3.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F4.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F5.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F%E6%BC%82%E7%A7%BB%E8%B7%AF%E5%BE%84.png)
- 第三个电极中间射入，各电极电流和漂移路径（每个电极宽60um，间隔50um）![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B41.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B42.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B43.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B44.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B45.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B4%E6%BC%82%E7%A7%BB%E8%B7%AF%E5%BE%84.png)

-  [x] Fenics更改边界条件解两个电极电场 ![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-24-p6.png)
[[2023-03-27-RASER]]
-  [x] 将电场修改为平板型，加权场改为单电极读出（顶部读出？）![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-31-1.png)
- x=1000um时波形![550](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-31-2.png)
- x=2500um时波形![550](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-31-3.png)
- x=4000um时波形![550](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3-31-4.png)
