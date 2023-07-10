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


# 建立一维实体模型
(./python/nju_pin_5mm_5mm_mesh.py--------./run 1.3.2)
## 必需的库文件（raser/Node）
## Step1.建立一维网格及模拟器件结构
使用devsim自带的网格划分器
````js
devsim.create_1d_mesh(mesh="dio")
````
实现名为dio网格的初始化，建立一个名叫dio的空白网格。
````js
devsim.add_1d_mesh_line(mesh="dio", pos=0, ps=1e-4, tag="top")
````
在网格内描点画线，上述代码指令是在dio网格中建立坐标为0的点，并从该点向坐标正方向延申$10^{-4}$,(反向延申则使用ns=)并将这条线段命名为top。
```js
devsim.add_1d_contact  (mesh="dio", name="top", tag="top", material="metal")
```
建立了几何网格后，对几何结构中需要的部分建立物理意义。例如电极，上述代码的意义是dio中找到top对应的线段，将该线段设置为金属电极，并将该电极命名为top。
```js
devsim.add_1d_region   (mesh="dio", material="SiliconCarbide", region=region, tag1="top", tag2="bot")
```
在几何网格中划分出需要求解的区域，上述代码意思为，在dio网格中建立区域，区域边界为top和bot标签所指的位置，该区域是碳化硅构成的。
```js
devsim.finalize_mesh(mesh="dio")
```
建立mesh结构
```js
devsim.create_device(mesh="dio", device=device)
```
建立使用上述要求的器件
## 定义掺杂
在Node库中调用CreateNodeModel函数，
```js
def CreateNodeModel(device, region, model, expression):

    '''

      Creates a node model

    '''

    result=devsim.node_model(device=device, region=region, name=model, equation=expression)
```
其中，device和region都是上述网格中定义的器件和区域，运算过程使用node_model(将节点看作源相，类比电动力学点电荷)。model一般指掺杂类型，比如施主-受主型。expression直接输入表达式表示掺杂浓度。
```js
devsim.edge_from_node_model(device=device,region=region,node_model="Acceptors")
```
在node模型里面建立边界，在node_model项中确定在node_model的类型，例如从节点模型中求电场分布，node_model设置为potential。及表明建立edge_model的位置。
# 输出画图
调用root画图即可（源代码使用python作图）
# 此处涉及到得到不同的模型
## node_model
点源模型，即可以通过点电荷计算电势内容
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/devsimnodemodel.png)

## edge_mode
参考边界上的节点模型，边缘模型相对于边界上两节点上计算的。
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/edgemodel.png)



# 仿真IV&CV曲线
## 定义主函数
定义参数的字典集合，括号内部sys.argv[ ]其实就是一个列表，里边的项为输入的参数，如果三叔中包含device项，则在字典中查看检索关键字和检索内容，关键字为device，检索内容是device对应的region。否则输出检索关键字错误。
定义网格，初始化解，
```js
initial_solution(device,region,para_dict)
```
在参数字典字典内调出初始解的类型，初始解类型包括：缺陷，最大电压值，电流，电容。
对于缺陷和最大电压，可以直接从字典中调用，对于电流和电容
电流采用
```js
solve_iv(device,region,v_max,para_dict)
```
通过最大电压求解电流
电容采用
```js
solve_cv(device,region,v_max,para_dict,frequency=1e3)
```
通过输入最大电压，频率为$10^3$ ,求解电容（猜测使用RC电路震荡，震荡频率设置为frequency）

## 定义参数字典
对参数列表做历遍，利用上面建立集合的计算方法建立字典，利用para.rpartition分割字符，并对检索关键字和检索内容建立字典。输出到参数字典。

## 确定网格
输入device对应字段，将device对应的网格导入，并将对应的网格，掺杂。
## 外延层集合建立

