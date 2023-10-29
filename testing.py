import cv2
import time

cap = cv2.VideoCapture(0)

seconds = 4

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    if cv2.waitKey(1) == 32:
        print("space pressed")
        for i in range (1000000000000):
            cv2.putText(frame, "text", (200, 100), 0, 3, (255, 0, 0), 5)
            cv2.imshow("Frame", frame)

    cv2.imshow("Frame", frame)       
    if cv2.waitKey(1) == 27:
        break   