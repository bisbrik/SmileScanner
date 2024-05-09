import cv2
from deepface import DeepFace # library for expression recognition
import matplotlib.pyplot as plt
import pickle 
import serial


#serial port configuration 
port = serial.Serial('COM12') #import the ports compatible with windows needs the serial port, rate, COM## for Windows
port.baudrate = 9600  # set Baud rate to 9600
port.bytesize = 8   # Number of data bits = 8
port.parity  ='N'   # No parity
port.stopbits = 1   # Number of Stop bits = 1

#open video capture 
video = cv2.VideoCapture(0)

#load the face cascade classifier 
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #needs the frontal face 


#load the trained face 
recognizer = cv2.face.LBPHFaceRecognizer_create()  # needs the face identification 
# load the trained face recognition model 
recognizer.read("C:/Users/Patrick/Documents/_speedhacks24/python/trainer.yml")

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
    face = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

#detect faces in the frames 
# faces detects  scale factor and and multi scale 
    '''
    for x, y, w, h in faces:
        # Extract face ROI
        face_roi = frame[y:y+h, x:x+w]
        print(face_roi)
        
        try:
            prediction = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

            happy = prediction['emotion']['happy']
            sad = prediction['emotion']['sad']
            print("Happy : ", happy, " Sad: ", sad)

            # Display emotion if confidence is within threshold
            if happy > 50 or sad > 50:
                # Control Arduino based on recognized face
                if happy > 50:
                    port.write(b'1')
                    print("Sent '1' to Arduino")
                elif sad > 50:
                    port.write(b'2')
                    print("Sent '2' to Arduino")
            else:
                port.write(b'0')        
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 4)
        except Exception as e:
            print("Error in DeepFace Analysis:", e)

    # Display video feed
    cv2.imshow("Facial Recognition", frame)

    # Check for quit key
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    '''

    for x,y,w,h in face:
        face_save = gray[y:y+h, x:x+w]
        
        # Predicting the face identified
        ID, conf = recognizer.predict(face_save)
        #print(ID,conf)
        if conf >= 20 and conf <= 115:
            print(ID)
            print(labels[ID])
            cv2.putText(frame,labels[ID],(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX ,1, (18,5,255), 2, cv2.LINE_AA )
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,255),4)

    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
    

#release video capture and close all windows 
cv2.destroyAllWindows() 
video.release() 

#video releases 
# cv2 closes windows 

