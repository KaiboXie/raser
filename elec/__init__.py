import os
import subprocess
from util.output import output

def main(kwargs):
    label = kwargs['label'] # Operation label or detector name
    name = kwargs['name']
    os.makedirs('output/elec/{}'.format(name), exist_ok=True)

    if label == 'trans':
        subprocess.run(['ngspice -b param_file/circuit/{}.cir'.format(name)], shell=True)
    elif label == 'get_fig':
        from . import ngspice_get_fig
        file_path = output(__file__)
        ngspice_get_fig.main(label, file_path)
    elif label == 'readout':
        from . import readout
        readout.main(label)
    else:
        from . import ngspice_set_input
        from . import ngspice
        input_p = ngspice_set_input.set_input(label)
        input_c=','.join(input_p)
        ngspice.ngspice(input_c, label, name)
        subprocess.run(['ngspice -b output/elec/{}/{}_tmp.cir'.format(label, name)], shell=True)
        file_path = output(__file__, label)
        from . import ngspice_get_fig
        ngspice_get_fig.main(name, file_path)
