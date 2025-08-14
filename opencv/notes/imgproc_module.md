# Image Processing Module (imgproc)

## Features
- Transformations: resize, rotate, warpPerspective
- Filtering: blur, GaussianBlur, medianBlur
- Edge Detection: Canny, Sobel
- Histogram: equalization, plotting

## Example
```python
import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('assets/lena.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
cv2_imshow(edges)

#Insights

Filtering reduces noise

Edge detection helps in feature extraction
