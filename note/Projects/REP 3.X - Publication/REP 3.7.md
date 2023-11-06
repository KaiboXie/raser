---
REP: 3.7
Title: Design of SiC beam monitor online system
Author: 何野、李星辰、肖素玉
Status: Draft
Type: Publication 
Created: 2021-10-01
Updated: 2023-04-25
---

- [ ] Release to team for review 📅 2023-11-10
# SiC BMOS

[[何野]],  [[李星臣]], [[肖素玉]]* 

## Overview 

-  [x] Hardware 
	-  [x] NJU SiC PIN [[REP 1.1]]
-  [x] Software 
	-  [x] Simulation: SiC in proton beam monitor REP signal after electronics[[REP 2.14]]
	- 批量质子峰值电流![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/5-19-edep.png)
	- 批量质子能量沉积![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/5-19-voltage.png)
-  [x] Presentation
	-  [x] [[何野]] The 41st RD50 Workshop [slides](https://indico.cern.ch/event/1132520/contributions/5149453/attachments/2556919/4406364/SiC%20for%20beam%20monitor%20system.pdf)


## Log 

### 2023-03-27 

确定一作、二作、通讯。

- 硬件部分[[REP 1.2]]
	- 辐照后PIN的IV、CV、CCE![charge.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/charge2.1.png)
	- 工作一年约6e14等效1MeV中子辐照，此时电荷收集效率大约为15%
- 软件部分：质子通过束流后沉积的能量、通过电子学产生的信号、实际读出的质子数
- 