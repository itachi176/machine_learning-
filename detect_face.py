import cv2 
import argparse
import imutils

face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    # chuyen sang anh xam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    rects = face_cascade.detectMultiScale(gray, scaleFactor = 1.06, minNeighbors = 7, minSize = (40,40), flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        dst = 6421 / w
        dst = '%.2f' %dst
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(dst), (x, y-10), font, 1, (0, 50, 250), 1, cv2.LINE_AA)

    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
CV2.destroyAllWindows()
