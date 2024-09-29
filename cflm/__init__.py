import logging
<<<<<<< Updated upstream
=======
from . import cflm
from . import get_signal
from . import cflm_Volt_Curr
from . import energy_deposition
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        from . import cflm
        cflm.main()
=======
       cflm.main()
>>>>>>> Stashed changes
    if label == 'GetSignal':
        from . import get_signal
        get_signal.get_signal()
    if label == 'GetVolCur':
        from . import cflm_Volt_Curr
        cflm_Volt_Curr.getVolCur()
    if label == 'GetEdep':
        from . import energy_deposition
        energy_deposition.getedep()
