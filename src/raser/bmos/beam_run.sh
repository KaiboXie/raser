#!/bin/bash

OUTPUT_ROOT=$dir_raser/output/bmos/
> $OUTPUT_ROOT/run_progress.txt

beam_start=9999
beam_num=2
pulse_num=2

for ((beam=beam_start; beam<beam_start+beam_num; beam++)); do
    echo "beam$beam running"
    for ((pulse=0; pulse<pulse_num; pulse++)); do
        printf "$beam\n$pulse" > $OUTPUT_ROOT/run_progress.txt
        echo "pulse$pulse running"
        raser bmos BeamRun
    done
    echo "beam$beam completed"
    python $dir_raser/src/raser/bmos/save_beamtest_result.py $beam $pulse_num $dir_raser
    echo "test result has been saved as root"
    rm -rf $OUTPUT_ROOT/signal_beamtest
    echo "tmp file deleted"
    echo "---------------------------------"
done

echo "Beam test completed!!!"
