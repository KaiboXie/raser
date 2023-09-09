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
- [ ]  Use 'unittest' to extend the function of raser 


## v4.0  (2023-08-31)

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