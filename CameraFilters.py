import cv2
import sys
import numpy as np
import time

PREVIEW = 0  # Preview Mode
BLUR = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY = 3  # Canny Edge Detector
adaptive_threshold = 4  # Adaptive Threshold
global_threshold = 5  # Global Threshold
feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

#Create a Var (image_filter) using in the loop check if this var equal any parameter above to active its filter 
image_filter = PREVIEW

#Create a Window name 
win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

result = None
#Capture The video from webcam
source = cv2.VideoCapture(s)
# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(source.get(3))
frame_height = int(source.get(4))

# Define the codec and create VideoWriter object to save the video 
out_mp4 = cv2.VideoWriter("CameraFilters.mp4", cv2.VideoWriter_fourcc(*"XMP4"), 30, (frame_width, frame_height))  # type: ignore

#While loop to use filter in each frame in video coming from webcam
while source.isOpened():
    has_frame, frame = source.read()
    if has_frame == True:
        if image_filter == PREVIEW:
            result = frame
            result = cv2.flip(result, 1)
            
        elif image_filter == CANNY:
            result = frame
            result = cv2.flip(result, 1)
            gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            result = cv2.Canny(result, 145, 150)

        elif image_filter == BLUR:
            result = frame
            result = cv2.flip(result, 1)
            result = cv2.blur(result, (13, 13))

        elif image_filter == FEATURES:
            result = frame
            result = cv2.flip(result, 1)
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)  # type: ignore
            if corners is not None:
                for x, y in np.float32(corners).reshape(-1, 2):
                    cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)

        elif image_filter == adaptive_threshold:
            result = frame
            result = cv2.flip(result, 1)
            frame_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

            result = cv2.adaptiveThreshold(
                frame_gray,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,
                7,
            )


        elif image_filter == global_threshold:
            result = frame
            result = cv2.flip(result, 1)
            frame_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

            retval, result = cv2.threshold(frame_gray, 100, 255, cv2.THRESH_BINARY)


        cv2.imshow(win_name, result)
        out_mp4.write(result)

        key = cv2.waitKey(1)
        if key == ord("Q") or key == ord("q") or key == 27:
            break
        elif key == ord("C") or key == ord("c"):
            image_filter = CANNY
        elif key == ord("B") or key == ord("b"):
            image_filter = BLUR
        elif key == ord("F") or key == ord("f"):
            image_filter = FEATURES
        elif key == ord("A") or key == ord("a"):
            image_filter = adaptive_threshold
        elif key == ord("G") or key == ord("g"):
            image_filter = global_threshold
        elif key == ord("P") or key == ord("p"):
            image_filter = PREVIEW
    else:
        break

source.release()
out_mp4.release()
cv2.destroyAllWindows()
