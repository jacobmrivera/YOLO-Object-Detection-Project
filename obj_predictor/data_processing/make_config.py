

'''
Reads json config file to create the .yaml file needed for YOLO training
Generates information in .yaml based on json config file

'''
def make_config(json_config):
    out_name = json_config["training"]["data"]
    dataset_path = json_config["dataset_folder"]

    yaml_config = open(f'{out_name}','w')
    yaml_config.write(f'path: {dataset_path}\n')
    yaml_config.write('train: train\n')
    yaml_config.write('val: test\n')
    yaml_config.write('names:\n')

    obj_num = json_config["constants"]["NUM_OBJS"]
    for i in range(obj_num):
        yaml_config.write(f'  {i}: {json_config["objects"][str(i)].strip()}\n')

    yaml_config.close()

    return



def make_config(out_name, dataset_path, obj_num, obj_dict, json_config):
    # out_name = json_config["training"]["data"]
    # dataset_path = json_config["dataset_folder"]

    yaml_config = open(f'{out_name}','w')
    yaml_config.write(f'path: {dataset_path}\n')
    yaml_config.write('train: train\n')
    yaml_config.write('val: test\n')
    yaml_config.write('names:\n')

    # obj_num = json_config["constants"]["NUM_OBJS"]
    for i in range(obj_num):
        yaml_config.write(f'  {i}: {obj_dict[i].strip()}\n')

    yaml_config.close()

    return