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


## Introduction 
硅微条探测器具有极好的位置分辨率，近年来，世界各大高能物理实验室几乎都采用它作为顶点探测器
目前进行的实验目标是根据ams上硅微条的参数来进行粒子入射模拟和top-tct模拟

## AMS parameter and Signal

|电极宽度|间隙宽度|厚度|
|---|---|---|
|60um|50um|100um|

# 当前进度

4.24-5.6
- 粒子入射位置距电极中心距离变化时电荷收集效率的变化（同样情况平板电极电荷收集效率视为100%）![|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/canvas.png)
- strip加入红光（660）tct单个示例（批量在跑中）![300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/laser.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.1eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.2eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.3eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.4eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/NO.5eletrode.png)
![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/E.png)
- 收缩加权场边界未能实现
- 

[[2023-04-10-TEAM]]
-  [x] si strip模拟中计算电荷收集效率
-  [x] 画图
- 7电极电场电势和加权场![600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/feild.png)
- 电极中心间距110um，电极60um，在第四个电极中心到第四个空隙中心取五个点（360um,375um,390um,402.5um,415um）计算电荷收集效率（最后一个电极为同一粒子入射时平板电极的电荷收集效率）![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/360cce.png)
- 电子从330um（顶）-440um（底）斜入射电荷收集效率![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/330-440.png)![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/drift_path.png)
[[2023-04-03-TEAM]]
-  [x] 将fenics解加权场改为二维
-  [x] 完成fenics解strip多电极加权场设置
-  [x] 完成多电极分别产生感应电流设置
-  [x] 完成多电极同时读出设置
-  [x] 画图
5电极时加权场分布和电场![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E7%94%B5%E5%9C%BA%E5%8A%A0%E6%9D%83%E5%9C%BA.png)
- ![500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E7%94%B5%E5%9C%BA%E5%BC%BA%E5%BA%A6.png)
- 第三个电极和第四个电极中间射入，各电极电流和漂移路径（每个电极宽60um，间隔50um）![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F1.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F2.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F3.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F4.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F5.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%81%8F%E6%BC%82%E7%A7%BB%E8%B7%AF%E5%BE%84.png)
- 第三个电极中间射入，各电极电流和漂移路径（每个电极宽60um，间隔50um）![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B41.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B42.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B43.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B44.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B45.png)![400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E4%B8%AD%E9%97%B4%E6%BC%82%E7%A7%BB%E8%B7%AF%E5%BE%84.png)