import cv2
import pickle##
import serial

# Setting serial port to COM4 at bard rate of 9600
port = serial.Serial('COM12',9600)

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainer.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    og_label = pickle.load(f)
    labels = {v:k for k,v in og_label.items()}
    print(labels)


sampleno = 0

while True:
    check,frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
    #print(face)

    for x,y,w,h in face:
        face_save = gray[y:y+h, x:x+w]

        ID, conf = recognise.predict(face_save)
        #print(ID,conf)
        if conf >= 20 and conf <= 115:
            port.write(1)

        else:
            port.write(0)
            break
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)

    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
