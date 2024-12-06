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

    if label == 'cflm':
        from . import cflm
        cflm.main()
    if label == 'GetSignal':
        from . import get_signal
        get_signal.main()
    if label == 'GetVolCur':
        from . import volt_current
        volt_current.main()
    if label == 'GetEdep':
        from . import energy_deposition
        energy_deposition.main()
    if label == 'RootPlot_1D':
        from . import sparticles_plot_1d
        sparticles_plot_1d.main()
    if label == 'GetTimeSignal':
        from . import time_signal
        time_signal.main()
    if label == 'PoissonGen':
         from . import poisson_generator
         poisson_generator.main()
    if label == 'GetSignalDsides':
         from . import get_signal_dsides
         get_signal_dsides.main()
    if label == 'PoiGenDsides':
         from . import poisson_generator_dsides
         poisson_generator_dsides.main()

    if label == 'GetPixelPrep':
        from . import cflm_pixel_area
        cflm_pixel_area.main()
    if label == 'GetPixelEdep':
        from . import get_pixel_area_edep
        get_pixel_area_edep.main()
    if label == 'GetPixelSignal':
        from . import get_pixel_area_siganl
        get_pixel_area_siganl.main()  
    if label == 'GetPixelMaxSignal':
        from . import get_pixel_area_maxsignal
        get_pixel_area_maxsignal.main()