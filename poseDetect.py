import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
cap = cv2.VideoCapture("video.mp4")


Pose = mpPose.Pose() #mediapipe func used for pose estimation
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    cv2.resize(img, (720, 405))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(imgRGB)



    if results.pose_landmarks:
            for id, lms in enumerate(results.pose_landmarks.landmark): # gives numbers
                h, w , c = img.shape
                cx,cy = int(lms.x * w) , int(lms.y * h)
                print(id, cx ,cy)
                cv2.circle(img, (cx,cy), 6 , (255,0,0), cv2.FILLED)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
