import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import pickle 
import serial


#serial port configuration 
port = serial.SER('COM12') #import the ports compatible with windows needs the serial port, rate, COM## for Windows
port.baudrate = 9600  # set Baud rate to 9600
port.bytesize = 8   # Number of data bits = 8
port.parity  ='N'   # No parity
port.stopbits = 1   # Number of Stop bits = 1

#open video capture 
video.cv2.videocap(0)

#load the face cascade classifier 
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #needs the frontal face 


#load the trained face 
recognizer = cv2.face.LBPHFaceRecognizer_create()  # needs the face identification 
# load the trained face recognition model 
recognizer.read("trainner.yml")

# load the the trained recognition model 
with open ("labels.pickle", 'rb') as f: 
    labels = {v: k for k, v in pickle.load (f).items()} 

#while true/false statement 

while True: 
    #read frame from video capture 
    ret, frame = video.read() 
# cv2 recognizer 
# recognizer reads the yml file for face reading 
# converts frame to grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

# loads the labels for face recognition model 
#detects faces
    faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

#detect faces in the frames 
# faces detects  scale factor and and multi scale 

#for loop 
    for x, y, w, h in faces:
    # Extract the face region
    face_roi = gray[y:y+h, x:x+w]

    # Recognize the face
    face_id, confidence = recognizer.predict(face_roi)

    # Display the recognized label
    if confidence >= 20 and confidence <= 115:
        name = labels[id_]
        cv2.putText(frame, name, (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)

        # Control Arduino based on the recognized face
        if id_ == 2:
            port.write(str.encode('1'))
            print("Sent 1 to arduino")
        elif id_ == 0 or id_ == 1:
            port.write(str.encode('0'))
        print("sent '0' to Arduino")

    #draw rectangle around face 
    cv2,rectangle(frame, (x,y) (x+w, y+h), (0,255, 255), 4)
#display the video feed 
    cv2.imshow("Facial Recognition", frame)

#check for x key press to exit 
    cv2.inshow("facial recognition", frame)

    key = cv2.waitKey(1)
    if key ==ord('q'):
    break

#release video capture and close all windows 
cv2.destroyAllWindows() 
video.release() 

#video releases 
# cv2 closes windows 

