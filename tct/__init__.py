def main(kwargs):
    label = kwargs['label']

    if label == 'extract_waveform':
        from . import extract_waveform
        extract_waveform.main()
    elif label == 'signal':
        from . import tct_signal
        tct_signal.main(kwargs)
    else:
        raise NameError
