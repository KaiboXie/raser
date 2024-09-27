import os
def main(kwargs):
    label = kwargs['label']
    os.makedirs('output/elec', exist_ok=True)

    if label == 'ngspice_t1':
        import subprocess
        subprocess.run(['ngspice -b output/elec/T1_tmp.cir'], shell=True)
    elif label.startswith('ngspice_'):
        import subprocess
        elec_name = label.replace('ngspice_', '')
        subprocess.run(['ngspice -b param_file/circuit/{}.cir'.format(elec_name)], shell=True)
    elif label.endswith('_get_fig'):
        from . import ngspice_get_fig
        ngspice_get_fig.main(label.replace('_get_fig', ''))
    else:
        from . import readout
        readout.main(label)
