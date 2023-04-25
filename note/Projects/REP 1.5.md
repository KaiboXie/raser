---
REP: 1.5
Title: T1 fabrication
Author: 何野 
Status: Active
Type: Hardware 
Created: 2022-10-01
Updated: 2023-04-25
---

# T1 fabrication

[[何野]]

- [ ] T1第一版的设计、生产
	设计：基于UCSC的读出电路，更改了图中R1的值和电路的形状（正方形→T型）
	目的：应用于散裂中子源的质子束流上，传感器选用NJU的5mm×5mm的SiC PIN
	
	原理图
![UCSC_simulation_circuit.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/UCSC_simulation_circuit.png)

	布线
![layout.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/layout.png)

目前T1第一版已经生产完成
	实物图
![T1_v1.0.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1_v1.0.jpg)

- [ ] T1第一版的测试
	- [ ] 355nm激光
		未辐照5mm的SiC PIN测试结果：
		测试环境：
		使用355nm激光 top扫描探测器中心位置 电路板直接连接示波器读出
		![laser_TCT.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/laser_TCT.jpg)


		100V时波形：
		![0_100V.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/100V.png)
		分布：
		![100.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/100.png)
		
		测试结果：对于355nm激光，能正常工作
	- [ ] β源
		- [ ] 测试环境：三号厅，Sr90β源，电路板连接20dB主放进行读出
			
			测试结果：在电压加到500V时，放置β源后，T型板不能看到β源的信号
			需要排查T型板不能看到β信号的原因，并解决问题
			
			- [ ] T型板噪声信号的采集
			是否由于噪声过大导致观测不到信号
			![T1noise.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/T1noise.png)
			- [ ] 快速的信号发生器在T型板上产生的信号（计划进行）
			模拟一个快速的信号观测电路的响应

