---
REP: 1.2
Title: SICAR1 Fabrication
Author: 张希媛、王聪聪,何野，王科琪
Status: Active
Todo: 科琪上传第一次流片结果，何野测试IC和CV
Type: Hardware 
Created: 2022-10-01
Updated: 2023-04-28
---

# SICAR1 Fabrication（第一次）

[[张希媛]], [[王聪聪]]


## 芯片外延



## 芯片制作
### 光刻版1.0设计（M1、M2、M3）
[[王科琪]]
- 整体效果：
    ![photolithography.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/photolithography.png)
- M1
    ![M1.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/7014bb4b7ac4846c4677685ea976e33.png)
- M2
    ![M2.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/24d01f4c8216f032963ad5bf83012c0.png)
- M3
    ![M3.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/74c68ea12c0d1f5b3ad4f171863d8e7.png)
- M4钝化层
    ![M4.png |400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/3e5f112e22f4965936333807e059b48.png)
   

### 第一次流片工艺
[[王科琪]]， [[何野]]
- 清洗![clean.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/clean.png)
- 刻蚀台面
    - 涂光刻胶（负胶）
    - 光刻显影台面（M1）
    - 刻蚀台面（四块2cmX2cm的片子由纳米所代做）
	![刻蚀1.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%88%BB%E8%9A%801.png)
	![刻蚀2.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%88%BB%E8%9A%802.png)


- 制造电极  
    - 涂光刻胶（负胶）
    - 光刻显影P电极（M2）![M2-1-3-50.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/M2-1-3-50.jpg)
    ![M2-1-2-50.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/M2-1-2-50.jpg)

    - 电子束蒸发Ni/Ti/Al=60/30/80nm
    - 金属剥离、清洗
    ![20230404_15_2.JPG](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230404_15_2.JPG)

	![20230404_15_5.JPG](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230404_15_5.JPG)

    - 淀积N电极
    - 退火
- 淀积钝化层
    - PECVD淀积钝化层（364nm）
    ![SICAR1_2_3.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/SICAR1_2_3.jpg)

    - 光刻显影（M2）
    - 刻蚀氧化层
-  制造Pad
    - 涂光刻胶（负胶）
    - 光刻显影（M3）
    - 磁控溅射Pad（Al=500um）
    - Pad剥离
    - 低温退火
### 第一次流片工艺流程图
[[王科琪]]
![process.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/e314bbfe289d745761c1e47f80207de.jpg)

### 第一次流片工艺花销（大致）
| 序号 | 工艺 | 数量 | 花销 |
| : - : | : - : | : - : | : - : |
| 1 | 光刻P电极 | 2 | 1500（估计） |
| 2 | 蒸镀P电极金属 | 2 |3000 |
| 3 | 退火 | 2 | 3000（估计） |
| 4 | 光刻台面+台面刻蚀 | 6 | 11195 |
| 5 | 光刻P电极 | 2 | 1500（估计） |
| 6 | 蒸镀P电极金属 | 2 | 3000 |
| 7 | 蒸镀N电极金属 | 4 | 1500 |
| 8 | 退火 | 4 | 6000 |
| 9 | PECVD 二氧化硅 | 4 | 1000 |
| 10 | 光刻钝化层 | 4 | 1900 |
| 11 | 刻蚀钝化层 | 4 |
| 12 | 光刻钝化层 | 4 | 1900 |
| 13 | 刻蚀钝化层 | 4 |
| 总计 | | 4 | 35495 |

### 第一次流片问题与后期改进
[[王科琪]]
| 序号 | 问题 | 改进 |
| : - : | : - : | : - : |
| 1 | 电极出现白色圆点 | 调整退火与PECVD的顺序，先退火 |
| 2 | 漂洗二氧化硅时，洗去过量的二氧化硅 | 
| 3 | 晶圆表面有杂质 | 每一次工艺之前都要对晶圆进行清洗 |
| 4 | 光刻版 | 增加钝化层；重新设计版标；修改欧姆接触电阻率测试版 |

#### 第一次流片IV和CV测试
[[何野]]
#### 第一次欧姆接触测试
[[何野]]

# Log 
1、欧姆接触电阻率测试（最优欧姆接触）**何野测试，科琪分析**

- [ ] P电极金属Ni/Ti/Al=60/30/80nm，不同退火温度800℃、950℃、1050℃（最高温度）欧姆接触电阻率。

- [ ] 相同退火温度（1050℃）不同金属的欧姆接触电阻率（Ni/Ti/Al=60/30/80nm，Ni/Ti/Al=60/20/100nm，Ni/Ti/Al=50/15/80nm）

2、温度对Sicar1电学性能影响研究（工作电压、暗电流、电阻率结电容等）

- [ ] 不同尺寸器件和相同尺寸不同金属条件IV测试（以便优化器件尺寸）**何野测试分析**

- [ ] 正反向IV趋势判断器件好坏（工作电压）

- [ ] 反向IV暗电流测试（避光测试IV，反向电流与电压公式关系判断暗电流，分析不同器件暗电流规律，重点）

3、CV测试 **何野测试分析**

- [ ] 电阻率、面积、工作电压和结电容的关系

- [ ]  求势垒高度和有效掺杂浓度、时间分辨和开启电压。

注释：何野（根据**Radiation hardness characterization of low gain avalanche** **detector prototypes for the high granularity timing detector**论文得到IV-CV测量研究的一些数据）

4、电荷收集和时间分辨研究

- [ ] 电荷收集和时间分辨测试（何野+谢凯博测试）


