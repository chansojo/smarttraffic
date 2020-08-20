import cv2
import numpy as np
import time
 
cap = cv2.VideoCapture("highway.mp4")
 
'''_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
time.sleep(2)
_, second_frame=cap.read()
second_gray = cv2.cvtColor(second_frame, cv2.COLOR_BGR2GRAY)
second_gray = cv2.GaussianBlur(second_gray, (5, 5), 0)'''
 
while (cap.isOpened()):
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
 
    _, first_frame = cap.read()
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
    time.sleep(1)
    _, second_frame=cap.read()
    second_gray = cv2.cvtColor(second_frame, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.GaussianBlur(second_gray, (5, 5), 0)

    difference = cv2.absdiff(first_gray, second_gray)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    
    difference1 = cv2.absdiff(first_gray, gray_frame)
    _, difference1 = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("First frame", first_frame)
    '''cv2.imshow("Frame", frame)'''
    cv2.imshow("difference", difference)
    cv2.imshow("difference1", difference1)
    cv2.imshow("Second Frame", second_frame)
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()