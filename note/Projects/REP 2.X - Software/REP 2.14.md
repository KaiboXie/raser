
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
## Introduction

前置放大器（预放大）

作用
1. 提高系统的信噪比；
2. 减小信号经由电缆传送时外界干扰的影响；
3. 主放大器通过长电缆与探头相连，主放大器本身和操作 人员可以摆脱现场条件的限制；
4. 实现阻抗转换和匹配
分类
电压灵敏前置放大器
==电荷灵敏前置放大器== 
电流灵敏前置放大器
噪声与干扰 
    噪声：电子器件内部产生 
    干扰：来自于外部 
    散粒噪声与热噪声 
         散粒噪声：载流子数目涨落 
         热噪声：载流子热运动 
     噪声的主要来源 
         探测器的反向电流：低频噪声、散粒噪声（载流子的产生与消失）
          ==前置放大器的第一级放大器—场效应管：热噪声（低温环境工作）==

电荷灵敏前置放大器（CSA）

基本原理：将微弱的电荷信号转换为电压信号并放大到可以进行后续测量的程度
基本组成：
-   输入电容器
    将输入的电荷信号转换为电压信号
-   放大系统
     将电容器的电压信号放大到足以被测量的电平
-    反馈 
     提高电荷放大器的稳定性和线性


## CSA的ngspice模拟 

电流源：Iin pulse(0 10u 0 0.1n 0.1n 2n 4n 5)

1、三管电荷灵敏放大器
![屏幕截图 2023-04-12 143813.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-04-12%20143813.png)

![屏幕截图 2023-04-28 164319.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-04-28%20164319.png)

2、积分型电荷灵敏放大器![HWJS202208003_00800.jpg|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/HWJS202208003_00800.jpg)
![屏幕截图 2023-05-01 232454.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-05-01%20232454.png)

3、单电源电荷灵敏放大器
![屏幕截图 2023-04-12 170913.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-04-12%20170913.png)

![屏幕截图 2023-05-02 164814.png|500](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-05-02%20164814.png)
