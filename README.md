# Real-Time Video Filtering with Webcam using OpenCV

## Description

The Real-Time Video Filtering project is a Python application that leverages the power of OpenCV, NumPy, and time libraries to capture video from a webcam and apply a variety of filters in real-time. The project provides an interactive and visually appealing interface for users to experiment with different filter algorithms.

The project incorporates several filtering techniques to enhance video frames captured by the webcam. These techniques include:

1. Canny Edge Detection: The Canny edge detection algorithm is employed to identify edges in the video frames. This filter highlights boundaries, making it useful for edge detection and object recognition.

2. Global and Adaptive Thresholding: The project utilizes global and adaptive thresholding techniques to segment the video frames into different regions based on intensity levels. Global thresholding sets a fixed threshold for the entire frame, while adaptive thresholding dynamically adjusts the threshold based on local neighborhood characteristics.

3. Corner Detection: Corner detection algorithms, such as the Harris corner detector or Shi-Tomasi corner detector, are implemented to identify and mark corners within the video frames. This filter is valuable for feature extraction and object tracking.

4. Blur Filtering: The project employs various blur filters, such as Gaussian blur or median blur, to reduce noise and smooth out the video frames. Blurring can help in reducing image artifacts and enhancing image quality.

5. Using Keyboard keys to use the filters
To achieve real-time performance, the project utilizes the OpenCV library, which provides optimized functions for computer vision tasks, and NumPy for efficient numerical computations. The time library is used to measure and display the frame processing time, allowing users to evaluate the performance of different filters.

The resulting application provides a user-friendly interface with live video streaming from the webcam and interactive controls to toggle between different filters. Users can adjust filter parameters and observe the real-time effects on the video stream. The project is a great opportunity for beginners to explore computer vision concepts and gain hands-on experience with popular libraries.

Overall, the Real-Time Video Filtering project showcases the capabilities of Python, OpenCV, NumPy, and time libraries in real-time video processing and filtering. It offers an engaging and interactive environment for users to experiment and understand the impact of different filters on video frames captured by a webcam.
