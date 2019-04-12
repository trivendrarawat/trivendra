from random import shuffle
import glob
import sys
import cv2
import requests
import os
import http.client
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        image_path=os.path.dirname(os.path.abspath(__file__))
        
        multipart_form_data = {
            'image': (img_name, open(image_path, 'rb')),

        }

        response = requests.post('http://www.example.com/api/v1/sensor_data/',
                         files=multipart_form_data)

        print(response.status_code)
        img_counter += 1
cam.release()

cv2.destroyAllWindows()












