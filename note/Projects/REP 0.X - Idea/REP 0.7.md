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


## v4.0.1 

- [ ]  Figures using on ROOT
- [ ]  Input data with RDataFrame
- [ ]  Debug with 'logging' module
- [ ]  print with sys.stdout.write
- [ ]  New code with 'unittest'
- [ ]  filenames in lowercase
- [ ]  Clean-up non-used code

Unit testing is a dance: tests lead, code follows.

[https://diveintopython3.net/unit-testing.html](https://diveintopython3.net/unit-testing.html)

## v4.0.0  (2023-08-31)

Goal:  reduce the library, one task with one software 

- Debian: 12.1
- Geant4: 11.2
- ROOT: 6.28
- DEVSIM: 2.5
- Remove FEniCS (focus on DEVSIM)
- Re-write 'run' 

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