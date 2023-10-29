---
REP: 2.24
Title: PyMTL3 Hardware Simulation
Author: 符晨曦
Status: in progress
Type: Software
Created: 2023-10-21
Updated: 2023-10-21
---
---
基本对象：
Bits对象：储存n位2进制（或\[n/4\]位16进制）数字，可以做加减乘运算、位运算等
	分为“值”对象和“信号”对象

电路对象：继承mtl.Component
	InPort：输入
	OutPort：输出
	Wire：导线（？）
	update装饰器：即时更新下一个网格的值，使用运算符@=
	update_ff装饰器：延时更新下一个网格的信号，使用运算符<<=

---
模拟操作：
elaborate()
apply( mtl.DefaultPassGroup(foo) ) 可以改变输出模式
sim_reset() 会让 time_tick + 3
	reset the simulator which will raise the implicit reset signal for two cycles
传入输入信号：
	model.in_ @= input_value
	model.sim_eval_combinational()
sim_tick()推动时刻+1

---
输出模式：DefaultPassGroup 的参数
	linetrace=True可以提供电路级联输出
		需要相应定义line_trace函数
	textwave=True可以在终端提供电流可视化
		需要运行结束后执行model.print_textwave()
	vcdwave=路径 可以将结果输出为.vcd格式
		gtkwave可以可视化.vcd文件 *目前还没安装*

---
![将信号加1的电路运行示例](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E6%88%AA%E5%B1%8F2023-10-21%2013.22.46.png)

---
电路的连接与复用
	可以通过connect将上一个电路类的输出信号与下一个电路类的输入信号相连接
		这样的操作需要定义在大的电路类内部
		等价的语法糖：//=

---
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E6%88%AA%E5%B1%8F2023-10-21%2013.43.42.png)