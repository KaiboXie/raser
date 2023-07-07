---
REP: 1.6
Title: 辐照缺陷对4H-SiC LGAD/PIN 的定时性能的影响机制研究
Author: 李再一
Status: in progress
Type:  Hardware
Created: 2023-04-28
Updated: 2023-06-19
---

	


## SICAR1，SICAR2 外延片的边角料进行切片 

-  [x]  联系切片，将SICAR1 边角料切成5mm x 5mm 的大小
-  [x]  SICAR1-4块，SICAR2-4块 切片，寄送
-  [x] 检查切片结果，在显微镜下拍照标记 
-  [x] 盘点样品数目，并挑选要做辐照实验的样品

---
SICAR1 4块 共有5mm×5mm 4+4+4+4=16块
选4-b，4块做实验
![sicar1-4.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1-4.jpg)
---
SICAR2 4块 共有5mm×5mm 4+2+4+4=14块
选4下方的4块做实验
![sicar2-4.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar2-4.jpg)
---
SICAR1切割情况：可能需要清洗
![sicar1_2_br1_cut1.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1_2_br1_cut1.jpg)
---
![sicar1_3_mr3_cut1.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1_3_mr3_cut1.jpg)
---
![sicar1_4_bt.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar1_4_bt.jpg)
---
SICAR2切割情况：可能需要清洗
![sicar2_4.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar2_4.jpg)
---
![sicar2_1_left2_cut2.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar2_1_left2_cut2.jpg)
---
![sicar2_1_left3_cut1.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/sicar2_1_left3_cut1.jpg)
---




## 辐照实验

-  [ ] 调研并确认辐照样品的数目
-  [ ]  调研并确认辐照剂量和标度方法
选用SICAR1-6块，SICAR2-6块，$1.5mm\times 1.5mm$ NJU-PIN 6块
辐照剂量为$1\times10^{11},1\times10^{12},3.5\times10^{12},1\times10^{13},3.5\times10^{13},1\times10^{14}$ $n_{eq}/cm^2$
80MeV质子 ，束斑20cm* 20cm，实时流强15$\mu A$

|样品编号|样品类型|名称|辐照剂量($n_{eq}/cm^2$)|质子通量($p/cm^2$)|辐照时间(s)|
|---|---|---|---|---|---|---|
|1|SICAR1外延片||$2\times 10^{11}$|$1.407\times 10^{11}$|35.27|35.27s|
|2|SICAR1外延片||$1\times 10^{12}$|$7.037\times 10^{11}$|176.37|2min56.4s|
|3|SICAR1外延片||$3.5\times 10^{12}$|$2.463\times 10^{12}$|617.31|10min17.3s|
|4|SICAR1外延片||$1\times 10^{13}$|$7.037\times 10^{12}$|1763.73|29min23.7s|
|5|SICAR1外延片||$3.5\times 10^{13}$|$2.463\times 10^{13}$|6173.1|1h42min53.1s|
|6|SICAR1外延片||$1\times 10^{14}$|$7.037\times 10^{13}$|17637.3|4h53min57.3s|
|7|SICAR2外延片||$1\times 10^{11}$|$7.037\times 10^{10}$|35.27|35.27s|
|8|SICAR2外延片||$1\times 10^{12}$|$7.037\times 10^{11}$|176.37|2min56.4s|
|9|SICAR2外延片||$3.5\times 10^{12}$|$2.463\times 10^{12}$|617.31|10min17.3s|
|10|SICAR2外延片||$1\times 10^{13}$|$7.037\times 10^{12}$|1763.73|29min23.7s|
|11|SICAR2外延片||$3.5\times 10^{13}$|$2.463\times 10^{13}$|6173.1|1h42min53.1s|
|12|SICAR2外延片||$1\times 10^{14}$|$7.037\times 10^{13}$|17637.3|4h53min57.3s|
|13|$1.5\times 1.5mm$ NJU-PIN|i7|$1\times 10^{11}$|$7.037\times 10^{10}$|35.27|35.27s|
|14|$1.5\times 1.5mm$ NJU-PIN|c1|$1\times 10^{12}$|$7.037\times 10^{11}$|176.37|2min56.4s|
|15|$1.5\times 1.5mm$ NJU-PIN|a3|$3.5\times 10^{12}$|$2.463\times 10^{12}$|617.31|10min17.3s|
|16|$1.5\times 1.5mm$ NJU-PIN|g1|$1\times 10^{13}$|$7.037\times 10^{12}$|1763.73|29min23.7s|
|17|$1.5\times 1.5mm$ NJU-PIN|e1|$3.5\times 10^{13}$|$2.463\times 10^{13}$|6173.1|1h42min53.1s|
|18|$1.5\times 1.5mm$ NJU-PIN|a9|$1\times 10^{14}$|$7.037\times 10^{13}$|17637.3|4h53min57.3s|


## 辐照前后XRD对宏观缺陷的表征
- [ ]  2theta-theta测试研究辐照对面外晶格大小的变化的影响
    - [ ]  调研4H-SiC的晶体学结构，如晶格常数
    - [ ] 了解XRD测试原理
    - [ ] 2theta-theta测试（0-90°）
    - [ ] 外延峰是否只有4H-SiC，是否存在3C-SiC 或者6H-SiC 等构型，是否有Si或者C杂质，从而判断SICAR1 和SICAR2 的外延质量
    - [ ] 不同辐照强度对晶格常数是否发生明显的影响，是否随着辐照剂量的增大，而发生明显的变化
    
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230428153920.png)

-  [ ]  摇摆曲线测试研究辐照对结晶度变化的影响
-  [ ]  RSM测试研究辐照对面内晶格结构的影响


参考文献
Properties of 3C-SiC Grown by Sublimation Epitaxy on Different Type of Substrates
Microhardness of Electroless Composite Coating of Ni-P with SiC Nano-particles
Properties of 3C-SiC Grown by Sublimation Epitaxy on Different Type of Substrates
Microstructural study of ferromagnetic Fe-implanted 6H-SiC



