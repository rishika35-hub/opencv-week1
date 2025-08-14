import cv2
import os
import urllib.request
import sys
import random

# --------------------------
# Ensure assets folder exists
# --------------------------
assets_folder = "assets"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)

# --------------------------
# List of sample images (tech, nature, etc.)
# --------------------------
image_urls = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",  # Nature
    "https://images.unsplash.com/photo-1518770660439-4636190af475",  # Tech
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",  # Ocean
    "https://images.unsplash.com/photo-1495567720989-cebdbdd97913",  # Mountains
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",  # Forest
]

# Pick a random URL
url = random.choice(image_urls)
filename = os.path.join(assets_folder, "random_image.jpg")

# --------------------------
# Download the random image
# --------------------------
print("Downloading a random image...")
urllib.request.urlretrieve(url, filename)
print(f"Image downloaded to {filename}")

# --------------------------
# Load and display the image
# --------------------------
img = cv2.imread(filename)
if img is None:
    print("Error: Could not load image.")
    sys.exit()

cv2.imshow("Random Image", img)
cv2.waitKey(0)  # Wait for