```js
devsim.set_parameter(name = "extended_solver", value=True)
```
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%A4%96%E5%BB%B6%E7%89%87.png)
extended_solver：      外延的精度矩阵牛顿和线性求解
extended_model：     外延的精度模型评价
extended_equation： 外延的精度方程装配
建立外延层参数。
```js
devsim.circuit_element(name="V1", n1=Physics.GetContactBiasName("top"), n2=0, value=0.0, acreal=1.0, acimag=0.0)
```
在电路中，交流电实数部分为1，虚部为0。电路中元素为电压，命名为V1，n1为电路节点，n2为默认0
## 定义初始解
调用初始解，从initial库中调用
```js
Initial.InitialSolution(device, region, circuit_contacts="top")
```
调用Initial函数库：
```js
def InitialSolution(device, region, circuit_contacts=None):
```
输入的参数为device，region，和电路电极
首先建立装配函数：
```js
CreateSolution(device, region, "Potential")
```
包括上一节点电势，本节点电势，命名为Potential@n0, Potential@n1
同时通过节点模型引入电子浓度初始值和空穴浓度初始值，初始值为NetDoping的绝对值（NetDoping通过掺杂时定义）：
```js
CreateNodeModel(device, region, "InitialElectron", "abs(NetDoping)")
```
通过节点模型导入边界模型：
```js
devsim.edge_from_node_model(device=device,region=region,node_model="InitialElectron")
```
通过导入之前节点模型的名称，实现将节点模型转化为边界模型，进一步计算电场（edge可以计算相邻节点之间的距离）。
只创建电势的物理模型（通过电势计算电场）：
```js
CreateSiliconPotentialOnly(device, region)
```
接下来通过引入偏压计算初始解：
```js
 for i in devsim.get_contact_list(device=device):

        if circuit_contacts and i in circuit_contacts:

            CreateSiliconPotentialOnlyContact(device, region, i, True)

        else:

            ###print "FIX THIS"

            ### it is more correct for the bias to be 0, and it looks like there is side effects

            devsim.set_parameter(device=device, name=GetContactBiasName(i), value=0.0)

            CreateSiliconPotentialOnlyContact(device, region, i)
```
对电极列表中的电极做一次循环：
如果电路中电极在电路电极中存在的话，则在只求得电势得到物理模型中建立电极，如果不存在，则把电极加入到电极的参数中并建立电极。
建立了电极和在devsim里面的虚拟电路时，使用直流解(最大迭代次数50)：
```js
devsim.solve(type="dc", absolute_error=1.0, relative_error=1e-10, maximum_iterations=50)
```


---
如果参数字典中有辐照项时，对于1维ITK_MD8，引入Initial库中的DriftDiffusionInitialSolutionSiIrradiated函数，进行初始化，否则改为DriftDiffusionInitialSolutionIrradiated函数。

### DriftDiffusionInitialSolutionIrradiated函数
```js
def DriftDiffusionInitialSolutionIrradiated(device, region, circuit_contacts=None):

    ####

    #### drift diffusion solution variables

    ####

    CreateSolution(device, region, "Electrons")

    CreateSolution(device, region, "Holes")

  

    ####

    #### create initial guess from dc only solution

    ####

    devsim.set_node_values(device=device, region=region, name="Electrons", init_from="IntrinsicElectrons")

    devsim.set_node_values(device=device, region=region, name="Holes",     init_from="IntrinsicHoles")

    #devsim.set_node_values(device=device, region=region, name="Electrons", init_from="InitialElectron")

    #devsim.set_node_values(device=device, region=region, name="Holes",     init_from="InitialHole")

  

    ###

    ### Set up equations

    ###

    CreateDriftDiffusionIrradiated(device, region)

    for i in devsim.get_contact_list(device=device):

        if circuit_contacts and i in circuit_contacts:

            CreateDriftDiffusionAtContact(device, region, i, True)

        else:

            CreateDriftDiffusionAtContact(device, region, i)
```
建立空穴解和电子解，设置求解变量，包括电子和空穴，变量来源于对电子和空穴做初始化。随后组装方程，对器件中电极列表中的电极，在电极处建立迁移漂移模型。
同理对于Si器件，则采用DriftDiffusionInitialSolutionSiIrradiated函数。


## 建立缺陷参数（还需完善）
在数据库文件中加入包含缺陷的参数，
## 解IV曲线
将area_factor设置为全局变量，新建condition选项，如果在参数字典中出出现了“irradiation”项，在condition中添加字符“_irradiation”，如果参数字典中出现了“defect”，则在condition中添加“_defect”，并收集缺陷参数（从参数字典中的检索内容和检索值）将缺陷参数补充到conditionho中。
### 初始条件
偏置电压初始值为0，创建偏置电压空白列表，建立顶部和底部电流空白列
新建表格文件，打开表格文件，文件名命名为（device和condition），表格表头为“voltage”“current”，将结果以行的形式的写入表格文件中。
对于1维ITKMD8器件，参数文件从“paras/setting.json"配置文件中导入。对其中的area_factor赋值。建立中值，强度和偏转电压，位置，电子和空穴的空白列表。
当偏置电压小于最大偏置电压时，