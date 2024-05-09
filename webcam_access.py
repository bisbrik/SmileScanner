# imports the opencv library
import cv2

# creates an object for video capture
camera = cv2.VideoCapture(0)

# enters an infinite while looo
while True:
    check,frame = camera.read()

    cv2.imshow("Video", frame)
    
    escKey = cv2.waitKey(1)
    if(escKey == ord('q')):
        break

camera.release()

cv2.destroyAllWindows()
