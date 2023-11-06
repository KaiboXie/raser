
# 线路连接
alibava读出系统包含一块母板和一块子板，此外我们还需要准备一块探测器板用于给我们的探测器提供工作条件。

## 子板
子板上有一个供电端口和256个信号通道。将探测器板与子板固定在一起后用导线连接两个板之间的高压和地，并将sensor的读出与子板上我们要使用信号通道连接。sensor通过子板上的供电端口供电。
对于NJU-PIN，我们需要加入在读出电极后连接电容以及偏置电阻构成AC耦合

## 母板
母板通过排线与子板连接，并通过USB与电脑连接使用。母板上有三个trigger in和一个trigger out。三个trigger in分别为trigger1、trigger2、trigger pulse，用于RSrun模式，通过软件设置条件用来做外部触发。trigger out用于laser run模式，通过输出脉冲控制激光器产生激光。

# 信号采集原理
alibava的核心是子板上的beetle芯片。电荷注入beetle芯片后经过放大会到达芯片内部的一个电容上，电容一侧的电压会随之变化，系统采集的数据就是该电容在某一时刻的电压。经过calibration可以得知在什么时间采集这样电压以及电压和注入的电荷量之间的关系

# 软件操作
## 软件下载
https://alibavasystems.com/alibava-system-classic/

## 加载配置文件
- ![Alibava GUI.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/Alibava%20GUI.png)
- 打开软件，file-open，选择配置文件
- 配置文件的作用是保存自己修改过的参数
- 按需修改参数后保存配置文件就可以在之后的使用中open直接将所有参数修改为保存文件时的值

## 保存数据
- 在Setting-Data File Format中选择HDF5
- 每次需要保存文件时需要点击LogData，选择保存路径并命名，之后一次Start时产生的数据会保存在该文件中
- 需要在数据采集前LogData，否则无法保存采集到的原始数据
- 每一次保存数据都需要一次LogData

## pedestal
- 数据需要保存
- 开始前需要完成硬件除放置源（不输出信号）以外的所有工作
- ![ped.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/ped.png)
- 软件右上角区域选择pedestal
- 下方画图区域选择pedestal
- start开始运行
- 该数据用于计算各通道信号基线以及噪声

## calibration
- Delay calibration
	- 选择右上角calibration，并点击calibration按钮选择Delay
	- ![delay.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/delay.png)
	- 在主界面start，alibava内部会自己进行电荷注入并采集，改变注入与采集的时间间隔重复电荷注入并采集，得到不同时间间隔与采集到的信号大小之间的关系
	- 可以在signal下看见不同delay下采集到的signal值，取signal最大处时间为delay，将delay填写至图中delay处
	- 途中last为delay测试时间范围，Num.Pulses为bin宽，Samples/point为每个bin取均值的数据数
- Charge calibration
	- 选择右上角calibration，并点击calibration按钮选择Delay
	- ![calibration.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/calibration.png)
	- 在主界面start，alibava内部会自己进行电荷注入并采集，改变注入的电荷量重复电荷注入并采集，得到不同电荷注入量与采集到的信号大小之间的关系
	- 可以在signal下看见不同电荷注入量下采集到的ADC值，原始数据需要保存
	- 途中last为delay注入的电荷量的范围，Num.Pulses为bin宽，Samples/point为每个bin取均值的数据数
- calibration是用一个channel代表所有channel，使用的channel可以在setting-DAQ-calibration monitor channel下更改

## RSrun
- 使用外部触发时我们选用RSrun模式
- 在有上角选择RSrun并在Trigger中设定Trigger的阈值以及逻辑
- 该模式在每一次触发时记录所有channel的signal
- 软件会根据每一个event下各通道的signal/noise的值判断hit channel，画出hit channel的分布图hit map
- 根据每个event中hit channel的signal画出signal分布图
- signal/noise的阈值可以在
- 在使用的channel少的情况下软件画出的signal分布图非常没有参考价值，需要自己保存原始数据处理

# 实验结果
## 激光测试
### 操作
- 20230822测试结果
	- 在alibava的控制程序上疑似看见了信号
	- ![laser_signal_20230822.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/laser_signal_20230822.jpg)
	- 发现噪声水平异常增大（第一张为实验前，第二张为实验后）![noise1_20230822.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/noise1_20230822.png)![noise2_20230822.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/noise2_20230822.png)
- 噪声异常原因分析
	- 拔掉与高压源连线时噪声表现非常好
	- 与高压源连线后高压源处于关闭、开机不输出、输出状态或者高压源不接电时噪声都会增大非常多
	- 一天不同时段噪声水平不同（早上实验开始时正常，中午发现变高，晚上开始时和中午一致，很晚时变回正常水平）
	- 使用干电池串联后58V电压接入，噪声与拔掉高压源连线时相当
- 20230823测试结果
	- 使用干电池测试未能看见信号
	- 尝试使用高压源复现20230823结果，未能复现
	- 发现alibava系统出现数据异常
	- 经过实验，确定只要在激光打在sensor的同时alibava采集数据就会出现异常（打开激光并确保激光照在sensor上时使用RSrun采数），需要将alibava母板断电一段时间才可恢复正常，该结果可复现
	- 结合20230822测试噪声异常原因分析，系统可能在昨天测试时就开始出现异常
	- 系统异常表现：
		- 采数时软件中pedestal选项下的各通道noise分布图上可以看到使用的通道的noise变得极大（提高了两个数量级）
		- 软件中signal分布图在各个ADC值都有event
		- 关闭激光后重新测量pedestal，使用的通道的noise仍然极大
		- 可复现
	- 观察原始数据，可以看见0和1023，该值为系统ADC的上下限，猜测异常为激光信号过大导致

## 信号发生器电荷注入
- 使用0.5pF的电容与信号发生器做电荷注入
- 使用方波，上升沿和下降沿分两次注入信号
- 示波器产生的波形![befor C.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/befor%20C.jpg)
- 过电容后的波形![after C.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/after%20C.jpg)
- 确定注入的信号不会超过系统的量程
- 成功采集到了信号（连续三天复现）
	- 信号发生器输出0.1V![0.1V_20230901.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/0.1V_20230901.png)
	- 信号发生器输出0.2V![0.2V_20230901.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/0.2V_20230901.png)
	- 信号发生器输出0.3V![0.3V_20230901.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/0.3V_20230901.png)
- 结果分析
	- 可以确定我们收集到的是信号，且几乎没有噪声
	- 可以观察到明显的双峰，与我们使用方波，在上升沿和下降沿分别是两次信号注入的想法想相互印证
	- 观察原始数据，可以看见数据明显是大小交替排列的
	- 以每两个相邻的数据为一组，按每一组的最大值和最小值将数据分为两组，将两个峰分离了出来
	- 上升沿和下降沿产生的信号应该是完全对称的，这与数据相符合
	- 峰的形状目前猜测是由于无法做到完全的阻抗匹配产生的信号反射造成的![reflection.jpg](https://raser-1314796952.cos.ap-beijing.myqcloud.com/reflection.jpg)
	- 采集到的信号与我们注入的电荷量相比低于预期值，目前猜测是信号发生器与电容电荷注入不够快导致的

