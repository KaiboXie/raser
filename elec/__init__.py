
def main(kwargs):
    label = kwargs['label']

    if label == 'ngspice_t1':
        import subprocess
        subprocess.run(['ngspice -b output/elec/T1_tmp.cir'], shell=True)
    elif label == 'ngspice_ABCStar_fe':
        import subprocess
        subprocess.run(['ngspice -b param_file/circuit/ABCStar_fe.cir'], shell=True)
    elif label == 'drs4_get_analog':
        import subprocess
        subprocess.run(['ngspice -b param_file/circuit/drs4_analog.cir'], shell=True)
    elif label == 'drs4_get_fig':
        from . import drs4_get_fig
        drs4_get_fig.main()
    elif label == 'ABCStar_fe_get_fig':
        from . import ABCStar_fe_get_fig
        ABCStar_fe_get_fig.main()
    else:
        from . import readout
        readout.main(label)
