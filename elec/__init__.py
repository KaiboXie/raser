
def main(kwargs):
    label = kwargs['label']

    if label == 'ngspice_t1':
        import subprocess
        subprocess.run(['ngspice -b output/T1_tmp.cir'], shell=True)
    elif label == 'drs4_get_analog':
        import subprocess
        subprocess.run(['ngspice -b paras/circuit/drs4_analog.cir'], shell=True)
    elif label == 'drs4_get_fig':
        from . import drs4_get_fig
        drs4_get_fig.main()
    elif label == 'HPK-Si-LGAD-CCE':
        from . import cce_alpha
        cce_alpha.main()        
    else:
        raise NameError(label)