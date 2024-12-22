# def main(kwargs):
#     label = kwargs['label']

#     if label == 'signal':
#         from . import tct_signal
#         tct_signal.main(kwargs)
#     else:
#         raise NameError

def main(kwargs):    
    label = kwargs['label']
    scan_number = kwargs['scan']
    job_number = kwargs['job']
    if label == 'signal':
        if scan_number != None:
            if job_number != None:
                from . import tct_signal_scan
                tct_signal_scan.job_main(kwargs)
            else:
                from . import tct_signal_scan
                tct_signal_scan.main(kwargs)
        else:
            from . import tct_signal
            tct_signal.main(kwargs)
    else:
        raise NameError