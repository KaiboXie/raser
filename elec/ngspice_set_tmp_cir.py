import re
def ngspice_set_tmp_cir(input_c, det_name, ele_name):
    with open('./param_file/circuit/{}.cir'.format(ele_name), 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('I1'):
                # replace pulse by PWL
                pattern = r"pulse"
                lines[i] = re.sub(pattern + r".*", 'PWL('+str(input_c)+') \n', lines[i], flags=re.IGNORECASE)
            if lines[i].startswith('wrdata'):
                # replace output file name & path
                lines[i] = re.sub(r".*" + r".raw", "wrdata output/elec/{}/{}.raw".format(det_name, ele_name), lines[i])
        f.close()
    with open('output/elec/{}/{}_tmp.cir'.format(det_name, ele_name), 'w+') as f:
        f.writelines(lines)
        f.close()
# TODO: Need to be TOTALLY rewritten