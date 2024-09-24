import shutil
import os

def set_pwl_input(pwl_file, cir_file, output_folder):
    string_list=[]
    shutil.copy(cir_file, output_folder)
    cir_file_basename=os.path.basename(cir_file)
    new_cir_file_basename=os.path.splitext(cir_file_basename)[0]+'_tmp'+'.cir'
    os.rename(output_folder+cir_file_basename, output_folder+new_cir_file_basename)
    print('Temporary circuit file has been created:', new_cir_file_basename)
    new_cir_file=os.path.join(output_folder, new_cir_file_basename)
    with open(pwl_file, 'r') as f:
        print('Reading pwl file........')
        lines = f.readlines()
        for i in range(len(lines)):
            if i == len(lines) - 1:  # 如果是最后一行
                lines[i] = lines[i].strip().replace(' ', ',')
                string_list.append(lines[i])
            else:
                lines[i] = lines[i].strip().replace(' ', ',') + ','
                string_list.append(lines[i])
    with open(new_cir_file, 'r') as f:
         replacement_line = 'I1 2 0 PWL(' + ''.join(string_list) + ')'
         output_lines = f.readlines()
         for i in range(len(output_lines)):
             if 'I1' in output_lines[i]:
                 output_lines[i] = replacement_line + '\n'
    with open(new_cir_file, 'w') as f:
         f.writelines(output_lines)
    print('Temporary circuit file has been modified')

    
