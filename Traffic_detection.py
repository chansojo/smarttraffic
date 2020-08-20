import cv2
from gtts import gTTS
import os

cascade_src = 'cars.xml'
video_src = 'dataset/video1.avi'
# video_src = 'dataset/traffic.avi'
# video_src = 'dataset/video2.avi'
# video_src = 'dataset/New video_Small.mp4'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
count = 0
while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break
    count += 1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video', img)

    if cv2.waitKey(20) == 20:
        break

cv2.destroyAllWindows()
f = open("Output.txt", "w+")
if count < 501:
    f.write("N")
    tts = gTTS(text='There is no traffic, continue on the same route', lang='en')
    tts.save("Speak.mp3")
    os.system("Speak.mp3")
else:
    f.write("t")
    tts = gTTS(text='There is traffic, choose an alternate route', lang='en')
    tts.save("Speak.mp3")
    os.system("Speak.mp3")

f.close()
