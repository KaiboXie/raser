---
REP: 1.4
Title: 4H-SiC PIN and 石墨烯/4H-SiC PIN Fabrication
Author: 王聪聪*，王科琪
Status: Active
Type: Hardware
Created: 2022-10-01
Updated: 2023-06-25
---
SiC PIN IHEP   
  
[[王聪聪]]  [[王科琪]]   
  
## 外延片用途   
  
1、PIN探测器（与LGAD探测器性能对比）  
2、研究石墨烯/PIN探测器电荷收集+时间分辨性能  
3、研究SiC PIN与BJT集成器件  
## 外延片制作进展  
  
1、已经与厂家联系，厂家正在评估外延结构生长与价格，最少外延两片。（广东）
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-09-18%20090018.jpg)
2、利用软件仿真PIN结构 [[王科琪]]
3、泰科天润工程师访问探讨技术（随时可以沟通），代理外延片以及代加工碳化硅芯片， JBS MPS SBD 二极管和MOS   PiN  GTO  都有在流片的项目，BJT几年前也做过。
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-09-18%20090955.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-09-18%20091012.jpg)
4、完成两个合同的审批，准备签订合同。

Silvaco Tacd仿真4H-SiC的CV特性
[[蒋震宇]]

1、通过工艺仿真器Athena生成器件结构
![|600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo65dc42cd438ac27b32810074abf708f.png)


得到的仿真结果与实际对比（5mm×5mm）：
![|1000](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgobd819e18bed8eec69564dc1dacbc6e4.png)
在-400V时仿真出的电容值为2.384e-11F,换算之后为23.84pf，Athena仿真得到的电容值较为理想
全耗尽电压的理想值为484V，仿真的结果为440V左右,由于PIN的结构较为规则，考虑改用Atlas生成结构，尝试一下是否会有改变

2、通过器件仿真器Atlas生成器件结构
![|600](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo5a4aa477af67093609c1f5f54830b3d.png)

得到的全耗尽电压仍为440V左右
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo100.100.png)
给定的参数下仿真不出来理想的全耗尽电压，根据公式
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo55b7677b9773f339e781eb668d54b87.png)
只能改变 I 层掺杂浓度来获得理想的全耗尽电压
将 I 层浓度改为5.7e13$cm^{-3}$ 
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo1d06ac13b689fd3e4181b76200353ef.png)
得到了理想的全耗尽电压，与计算得到的484V一致。

3、每10um减小 I 区厚度，得到全耗尽电压变化趋势
![#left|全耗尽电压随I区厚度变化趋势](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo67de61f17aea43b0c47eb28479f1451.png)
全耗尽电压随着 I 区厚度的减小而减小，与理论相符。

4、如果要求全耗尽电压在300-350之间，则根据仿真结果推测，I 区厚度应该在78.5-85之间

d=78.5um时的全耗尽电压
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgo6015a535e19e3976cd5c9686eb1d3a7.png)


d=85um时全耗尽电压
!["d=85um时全耗尽电压"|800](https://raser-1314796952.cos.ap-beijing.myqcloud.com/L:%5Cpicgoad4ec106a09b7294f36513daf7447e3.png)

