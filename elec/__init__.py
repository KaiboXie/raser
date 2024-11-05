import os
import subprocess
from util.output import output

def main(kwargs):
    label = kwargs['label'] # Operation label or detector name
    name = kwargs['name']
    tct = kwargs['tct']
    os.makedirs('output/elec/{}'.format(name), exist_ok=True)

    if label == 'trans':
        subprocess.run(['ngspice -b setting/electronics/{}.cir'.format(name)], shell=True)
    elif label == 'get_fig':
        from . import ngspice_get_fig
        file_path = output(__file__)
        ngspice_get_fig.main(label, file_path)
    elif label == 'readout':
        from . import readout
        readout.main(label)
    else:
        if tct == None:
            from . import ngspice_set_input
            from . import ngspice_set_tmp_cir
            input_p = ngspice_set_input.set_input(label)
            input_c=','.join(input_p)
            ngspice_set_tmp_cir.ngspice_set_tmp_cir(input_c, label, name)
            subprocess.run(['ngspice -b output/elec/{}/{}_tmp.cir'.format(label, name)], shell=True)
            file_path = output(__file__, label)
            from . import ngspice_get_fig
            ngspice_get_fig.main(name, file_path)
        if tct != None:
            from . import ngspice_set_input
            from . import ngspice_set_tmp_cir
            input_p = ngspice_set_input.set_input(label, tct)
            input_c=','.join(input_p)
            ngspice_set_tmp_cir.ngspice_set_tmp_cir(input_c, label, name, tct)
            subprocess.run(['ngspice -b output/elec/{}/{}{}_tmp.cir'.format(label, name, tct)], shell=True)
            file_path = output(__file__, label)
            from . import ngspice_get_fig
            ngspice_get_fig.main(name, file_path, tct)
