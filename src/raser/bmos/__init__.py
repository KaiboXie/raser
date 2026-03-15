
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
        from . import full_simulation
        full_simulation.get_signal()

    if label == 'DrawHistogram':
        from . import draw
        draw.DrawHistogram()

    if label == 'DrawSignal':
        from . import draw
        draw.DrawSignal()

    if label == 'BeamCreate':
        from . import beam_create
        beam_create.beam_create()
        
    if label == 'BeamRun':
        from . import full_simulation
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
        print(full_simulation.get_signal(geant4_json, output_path))
        # beam_run.beam_run()
    
