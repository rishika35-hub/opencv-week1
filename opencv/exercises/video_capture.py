import cv2
import os
import urllib.request
import random

# Ensure assets folder exists
assets_folder = "assets"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)

# List of sample videos
video_urls = [
    "https://github.com/opencv/opencv/raw/master/samples/data/vtest.avi",
    "https://github.com/opencv/opencv/raw/master/samples/data/highway.avi"
]

# Pick a random video
video_url = random.choice(video_urls)
video_path = os.path.join(assets_folder, "random_video.avi")

# Download if not exists
if not os.path.exists(video_path):
    print("Downloading random video...")
    urllib.request.urlretrieve(video_url, video_path)
    print("Video downloaded.")

# Play video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Random Video", frame)
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
