
def main(kwargs):
    label = kwargs['label']
    if label == 'temperature':
        from . import cal_temp
        cal_temp.main()

    elif label == 'cflm_v1':
        from . import cflm
        cflm.main()
    elif label == "test":
        from . import g4_sic_energy_deposition
        command="./param_file/g4macro/gui.mac"
        g4_sic_energy_deposition.main()
    else:
        raise NameError(label)