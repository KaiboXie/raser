---
REP: 3.4
Title: Simulation of Edge Transient Current Technique on Silicon Low Gain Avalanche Detector
Author: 符晨曦、王浩博、肖素玉
Status: Revision 
Type: Publication 
Created: 2022-10-01
Team Report: 2023-05-22
---


# Simulation of Edge Transient Current Technique on Silicon Low Gain Avalanche Detector

[[符晨曦]]，[[王浩博]]，[[肖素玉]]*



## Overview 

-  [x] Hardware 
	-  [x]  SiC PIN [[REP 1.1]] 
-  [x] Software 
	-  [x] Simulation: [[REP 2.3]]
-  [x] Presentation
	-  [x] [[肖素玉]] The 36th RD50 Workshop [slides](https://indico.cern.ch/event/918298/contributions/3880551/attachments/2050616/3437058/RD50_TRACSforLGAD_suyu.pdf)
	-  [x] [[符晨曦]] The 41st RD50 Workshop [slides](https://indico.cern.ch/event/1132520/contributions/5149650/attachments/2555302/4409343/Edge-TCT%20simulation%20of%20LGADs%20in%20RASER.pdf)
-  [x] Publication
	-  [x] arXiv: http://arxiv.org/abs/2302.10020 
	-  [ ] Journal: review
	-  [ ] Webpage: 


- Source code: 
	https://code.ihep.ac.cn/raser/paper/p4_lgad_hpk_tct 
- Read
	https://latex.ihep.ac.cn/read/tvjjsgytjshm


## Release  

- v0.7（due 2023-01-06)
	-  [x] 完成基本图、表、公式 
	-  [x] 除了摘要和结论之外的主要段落和章节 
- v0.8 (due 2023-01-13)
	-  [x] 完成所有图、表、公式、数值结果
	-  [x] 文章所有文字部分内容完整，包括摘要、总结与讨论
	-  [x]  提交内部团队审核
- v0.9 (due 2023-01-20)
	-  [x] 语言通顺无语法错误
	-  [x] 确认作者名单、致谢、参考文献列表
- v1.0 (due 2023-01-27)
	-  [x] 全文达到投稿要求
	-  [x] 投稿杂志期刊 

- v1.1 (due 2023-05-05)
	-  [x] 做literature，确立文章创新点
	-  [x] 明确数据储存的位置
- v1.2 (due 2023-05-12)
	-  [x] 对主要数据处理过程做误差分析
	-  [x] 重制文章主要数据部分
		-  [x] trapping time
		-  [x] guard ring侧面结构
- v1.3 
	-  [x] 回复编辑部/预备重投稿


##  Log 


### 2023-10-07 

Resubmit to NIMA 

### 2023-05-22
当前结果
	迁移率模型：Reggiani
	激光腰宽：14um
	激光脉宽：600ps
	RC时间常数：500ps

LGAD幅值 电荷 电场 上升时间

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Amplitude_comparison.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Charge_comparison.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Elefield_comparison.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RiseTime_comparison.jpg)

pin幅值 电荷 电场 上升时间

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Amplitude_comparison_pin.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Charge_comparison_pin.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Elefield_comparison_pin.jpg)
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RiseTime_comparison_pin.jpg)

其他数据对的很好，但是电场数据与波形的具体形状关系很大，不好调

### 2023-02-21 

http://arxiv.org/abs/2302.10020  Online

### 2023-02-20 

Submitted to NIMA, arXiv

NIMA-D-23-00171 

