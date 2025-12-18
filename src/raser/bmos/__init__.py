
'''
@Date       : 2024
@Author     : Ye He, Kaibo Xie
@version    : 2.0
'''

import logging

def main(kwargs):
    label = kwargs['label']
    verbose = kwargs['verbose'] 

    if verbose == 1: # -v 
        logging.basicConfig(level=logging.INFO)
    if verbose == 2: # -vv 
        logging.basicConfig(level=logging.DEBUG)

    logging.info('This is INFO messaage')
    logging.debug('This is DEBUG messaage')


    if label == 'GetSignal':
        from . import get_signal
        get_signal.get_signal()
        
    if label == 'histogram_signal':
        from . import histogram_signal
        histogram_signal.get_signal()

    if label == 'one_histogram':
        from . import histogram
        histogram.main("one")

    if label == 'all_histogram':
        from . import histogram
        histogram.main("all")

    if label == 'beam_create':
        from . import beam_create
        beam_create.beam_create()
        
    if label == 'beam_run':
        from . import beam_run
        import os
        from ..util.output import output, create_path

        with open(os.path.join(output(__file__), 'run_progress.txt')) as f:
            f = f.readlines()
            beam = int(f[0])
            pulse = int(f[1])

        output_path = os.path.join(output(__file__), 'signal_beamtest', f'beam_{beam}', f'pulse_{pulse}')
        json_path = os.path.join(output(__file__), 'beam_information', f'beam_{beam}')
        create_path(output_path)

        geant4_json = os.path.join(json_path, f'pulse_{pulse}.json')
        print(beam_run.get_signal(geant4_json, output_path))
        # beam_run.beam_run()
    
    if label == 'run':
        import subprocess
        subprocess.run(["sh", "beam_run.sh"], capture_output=True, text=True)