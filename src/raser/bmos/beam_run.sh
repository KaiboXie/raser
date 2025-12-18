#!/bin/bash

export dir_raser="/scratchfs/atlas/xiekaibo/raser"
cd $dir_raser
source ./cfg/setup_lxlogin.sh
OUTPUT_ROOT="${dir_raser}/output/bmos/"
> $OUTPUT_ROOT/run_progress.txt

# 运行参数配置
beam_num=10
pulse_num=10

# 主运行循环
for ((beam=0; beam<beam_num; beam++)); do
    echo "▶ 开始处理束流 $beam"
    # 脉冲循环
    for ((pulse=0; pulse<pulse_num; pulse++)); do
        printf "$beam\n$pulse" > $OUTPUT_ROOT/run_progress.txt
        echo "▸ 处理脉冲 $pulse"
        raser bmos beam_run
    done
    echo "✓ 束流 $beam 处理完成"
    echo "---------------------------------"
done

echo "✅ 所有束流测试完成！"
