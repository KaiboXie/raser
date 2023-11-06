
环境变量配置：export PATH=/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin:$PATH
自动配置环境变量：vim(或 code) ~/.bashrc 打开文件后把上面一条指令写进去

提交作业（一般不直接使用）：hep_sub 要交的作业文件名
查看作业情况：hep_q -u（如果掉作业可以用hep_q -u -hold）
删除作业：hep_rm 要删的作业编号（-a删除所有名下的作业）
