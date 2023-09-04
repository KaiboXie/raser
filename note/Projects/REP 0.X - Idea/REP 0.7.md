---
REP: 0.7
Title: RAdiation SEmicondoctoR - RASER 
Author: 史欣、刘凯、谭雨航、杨涛
Status: Active
Type: Idea
Created: 2021-03-18
Updated: 2023-04-25
---

# RAdiation SEmicondoctoR - RASER


## v4.1 (2023-09-30)

- [ ]  Remove 'run' (use 'raser')
- [ ]  Figures using on ROOT
- [ ]  Input data with RDataFrame
- [ ]  Debug with 'logging' module
- [ ]  print with sys.stdout.write
- [ ]  filenames in lowercase (PEP8: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/))
- [ ]  Clean-up non-used code

<<<<<<< HEAD
Unit testing is a dance: tests lead, code follows.

[https://diveintopython3.net/unit-testing.html](https://diveintopython3.net/unit-testing.html)

计划做到的事：
- 以功能与物理过程为着力点设计run
	- 新设计的七项主目录：'Electric Profile' 'Particle Injection' 'Current Induction' 'Electronics' 'Time Resolution' 'Space Resolution' 'Transient Current Technique'
- 程序设计模块化，可以相互分离的程序就一定要做到可以单独测试
	- 反例：现在gsignal的运行，经过setting类，各个功能模块互相绑定，无法单独测试
- 配置文件模块化，同一的配置相互合并、不同的配置相互分离
	- 现有setting中，geant4配置、探测器配置、电子学配置相互杂糅
	- devsim中各个mesh相互分离，并且都不调用setting
- 升级Geant4、ROOT、DevSim等至最新版本，不再使用FEniCS*，避免使用Matplotlib**
	- \*在目前的物理目标下，FEniCS的用途被DevSim完全覆盖
	- \*\*Matplotlib的固有格式与行业内惯用的ROOT差异较大，不利于文章插图

阶段性目标：
-  [x] 配置新环境（Xin）
-  [ ] 测试g4pybind、numpy、scipy等模块的可用性（Xin, Chenxi）
-  [x] 配置新run格式（Chenxi）
-  [ ] 分离Setting.json，取消Setting.py（Chenxi）
-  [ ] 实现以下模块的独立运作：（Chenxi）
	-  [x] DevSim电场求解
	-  [ ] Geant4模拟粒子射入与能量沉积
	-  [ ] 感应信号收集
	-  [ ] 电子学波形处理
-  [ ] 在功能层面替换掉FEniCS与Matplotlib
	-  [ ] 多电极体系探测器电场Devsim求解
	-  [ ] Devsim加权场的快速求解与严格求解
	-  [ ] （可选）Devsim全耗尽电场快速求解
	-  [ ] 用ROOT画出物理模型曲线与IV/CV图

目前在dev分支下进行开发

## v4.0.0  (2023-08-31)
=======
## v4.0  (2023-08-31)
>>>>>>> upstream/main

Goal:  reduce the library, one task with one software 

- Debian: 11.7
- Geant4: 10.7.p02
- ROOT: 6.26.06
- DEVSIM: 2.6
- Remove FEniCS (focus on DEVSIM)
- Create 'raser' with setup.sh (will replace 'run') 

## v3.3 (2023-08-25)

- [[REP 3.4]]
- [[REP 3.5]]
- [[REP 3.6]]
- [[REP 3.7]]

## v2 

-  [[REP 3.3]]

## v1

- [[REP 3.1]]
- [[REP 3.2]] 

## Log

### 2021-03-19 

Start to work on raser with docker. 

### 2021-03-18 

Discussed with Kai, Yuhang, Tao, decided to create the software. 

Starting with KDetSim. 

Candidate names:

- Radiation Hard Semiconductor Devices Simulator
- RHSDS
 - RadDevSim
 - RASER - RAdiatin SEmiconductoR
- RADISIM
- RASES - RAdiatin SEmiconductor Simulator
- RADISC - RADIation Semiconductor Craft
- SCDS - Silicon Carbide Detector Simulator
- SIDESR - SIc DEtector SimulatoR 

Need to be inclusive, not just SiC. 

Talked with Chen, decided to use 'RASER'. 