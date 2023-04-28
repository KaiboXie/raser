---
REP: 2.5
Title: Improvement of Physics models in DEVSIM simulation
Author: 李再一
Status: 
Type: Software 
Created: 2023-04-05
---

# Improvement of Physics models in DEVSIM simulation

[[李再一]]



## 为什么要改进器件仿真中的物理模型？
器件的电学特性仿真是基于开源软件DEVSIM，利用Python添加物理模型并求解方程。在已有的仿真中，基于我们完全理解的物理模型，C-V特性曲线与实验数据基本一致，但是I-V特性曲线差别很大，相差大约16个数量级，等效于在载流子的复合率上大约有$10^{12}$的差别。
造成这样结果有以下可能的原因：
1.器件侧面存在漏电，将漏电项和目前的仿真结果叠加才能符合实验数据（机制不清楚）
2.当前模型中的参数不正确，需要调整参数（效果不好）
3.当前仿真中的模型不完整，需要添加模型（目前看来最可能的原因）
4.网格不完整（已经证明加上substrate没有差别；二维的网格也不可能解决一维的问题）

## Hurkx Model
在pn结中载流子可能从价带隧穿到导带（band to band tunneling,BTBT），可以等效为复合率
$R_{BTBT}=-B|F|^{\sigma}D_{Kane}exp(\frac{-F}{F_0})$
F是电场强度
添加$R_{BTBT}=-B|F|^{2.5}$后的结果：电流变化范围和实验数据完全符合，形状不同可能是更次级的效应导致的
![nju_pin_simple_tunneling.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/nju_pin_simple_tunneling.png)
从数学上调整后的结果，使用的公式为$R=-3.11q|E|^{2.5}exp(\frac{|E|}{30000})$![compare_IV_tnl.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/compare_IV_tnl.png)
![nju_pin_iv_improved.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/nju_pin_iv_improved.png)
![nju_pin_iv_improved_linear.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/nju_pin_iv_improved_linear.png)
把完全相同的公式和参数用在LGAD上面![230407_lgad_breakdown.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/230407_lgad_breakdown.png)
得出的电流水平过高（绝不可能符合实际，也测不出来），形状与之前的仿真类似，击穿电压小于2560V，比之前的仿真提前了1000多伏击穿
其他的结果：![compare_IV_tnl_exp2e4.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/compare_IV_tnl_exp2e4.png)


## Field-enhanced SRH Recombination
$R_{SRH}=\frac{np-n_i^2}{\tau_p(F)[n+n_i exp(\frac{E_t-E_i}{kT})]+\tau_n(F)[p+n_i exp(\frac{E_i-E_t}{kT})]}$
通常$\tau_n=\frac{1}{N_tr_n}$
在电场的作用下，$\tau_n=\frac{\tau_n}{1+g(F)}$
电场极强的情况下，载流子运动速度过快不能复合，可以直接忽略代表复合的np项