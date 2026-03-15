import os
import numpy as np
import ROOT
import sys
import pathlib

def mkdir(folder_name):
    try:
        os.makedirs(folder_name)
    except Exception as e:
        pass

def main(beam, pulse_num, raser_path):
    signals = []
    output_path = os.path.join(raser_path, "output/bmos/beamtest_result")
    mkdir(output_path)
    root_name = f"signal_beamtest_beam{beam}.root"

    beam_information_root = ROOT.TFile(os.path.join(output_path, root_name), "RECREATE")

    amplitude = np.zeros(1, dtype=float)
    amplitude_tree = ROOT.TTree("amplitude", "all signal amplitude")
    amplitude_tree.Branch("amplitude", amplitude, "amplitude/D")

    no_signal_pluse = np.zeros(1, dtype=float)
    no_signal_pluse_tree = ROOT.TTree("no_signal_pluse", "pulse number of haven't signal")
    no_signal_pluse_tree.Branch("amplitude", no_signal_pluse, "amplitude/D")

    for pulse in range(pulse_num):
        file_path = os.path.join(raser_path, "output/bmos/signal_beamtest", f'beam_{beam}', f'pulse_{pulse}')
        path_obj = pathlib.Path(file_path)
        raw_file = next(path_obj.glob('*.raw'), None)

        volt = np.zeros(1, dtype=float)
        time_signal = np.zeros(1, dtype=float)
        waveform_tree = ROOT.TTree(f"pulse{pulse}", "signal waveform")
        waveform_tree.Branch("volt", volt, "volt/D")
        waveform_tree.Branch("time", time_signal, "time/D")

        if not raw_file or not raw_file.is_file():
            print(f"beam{beam}pulse{pulse} no signal")
            no_signal_pluse[0] = pulse
            no_signal_pluse_tree.Fill()
            amplitude[0] = 0
        else:
            print(f"Processing beam{beam}pulse{pulse}")
            with open(os.path.join(file_path, raw_file)) as f:
                lines = f.readlines()
                v_temp = []
                for line in lines:
                    time_signal[0] = float(line.split()[0])*1e9
                    volt[0] = float(line.split()[1])*1e3
                    v_temp.append(volt[0])
                    waveform_tree.Fill()

            amplitude[0] = max(v_temp)
        waveform_tree.Write()
        amplitude_tree.Fill()
        signals.append(amplitude)

    amplitude_tree.Write()
    no_signal_pluse_tree.Write()
    beam_information_root.Close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        beam = int(sys.argv[1])
        pulse_num = int(sys.argv[2])
        raser_path = sys.argv[3]
        print(f"Processing beam: {beam}")
        main(beam, pulse_num, raser_path)
    else:
        print("Error: Beam number not provided")
        sys.exit(1)