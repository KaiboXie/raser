def main(kwargs):
    label = kwargs['label']

    if label == 'signal':
        from . import tct_signal
        tct_signal.main(kwargs)
    else:
        raise NameError
