import os

import scipy.io

one_path = "M:\\experiment_12\\included\\__20170325_18068\\extra_p\\1228_child_boxes.mat"



mat = scipy.io.loadmat(one_path)

# print(mat.keys())
# print(mat['box_data']['frame_name'])

# for i in mat['box_data']['post_boxes'][0]:
#     print(i)

#     break


for i in mat['box_data']['frame_name'][0]:
    subID = ''
    image_name = i[0]
    print(i[0])
    break