def ngspice(input_c, input_p):
    with open('./param_file/circuit/T1.cir', 'r') as f:
        lines = f.readlines()
        lines[113] = 'I1 2 0 PWL('+str(input_c)+') \n'
        lines[140] = 'tran 0.1p ' + str((input_p[len(input_p) - 2])) + '\n'
        lines[141] = 'wrdata output/t1.raw v(out)\n'
        f.close()
    with open('./output/elec/T1_tmp.cir', 'w') as f:
        f.writelines(lines)
        f.close()
# TODO: Need to be TOTALLY rewritten