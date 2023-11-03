def make_config(object_names_file, out_name, dataset_path):

    config = open(f'{out_name}.yaml','w')
    config.write(f'path: {dataset_path}\n')
    config.write('train: train\n')
    config.write('val: test\n')
    config.write('names:\n')

    f = open(object_names_file,'r')

    for i, line in enumerate(f):
        config.write(f'  {i}: {line.strip()}\n')
    
    f.close()
    config.close()