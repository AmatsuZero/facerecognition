## Original source from here:
## https://realpython.com/face-detection-in-python-using-a-webcam/

import time
import os
import cv2

video_capture = cv2.VideoCapture(0)
folder = os.path.dirname(os.path.realpath(__file__))
folder = os.path.join(folder, "images/")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        print("Exiting...")
        break
    if key  == ord('s'):
        timestr = time.strftime("%Y-%m-%d %H:%M:%S")
        print("Saving image: "+timestr + ".jpeg")
        filename = folder + timestr + ".jpeg"
        if not cv2.imwrite(filename, frame):
            print("Error saving image")
    if key == 13: ## enter key
        timestr = time.strftime("%Y-%m-%d %H:%M:%S")
        print("Saving image: "+timestr + ".jpeg")
        filename = folder + timestr + ".jpeg"
        cv2.imwrite(filename, frame)

video_capture.release()
cv2.destroyAllWindows()