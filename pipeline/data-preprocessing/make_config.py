import runner

def make_config():
    out_name = runner.json_config["training"]["data"]
    dataset_path = runner.json_config["dataset_folder"]

    config = open(f'{out_name}','w')
    config.write(f'path: {dataset_path}\n')
    config.write('train: train\n')
    config.write('val: test\n')
    config.write('names:\n')

    # f = open(object_names_file,'r')

    # for i, line in enumerate(f):
    #     config.write(f'  {i}: {line.strip()}\n')
    
    # f.close()
    obj_num = runner.json_config["constants"]["NUM_OBJS"]
    for i in range(obj_num):
        config.write(f'\t{i}: {runner.json_config["objects"][str(i)]}\n')

    config.close()
