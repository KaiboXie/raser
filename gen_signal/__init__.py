def main(kwargs):
    label = kwargs['label']

    if label == 'signal':
        from . import gen_signal_main
        gen_signal_main.main(kwargs)
    else:
        raise NameError
