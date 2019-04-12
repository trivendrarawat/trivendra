from random import shuffle
import glob
import sys
import cv2
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

        h = http.client.HTTPConnection('github.com/googlesamples/google-photos.git')
        h.request('PUT', img_name, open(img_name, 'rb'))
        print(h.getresponse().read())
        img_counter += 1
cam.release()

cv2.destroyAllWindows()






