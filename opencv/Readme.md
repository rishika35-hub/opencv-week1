# OpenCV Week 1 Assignment

## Project Overview
This repository contains the Week 1 assignment for OpenCV fundamentals. The goal of this assignment is to help you understand OpenCV core modules, image processing operations, basic drawing, video processing, and practical applications of OpenCV using Python.

You will also explore image and video handling, filters, edge detection, and auto-downloading of sample assets. This is a foundational step to prepare for advanced computer vision projects.

---

## Folder Structure



opencv-week1/
│
├── notes/
│ ├── introduction.md
│ ├── core_module.md
│ ├── imgproc_module.md
│ ├── misc_research.md
│
├── exercises/
│ ├── read_display_image.py
│ ├── basic_drawing.py
│ ├── video_capture.py
│ ├── filtering.py
│
├── research/
│ ├── opencv_applications.md
│ ├── os_window_differences.md
│
├── assets/
│ ├── lena.jpg # Sample image (auto downloaded)
│ ├── vtest.avi # Sample video (auto downloaded)
│ ├── basic_drawing_output.jpg # Output from drawing exercise
│
├── report.pdf
├── README.md
├── requirements.txt
├── setup_assets.py


---

## Notes (`notes/`)
These markdown files summarize the theoretical concepts of OpenCV:

1. **`introduction.md`**  
   - Overview, history, installation, and setup of OpenCV.
   - Reference links to official documentation and tutorials.

2. **`core_module.md`**  
   - Explains the core module: arrays, data structures, basic operations.
   - Example code included with NumPy arrays and OpenCV utility functions.

3. **`imgproc_module.md`**  
   - Explains image processing functions: filters, edge detection, transformations.
   - Includes code examples for Gaussian blur, Canny edge detection.

4. **`misc_research.md`**  
   - Research notes about OpenCV applications in robotics, medical imaging, AR, and differences in window handling between Linux and Windows.

---

## Exercises (`exercises/`)
These Python scripts demonstrate practical OpenCV operations.

### 1. `read_display_image.py`
- **Purpose:** Read and display an image.
- **File path:** `exercises/read_display_image.py`
- **How to run:**
```bash
python exercises/read_display_image.py


Expected Result: A window displaying lena.jpg. Press any key to close. A copy will be saved as assets/output.jpg.

Screenshot Example:
(Add image later: assets/screenshot_read_image.jpg)

2. basic_drawing.py

Purpose: Draw shapes (line, rectangle, circle) on a canvas.

File path: exercises/basic_drawing.py

How to run:

python exercises/basic_drawing.py


Expected Result: A window displaying a canvas with a blue line, green rectangle, and red circle. Saved as assets/basic_drawing_output.jpg.

Screenshot Example:
(Add image later: assets/screenshot_basic_drawing.jpg)

3. video_capture.py

Purpose: Read and play a video file.

File path: exercises/video_capture.py

How to run:

python exercises/video_capture.py


Expected Result: Window playing vtest.avi. Press q to exit.

4. filtering.py

Purpose: Apply image processing filters and edge detection.

File path: exercises/filtering.py

How to run:

python exercises/filtering.py


Expected Result: A window showing edges of the image after Gaussian blur and Canny edge detection.

Research (research/)

opencv_applications.md → Lists real-world applications of OpenCV in various industries.

os_window_differences.md → Explains how OpenCV handles windows differently in Linux and Windows.

Assets (assets/)

Contains downloaded sample images and videos.

All exercises automatically check for these assets and download them if missing.

Outputs from exercises are also saved here.

Setup Instructions

Clone the repository:

git clone https://github.com/<your-username>/opencv-week1.git
cd opencv-week1


Install dependencies:

pip install -r requirements.txt


Or install individually:

pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install matplotlib


Run setup_assets.py once to ensure assets are downloaded (optional; exercises also auto-download):

python setup_assets.py


Run any exercise:

python exercises/read_display_image.py
python exercises/basic_drawing.py
python exercises/video_capture.py
python exercises/filtering.py

Project Highlights

Fully Python-based OpenCV exercises.

Auto-download assets: No manual setup required.

Demonstrates core module, image processing, drawing, video handling.

Organized with notes, exercises, research for learning and reference.

Ready for VS Code and local execution.

Future Improvements

Add more exercises: camera capture, filters, and feature detection.

Include histogram visualization using matplotlib.

Expand research notes with deep learning and DNN examples.

References

OpenCV Official Documentation

YouTube Playlist for OpenCV Week 1