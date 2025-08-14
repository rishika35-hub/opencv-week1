# Core Module (cv2 core)

## Key Points
- Handles basic data structures like Mat/arrays.
- Provides array operations: add, subtract, multiply.
- Utilities: cv2.sumElems(), cv2.mean(), cv2.norm().

## Example
```python
import cv2
import numpy as np

mat = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.uint8)
print("Sum:", cv2.sumElems(mat))
print("Norm:", cv2.norm(mat))

# Insights

Core module is the foundation for all OpenCV operations.

Every image is represented as a NumPy array.