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

    if label == 'gen_devsim_db':
        from . import gen_devsim_db
        gen_devsim_db.main()
    elif label == "3d_plugin_field":
        from . import test4hsic
        test4hsic.main("2dfield_4HSiC")
    elif label == "3d_ringcontact_Elefield":
        from . import test4hsic
        test4hsic.main("3d_ringcontact")
    else:
        from . import devsim_solve
        devsim_solve.main(kwargs)
