提出与解答问题请使用“代码”格式。

最后更新：2023/04/03

〇、程序运行顺序
python/入口程序：唤起
	raser/Node.py（定义数据类型）
		raser/Physics.py：PotentialOnly（定义忽略载流子相互作用和流动性时，器件的物理条件）
			raser/Initial.py：PotentialOnly（根据物理条件计算电场）
	raser/DriftDiffusion.py（定义电流）
		raser/Physics.py：PotentialOnly（定义器件的载流子分布条件）
			raser/Initial.py：PotentialOnly（根据物理条件计算电流、更新电场）
python/入口程序：计算（更新偏压条件，对应计算该偏压下的电流、电场与电容）
python/入口程序：画图（或专用画图程序，画出IV/CV图与电场图）

