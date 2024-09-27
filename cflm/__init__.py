import logging
from . import cflm
from . import RootPlot_1D
from . import get_signal
from . import cflm_Volt_Curr
from . import energy_deposition

def main(kwargs):
    label = kwargs['label']
    verbose = kwargs['verbose'] 

    if verbose == 1: # -v 
        logging.basicConfig(level=logging.INFO)
    if verbose == 2: # -vv 
        logging.basicConfig(level=logging.DEBUG)

    logging.info('This is INFO messaage')
    logging.debug('This is DEBUG messaage')

    if label == 'cflm':
       cflm.main()
    if label == 'RootPlot_1D':
       RootPlot_1D.RootPlot_1D()
    if label == 'GetSignal':
       get_signal.get_signal()
    if label == 'GetVolCur':
       cflm_Volt_Curr.getVolCur()
    if label == 'GetEdep':
       energy_deposition.getedep()
