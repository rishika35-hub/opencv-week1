import cv2
import os
import urllib.request
import sys
import random

# Ensure assets folder exists
assets_folder = "assets"
if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)

# List of random images
image_urls = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1518770660439-4636190af475",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1495567720989-cebdbdd97913",
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
]

# Pick a random image
url = random.choice(image_urls)
filename = os.path.join(assets_folder, "random_image_filter.jpg")

# Download if not exists
if not os.path.exists(filename):
    print("Downloading random image...")
    urllib.request.urlretrieve(url, filename)
    print("Image downloaded.")

# Load image
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Error loading image")

# Apply Gaussian blur
blur = cv2.GaussianBlur(img, (5, 5), 0)
# Apply Canny edge detection
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite(os.path.join(assets_folder, "output_edges.jpg"), edges)
