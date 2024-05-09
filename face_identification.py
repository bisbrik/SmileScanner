#import OpenCV
import cv2

camera = cv2.VideoCapture(0)

# load xml file with pre-coded instructions
case = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#camera loop
while True:
    check,frame = camera.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = case.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 6)

    for x,y,w,h in face:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 3)
                              
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
