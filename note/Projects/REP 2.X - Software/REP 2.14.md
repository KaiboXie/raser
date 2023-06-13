
---
REP: 2.14
Title: CSA circuit simulation
Author: 李雁鹏
Status: in progress
Type: Software
Created: 2023-04-05
---
# CSA circuit simulation

[[李雁鹏]]

##### 电荷灵敏放大器

作用：将来自detector的电流信号放大并转换为电压信号，并==提高信号的信噪比==

基本结构：
![屏幕截图 2023-06-12 202000.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-06-12%20202000.png)
模拟结果：
![Cf单.png|375](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Cf%E5%8D%95.png)
一个电流脉冲经CSA放大后如上，但是多个电流脉冲到来时会产生信号的堆积
解决方案：引入泄放电阻形成泄放电路来将电容上的电荷泄放

引入泄放电阻后：
![屏幕截图 2023-06-12 202827.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-06-12%20202827.png)
模拟结果：
![Rf.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/Rf.png)
在电流电平结束后电容C<sub>f</sub> 上的电荷被电阻R<sub>f</sub> 泄放掉，信号的下降沿与泄放电路的时间常数$$\tau=R_fC_f$$ 有关，由于C<sub>f</sub> 与电荷灵敏放大器的变换增益有关不能轻易改变，所以要使用尽可能小的电阻来增大电荷的泄放速度，但较小的电阻会产生较大的热噪声

降低噪声，提高信噪比的思路：
噪声分类（以等效电流噪声或电压噪声表示）：
散粒噪声：载流子的产生与消失，正比于流过器件的平均电流、噪声的频域带宽
$$\overline{\Delta i^2_S}=2e\overline{I} \Delta f$$
热噪声：载流子的随机运动，正比于温度，反比于电阻
$$\overline{\Delta i_T^2}=\frac{4kT}{R}\Delta f$$
低频噪声（闪烁噪声，1/f噪声）：与器件的工作频率成反比
$$\overline{\Delta u_f^2}=A_f\frac{\Delta f}{f}$$ 降低噪声，提升信噪比的方法：
1、在运放输入端加一个场效应管，利用其高输入电阻来增大信号的输入，来提升信噪比
![JEFT+Amplifier circuit.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/JEFT+Amplifier%20circuit.png)
模拟结果：
![JEFT+Amplifier.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/JEFT+Amplifier.png)
存在反冲，需要引入极零相消电路来消除反冲

2、由最佳滤波原理可知：当输出信号的波形为准高斯型脉冲时信号的信噪比最佳，因此可以加一个滤波成形电路来整理波形
无源滤波成形电路：CR-(RC)<sup>4</sup> 
![CR-RC4 circuit.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/CR-RC4%20circuit.png)
经过波形整理后的输出模拟：
![CR-(RC)4-noam.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/CR-(RC)4-noam.png)
整形结果不佳，但是继续增加积分电路的级数，波形变化不大

3、将电阻泄放电路换成其他泄放电路来消除反馈电阻的热噪声
(1)RC低通反馈网络
![RC低通局部.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RC%E4%BD%8E%E9%80%9A%E5%B1%80%E9%83%A8.png)
模拟结果:
当输入电流信号为（0 -10n 0 0.1n 0.1n 10n 20n)时：
![RC低通10n.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RC%E4%BD%8E%E9%80%9A10n.png)
当输入信号为（0 -10n 0 0.1n 0.1n 0.00000001n 20n）时：
![RC低通0.00000001n.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RC%E4%BD%8E%E9%80%9A0.00000001n.png)
似乎对于脉冲宽度较窄的脉冲CSA不能正常工作
当不加输入信号时：
![RC低通0.png|382](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/RC%E4%BD%8E%E9%80%9A0.png)
或许是因为频率过高的原因，RC低通反馈CSA无法正常工作
接下来工作（weekly plan）
1）分别提出剔除RC低通滤波电路和场效应管来看观察是否能产生正确的波形
2）将RC低通滤波电路部分改为高通尝试输出正确的波形


