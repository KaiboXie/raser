---
本手册可能存在一定问题，欢迎提出修改并指正
---

# DEVSIM数据集的建立
(./python/gen_devsim_db.py--------./run 1.3.1)
## 常数命名（CreateGlobalConstant & CreateSiliconCarbideConstant &CreateSiliconConstant）
在全局变量中，定义了类如电流、玻尔兹曼常数、真空介电常数、和温度。之后使用devsim.add_db_entry命令使devsim了解常数，使devsim了解该常数如何调用，数值，以及其对应的单位。例如：
```js
devsim.add_db_entry(material="global",   parameter="T",    value=T,     unit="K",   description="T")
```
在碳化硅和硅中的常数定义，则定义了导带价带的电子浓度，载流子寿命，载流子浓度和载流子漂移速率等与材料有关的常数。通用使用devsim.add_db_entry命令读入程序。例如：

````js
devsim.add_db_entry(material="SiliconCarbide",   parameter="tau_p",  value=0.5e-6,    unit="s",         description="Constant SRH Lifetime of Hole")
````
## 计算涉及到的模型——Hatakeyama效应（CreateHatakeyamaImpact）& VanOvenstraeten效应（雪崩效应模型）（CreateVanOvenstraetenImpact）

````
The Hatakeyama avalanche model describes the anisotropic behavior in 4H-SiC power devices. The impact ionization coefficient is obtainedaccording to the Chynoweth law.
    Ref DOI: https://onlinelibrary.wiley.com/doi/abs/10.1002/pssa.200925213
````
该效应主要针对$4H-SiC$, 涉及到$[1120]$和$[0001]$ 晶向。定义了不同晶向上载流子浓度和该效应涉及到的温度和在ev单位下$\hbar$$\omega$取值。并且定义系数：（cal_impact_coefficient(electric_field)
计算具体为
````js
n_coeff = gamma*n_a*math.exp(-(gamma*n_b/electric_field))
p_coeff = gamma*p_a*math.exp(-(gamma*p_b/electric_field))
````

计算得到不同电场对应SiC电子空穴的漂移系数，步长为电场上限/1000.以数组的形式存入之前定义的空白数组内。

总结：1.3.1确定了计算的模型和材料参数，深刻了解需要研读文献
Ref DOI: https://onlinelibrary.wiley.com/doi/abs/10.1002/pssa.200925213