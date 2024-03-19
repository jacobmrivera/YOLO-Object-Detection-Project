#!/bin/bash 

# INPUT_DIR=""
# MAX_SKIPS=1

IMAGES_DIR="G:\\jacob\\yolo_smoothing_check\\orig_data\\cam07_frames_p"
IMAGES_DIR="M:\\experiment_351\\included\\__20221112_10041\\cam07_frames_p"
source venv\\Scripts\\activate

# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\practice_labels"
# MAX_SKIPS=1
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_1.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir "$FRAME_OUTPUT"
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_2"
# MAX_SKIPS=2
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_2.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_3"
# MAX_SKIPS=3
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_3.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_4"
# MAX_SKIPS=4
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_4.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


INPUT_DIR="Z:\\Jacob\\YOLO_Predicted\\20221112_10041_cam07_predicted_data\\pred_labels_w_conf-c"
MAX_SKIPS=5
FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
OUTPUT_VID="Z:\\Jacob\\YOLO_Predicted\\20221112_10041_cam07_predicted_data\\pred_labels-c-check.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_6"
# MAX_SKIPS=6
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_6.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID

# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_7"
# MAX_SKIPS=6
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_7.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID

# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_8"
# MAX_SKIPS=6
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_8.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID

# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_9"
# MAX_SKIPS=6
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_9.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_10"
# MAX_SKIPS=10
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_10.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


# INPUT_DIR="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_15"
# MAX_SKIPS=15
# FRAME_OUTPUT="${INPUT_DIR}_drawn_frames"
# OUTPUT_VID="G:\\jacob\\yolo_smoothing_check\\pred_labels_skip_15.mp4"
# python scripts\\py_scripts\\smoothing_scripts\\smooth_annotations.py --input_dir $INPUT_DIR --max_skips $MAX_SKIPS
# python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir $IMAGES_DIR --labels_dir $INPUT_DIR --output_dir $FRAME_OUTPUT
# python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir $FRAME_OUTPUT --output_dir $OUTPUT_VID


deactivate
