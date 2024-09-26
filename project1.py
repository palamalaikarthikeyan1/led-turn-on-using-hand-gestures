import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    hands, img = detector.findHands(frame)  # Detect the hand and landmarks

    if hands:
        lmList = hands[0]['lmList']  # 'lmList' gives list of hand landmarks
        fingerUp = detector.fingersUp(hands[0])  # Detect which fingers are up

        print(fingerUp)  # Debugging print to ensure fingerUp is being calculated
        cnt.led(fingerUp)  # Assuming this is a function controlling an external system

        # Display text based on fingers count
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)    
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Finger count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Finger count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA) 

    # Display the frame with the finger count
    cv2.imshow("frame", frame)

    # Break the loop if 'k' key is pressed
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

# Release the camera and destroy all windows
video.release()
cv2.destroyAllWindows()
