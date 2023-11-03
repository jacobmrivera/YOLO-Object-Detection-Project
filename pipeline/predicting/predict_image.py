from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('runs\\detect\\train33\\weights\\best.pt')

# Run inference on an image
# results = model('img_178.jpg')  # results list
model.predict('img_178.jpg', save=True, imgsz=1600, conf=0.1)

print("~~~~~~~~~~~~~~~~~~~~~~~`")
# # View results
# for r in results:
#     print(r.boxes)  # print the Boxes object containing the detection bounding boxesdataset_12/images/exp12__20151217_16963_img_361_parent.jpg
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs 
#     print(boxes)
#     print(masks)
#     print(keypoints)
#     print(probs)