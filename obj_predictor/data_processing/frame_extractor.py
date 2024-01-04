import cv2
import os

def process_video(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if the video is opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    frame_count = 0

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # Check if frame is read correctly
        if not ret:
            break

        # Save the frame as an image in the output folder
        frame_filename = f"frame_{frame_count:04d}.jpg"  # You can adjust the filename pattern
        frame_path = os.path.join(output_folder, frame_filename)
        cv2.imwrite(frame_path, frame)

        # Display the frame (optional)
        cv2.imshow('Frame', frame)

        # Increment frame count
        frame_count += 1

        # Break the loop on pressing 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture object and close windows
    video.release()
    cv2.destroyAllWindows()

    print(f"Processed {frame_count} frames. Saved in {output_folder}")

# Replace 'video_file_path.mp4' with the path to your video file
video_path = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\supplementary data\\bulldozer_firetruck.mp4"

output_folder = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\supplementary data\\bulldozer_firetruck_frames"
process_video(video_path, output_folder)
