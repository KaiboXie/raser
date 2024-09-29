def main(kwargs):    
    label = kwargs['label']
    scan_number = kwargs['scan']
    job_number = kwargs['job']

    if label == 'signal':
        if scan_number != None:
            if job_number != None:
                from . import gen_signal_scan
                gen_signal_scan.job_main(kwargs)
            else:
                from . import gen_signal_scan
                gen_signal_scan.main(kwargs)
        else:
            from . import gen_signal_main
            gen_signal_main.main(kwargs)