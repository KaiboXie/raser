---
REP: 2.4
Title: SiC-LGAD Timing simulation and Fabrication
Author: 符晨曦,杨涛,王科琪
Status: implemented
Type: Software
Created: 2021-10-01
Updated: 2023-04-25
---

# SiC-LGAD C-V simulation

### sicar1.1.8 一维C-V仿真（与测试结果有一定差距）
> raser field sicar1.1.8_cv_0-1v
![1D_SICAR1_LGAD_reverse_cv.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/1D_SICAR1_LGAD_reverse_cv.png)

# SiC-LGAD Timing simulation

[[符晨曦]]，[[杨涛]]，[[王科琪]]

Implemented as: ./run 2.1 

SICAR2时间分辨仿真：对500V-800V电压区间进行了仿真
        ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/wkq20230327_SICAR2_time_resolution.png)
        时间分辨率从49.9±0.3 ps下降至35.4±0.2 ps
        ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/wkq20230327_SICAR2_800V_BB.png)


# SiC-LGAD Fabrication

SICAR2离子注入仿真：
 -  仿真目标：
      注入浓度：4e17~1e19
      注入深度：0.4um
 - 目前问题：silvaco中没有SiC中注入Al离子的模型
     改变不同的入射角度，对离子注入进行仿真。设置的dose=6e14  energy=70  temperature=500 diffuse time=30  temperature=1000
            ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/wkq20230327%20ion_implant_tilt=0.png)
            ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/wkq20230327%20ion_implant_tilt=1.png)
            ![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/wkq20230327%20ion_implant_tilt=10.png)
  - synopsys仿真中，改变了注入能量和退火时间，结果显示的注入深度并没有明显改变。
      怀疑程序有问题，还没找到解决办法。
