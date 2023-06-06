---
REP: 1.8
Title: 石墨烯/LGAD Fabrication
Author: 王聪聪 
Status: Active
Type: Hardware 
Created: 2023-5-24
Updated: 2023-04-25
---


# 石墨烯/LGAD Fabrication

[[王聪聪]]

[[王科琪]]完成光刻版的设计M1、M5、M6、M7（已完成）
[[王聪聪]]光刻版发给微电子所制作（5月底完成）
[[何野]]流片+测试，科琪电阻率分析，[[解凯博]]流片+电荷收集测试
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/55704333549fd5b7f38aab5cce28801.png)
- 刻蚀台面
    - 涂光刻胶（负胶）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/070d4f84ad7c2dac64b6853aa6348ca.png)
    - 光刻显影台面（M1）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/977cad92f7df66b5d3594ea683f9527.png)  ![|235](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography1.1_M1.png)
    - 刻蚀台面（四块2cmX2cm的片子由纳米所代做）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/459938d0874598c8fe200424e454a74.png)
- 制造电极  
    - 涂光刻胶（负胶）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/a9ca481ee4e6d9051d8ef0700206a71.png)
    - 光刻显影P电极（M2/5）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3c7bb11f55646b709c6a075dcb853c6.png)   ![|225](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography1.1_M5.png)
    - 电子束蒸发Ni/Ti/Al=60/30/80nm
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/8857d541febf8397dc428d70d011bee.png)
    - 金属剥离、清洗
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/1faa6b46ab0838fe3bf96989f21c996.png)
    - 淀积N电极
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/c9c5ee28a21139ce9dbdd820619318b.png)
    - 退火
- 淀积钝化层
    - PECVD淀积钝化层（182nm、364nm）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/a747a8991130fa7cb553ead0b7c3dd6.png)
    - 光刻显影（M4/6）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/7d296ce92de23b26acfd81e7ab64b4f.png)  ![|240](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography1.1_M6.png)
    - 刻蚀氧化层
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/399a02ae3488663155a3274c72ecc56.png)
-  制造Pad
    - 涂光刻胶（负胶）
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/cf2fe3d4af2dd872d5f9cf7ad30b94d.png)
    - 光刻显影（M3/7）
    ![|250](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/8886b83d97ce83aa769fe9d552bc1f6.png)   ![|240](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography1.1_M7.png)
    - 磁控溅射Pad（Al=500um）
    ![|250](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/68b2acdb457d5bacee3edc31d281088.png)
    - Pad剥离
    ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/25840183c782755a6d6fdeefa3d6201.png)
    - 低温退火
-  生长或者转移石墨烯（测试完）
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/68f3d4359535181a741eef37c817d11.png)
# Schedule 
| 时间 | 1号晶圆(实心电极) | 2号晶圆 (环形电极/石墨烯)|
| : - : | : - : | : - : |
| 2023-05-24 |刻蚀台面（M1）| 刻蚀台面（M1）|
| 2023-06-03 |光刻显影P电极（M2） | 光刻显影P电极（M5）|
| 2023-06- | 电子束蒸发 金属剥离 | 电子束蒸发 金属剥离 |
| 2023-06- | 淀积N电极、退火 | 淀积N电极、退火 |
| 2023-06- | PECVD淀积钝化层 | PECVD淀积钝化层 | 
| 2023-06- | 光刻钝化层掏孔(M4) | 光刻钝化层掏孔(M6) | 
| 2023-06- | 刻蚀钝化层| 刻蚀钝化层 |
| 2023-06- | 光刻显影(M3) | 光刻显影(M7) | 
| 2023-06- | 磁控溅射Pad| 磁控溅射Pad |
| 2023-06- | - |生长/转移石墨烯|
# Log 
1、欧姆接触电阻率测试（最优欧姆接触）[[何野]]测试，[[王科琪]]分析**

- [ ] P电极金属Ni/Ti/Al=60/30/80nm，不同退火温度800℃、950℃、1050℃（最高温度）欧姆接触电阻率。

- [ ] 相同退火温度（1050℃）不同金属的欧姆接触电阻率（Ni/Ti/Al=60/30/80nm，Ni/Ti/Al=60/20/100nm，Ni/Ti/Al=50/15/80nm）

2、温度对电学性能影响研究（工作电压、暗电流、电阻率结电容等）

- [ ] 不同尺寸器件和相同尺寸不同金属条件IV测试（以便优化器件尺寸）[[何野]]**测试分析**

- [ ] 正反向IV趋势判断器件好坏（工作电压）

- [ ] 反向IV暗电流测试（避光测试IV，反向电流与电压公式关系判断暗电流，分析不同器件暗电流规律，重点）

3、CV测试 **何野测试分析**

- [ ] 电阻率、面积、工作电压和结电容的关系

- [ ]  求势垒高度和有效掺杂浓度、时间分辨和开启电压。

注释：何野（根据**Radiation hardness characterization of low gain avalanche** **detector prototypes for the high granularity timing detector**论文得到IV-CV测量研究的一些数据）

4、电荷收集和时间分辨研究

- [ ] 电荷收集和时间分辨测试（[[何野[[解凯博]]]]测试）