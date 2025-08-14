import cv2
import numpy as np

# --------------------------
# Create a black canvas
# --------------------------
canvas = np.zeros((512, 512, 3), dtype=np.uint8)  # 512x512 RGB image

# --------------------------
# Draw a blue line (BGR format)
# --------------------------
cv2.line(canvas, (0, 0), (512, 512), (255, 0, 0), 5)  # thickness=5

# --------------------------
# Draw a green rectangle
# --------------------------
cv2.rectangle(canvas, (100, 100), (400, 300), (0, 255, 0), 3)  # thickness=3

# --------------------------
# Draw a filled red circle
# --------------------------
cv2.circle(canvas, (256, 256), 50, (0, 0, 255), -1)  # -1 for filled

# --------------------------
# Display the result
# --------------------------
cv2.imshow("Drawing", canvas)
cv2.waitKey(0)  # Wait for any key press
cv2.destroyAllWindows()

# --------------------------
# Optionally save the drawing
# --------------------------
cv2.imwrite("assets/basic_drawing_output.jpg", canvas)
