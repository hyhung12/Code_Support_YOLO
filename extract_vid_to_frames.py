import os
import numpy as np
import cv2

# Input video file path
video_file = r"D:\CarDetection\Archive\RawVideo\Test_Video\Cam_ch1_20231008085907_20231008095907.mp4"

# Output folder where images will be saved
output_folder = r"D:\CarDetection\Archive\RawVideo\Test_Video\Cam1_2023_10_08_09g_10g"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_file)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_count = 0
frame_skip = 25*4-1  # Skip every 'frame_skip' frames

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Save the frame as an image only if it's a frame we want (frame_count % frame_skip == 0)
    if frame_count % frame_skip == 0:
        # Construct the output file path for the current frame
        output_file = os.path.join(output_folder, f'Video_frame_Cam1_2023_10_08_09g_10g_{frame_count:04d}.png')

        # Save the frame as an image
        cv2.imwrite(output_file, frame)

    # Increment the frame count
    frame_count += 1

# Release the video file
cap.release()

print(f"Frames extracted: {frame_count}")
