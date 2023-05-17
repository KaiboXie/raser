
## FEniCS 介绍

[[符晨曦]]

2023-05-17
13:00 ~ 13:15 

---
## 报告提纲

#### FEniCS是什么？
#### 利用FEniCS要解决什么物理问题？
#### 利用FEniCS要解决什么数学问题？
#### FEniCS如何解题？
#### 为什么说FEniCS是局限的？

#### FEniCS是什么？

是一个有限元求解器（Finite Element Method Solver）。

#### 利用FEniCS要解决什么物理问题？

场的信息

我们需要通过电场$\vec E=-\nabla U$来解决载流子的漂移问题$\vec v = \mu(N,T,E)\vec E$,
通过加权势$\vec E_w = -\nabla U_w$来获取载流子产生的感应信号$I_q(t)=q\vec v(t) \cdot \vec E_w(\vec r (t))$.

漂移问题实质上是微观欧姆定律$\vec J = \sigma \vec E$，感应信号的公式则来源于Shockley-Ramo定理，其中$\vec E_w=\nabla U_w$是加权场，满足
$$
\nabla^2U_w=0
$$
电极上具有边界条件$U_{electrode\ i}=0\ or\ 1$，读出电极置1，其余置0.

得到的物理结果：

![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/planar3Dxz2500.0.jpg)

#### 利用FEniCS要解决什么数学问题？

电场：
$$
\nabla^2U=\frac{-e}{\varepsilon\varepsilon_0}(N_D-N_A)
$$
其中：$U=U(\vec r)$是系统的电势，在电极上具有边界条件$U_{electrode\ i}=U_{bias\ i}$；
$N_D,N_A$是系统的受主和施主掺杂浓度，也可以说是系统的自由电荷密度。

加权场：
$$
\nabla^2U_w=0
$$

#### FEniCS如何解题？

将方程的微分形式
$$
-\nabla^2u(\vec r)=f(\vec r)
$$
转化为对所有试验函数（Test Function）v都成立、至多含一阶导的积分形式
$$
\int_\Omega -v\nabla^2u\ dx = \int_\Omega fv\ dx
$$

并利用分部积分给它降次：
$$
−\int_\Omega (∇^2 u)v\ dx=\int_\Omega ∇u·∇v\ dx− \int_{\partial\Omega} \frac{∂u}{∂n}v\ ds
$$
冯诺依曼边界条件下后一项可以被消掉，于是方程就变成了
$$
\int_\Omega ∇u·∇v\ dx = \int_\Omega fv\ dx
$$
这样就得到了方程的弱形式（weak form）。接下来，只需要在解空间（满足u边界条件的函数空间）搜索能让所有v都满足这个式子的u即可。

实际计算时要先将待求解空间离散化，将空间划成一个一个小网格（mesh）。

#### 为什么说FEniCS是局限的？

真实的、尤其是未耗尽或受辐照的器件，应该满足更为精确的方程：
$$
\nabla^2U=\frac{-e}{\varepsilon\varepsilon_0}(N_D-N_A+p-n+T_p-T_n)
$$
$p,n$是系统的空穴和电子密度，耗尽假设下可以把它们当成0。
$T_p,T_n$是系统的陷阱俘获载流子密度。

$p,n$满足漂移扩散方程：
$$
D_{p,n}\nabla^2(\Delta p,\Delta n)-\mu\vec E\cdot\nabla(\Delta p, \Delta n)+g_{p,n}=0
$$
该式由稳态条件、
$$q\frac{\partial \Delta p}{\partial t}=-\nabla\cdot \vec J=0$$
电流关系、
$$
\vec J_{drift\ p}=qp\mu_{p}\vec E,\ \vec J_{diffuse\ p}=D_{p}\nabla \Delta p
$$
和爱因斯坦关系
$$
D_p/\mu_p=k_BT/q
$$
得到，其中$\Delta p,\Delta n$指代非平衡载流子的数量，是载流子总密度与平衡时载流子密度之差。针对不同的复合/增益机制，$g_{p,n}$有不同的项，包括SRH复合与电离增益等。SRH复合是载流子密度的非线性函数，电离增益是场强的非线性函数。

对于一维的非耗尽器件，可以先行算出耗尽区宽度，再在指定的耗尽区内求解电场；但对于具有复杂结构的器件，耗尽区难以直接得到，也就无法应用耗尽假设。

FEniCS具有用牛顿法求解非线性的能力，但是几次尝试都不收敛。

Solving nonlinear variational problem.
  Newton iteration 0: r (abs) = 5.210e+04 (tol = 1.000e-10) r (rel) = 1.000e+00 (tol = 1.000e-09)
  Newton iteration 1: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 2: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 3: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 4: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 5: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 6: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 7: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 8: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 9: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 10: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 11: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 12: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 13: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 14: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 15: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 16: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 17: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 18: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 19: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 20: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 21: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 22: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 23: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 24: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 25: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 26: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 27: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 28: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 29: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 30: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 31: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 32: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 33: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 34: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 35: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 36: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 37: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 38: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 39: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 40: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 41: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 42: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 43: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 44: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 45: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 46: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 47: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 48: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 49: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
  Newton iteration 50: r (abs) = -nan (tol = 1.000e-10) r (rel) = -nan (tol = 1.000e-09)
Traceback (most recent call last):
  File "/afs/ihep.ac.cn/users/f/fuchenxi/raser/python/gsignal.py", line 165, in <module>
    main()
  File "/afs/ihep.ac.cn/users/f/fuchenxi/raser/python/gsignal.py", line 92, in main
    my_f = raser.FenicsCal(my_d,dset.fenics)
  File "/afs/ihep.ac.cn/users/f/fuchenxi/raser/raser/pyfenics.py", line 37, in __init__
    self.electric_field_with_carrier(my_d)
  File "/afs/ihep.ac.cn/users/f/fuchenxi/raser/raser/pyfenics.py", line 282, in electric_field_with_carrier
    solver.solve()
RuntimeError: 

*** -------------------------------------------------------------------------
*** DOLFIN encountered an error. If you are not able to resolve this issue
*** using the information listed below, you can ask for help at
***
***     fenics-support@googlegroups.com
***
*** Remember to include the error message listed below and, if possible,
*** include a *minimal* running example to reproduce the error.
***
*** -------------------------------------------------------------------------
*** Error:   Unable to solve nonlinear system with NewtonSolver.
*** Reason:  Newton solver did not converge because maximum number of iterations reached.
*** Where:   This error was encountered inside NewtonSolver.cpp.
*** Process: 0
*** 
*** DOLFIN version: 2019.2.0.dev0
*** Git changeset:  unknown
*** -------------------------------------------------------------------------
