# OpenCV Week 1 Assignment

## Project Overview
This repository contains the Week 1 assignment for OpenCV fundamentals using Python. The goal is to help you understand OpenCV core modules, image processing operations, basic drawing, video processing, and practical applications.  

It also demonstrates image and video handling, filters, edge detection, and automatic downloading of sample assets. This project is a foundation for advanced computer vision projects.

---

## Folder Structure

opencv-week1/
│
├── notes/
│ ├── introduction.md
│ ├── core_module.md
│ ├── imgproc_module.md
│ └── misc_research.md
│
├── exercises/
│ ├── read_display_image.py
│ ├── basic_drawing.py
│ ├── video_capture.py
│ └── filtering.py
│
├── research/
│ ├── opencv_applications.md
│ └── os_window_differences.md
│
├── assets/
│ ├── lena.jpg
│ ├── vtest.avi
│ └── basic_drawing_output.jpg
│
├── report.pdf
├── README.md
├── requirements.txt
└── setup_assets.py

---

## Notes (`notes/`)
These markdown files summarize theoretical OpenCV concepts:

- **[introduction.md](notes/introduction.md)** – Overview, history, installation, and setup.  
- **[core_module.md](notes/core_module.md)** – Core module: arrays, data structures, basic operations.  
- **[imgproc_module.md](notes/imgproc_module.md)** – Image processing functions: filters, edge detection, transformations.  
- **[misc_research.md](notes/misc_research.md)** – Research on OpenCV applications and OS window handling differences.

---

## Exercises (`exercises/`)

### 1. [read_display_image.py](exercises/read_display_image.py)
- **Purpose:** Read and display an image.  
- **How to run locally:**  
```bash
python exercises/read_display_image.py
Expected Result: Opens a window displaying assets/lena.jpg. A copy is saved as assets/output.jpg.

Screenshot Example:


2. basic_drawing.py
Purpose: Draw shapes (line, rectangle, circle) on a canvas.

How to run locally:

python exercises/basic_drawing.py
Expected Result: Window shows a blue line, green rectangle, and red circle. Saved as assets/basic_drawing_output.jpg.

Screenshot Example:


3. video_capture.py
Purpose: Play a video file.

How to run locally:

python exercises/video_capture.py
Expected Result: Window plays assets/vtest.avi. Press q to exit.

4. filtering.py
Purpose: Apply filters and edge detection.

How to run locally:

python exercises/filtering.py
Expected Result: Window shows edges after Gaussian blur and Canny edge detection.

Research (research/)
opencv_applications.md – Lists real-world applications of OpenCV.

os_window_differences.md – Explains OpenCV window handling differences between Linux and Windows.

Assets (assets/)
Contains sample images and videos downloaded automatically.
Outputs from exercises are also saved here.

cd opencv-week1
Install dependencies:

pip install -r requirements.txt
Or individually:

pip install opencv-python opencv-contrib-python numpy matplotlib
Download sample assets (optional, exercises auto-download too):

python setup_assets.py
Run any exercise:

python exercises/read_display_image.py
python exercises/basic_drawing.py
python exercises/video_capture.py
python exercises/filtering.py
Project Highlights
Fully Python-based OpenCV exercises.

Automatic asset downloading.

Demonstrates core module, image processing, drawing, and video handling.

Organized for easy learning and reference.

Ready for VS Code execution.

Future Improvements
Additional exercises: camera capture, filters, and feature detection.

Histogram visualization using matplotlib.

Extended research notes with deep learning and DNN examples.

References
OpenCV Official Documentation

YouTube Playlist: OpenCV Week 1
