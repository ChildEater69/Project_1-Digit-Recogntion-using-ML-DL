#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import time
# Load the video
video_path = r'C:\Users\Acer pc\OneDrive - Manav Rachna Education Institutions\Pictures\Camera Roll\WIN_20230510_23_46_46_Pro.mp4'
cap = cv2.VideoCapture(video_path)

# Create a VideoWriter object to save the enhanced video
output_path = r"C:\Users\Acer pc\OneDrive - Manav Rachna Education Institutions\Desktop\UI-II\New folder\enhanced_video.mp4"
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process each frame and enhance the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(0.1)

    # Apply histogram equalization to enhance the frame
    enhanced_frame = cv2.equalizeHist(gray_frame)

    # Write the enhanced frame to the output video
    out.write(enhanced_frame)

    # Display the enhanced frame (optional)
    cv2.imshow('Enhanced Video', enhanced_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()




