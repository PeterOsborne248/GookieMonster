from deepface import DeepFace
import matplotlib.pyplot as plt
import time
import cv2
import json
import pyserial

cap = cv2.VideoCapture(0)
i = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    time.sleep(3)

    obj = DeepFace.analyze(img_path = "Frame"+str(i)+".jpg", enforce_detection=False)
    print(obj)

    race = obj['dominant_race']
    print(race)


    time.sleep(1)
    i += 1

    print(pyserial)


cap.release()
cv2.destroyAllWindows()























#k=0
#try:
#    def detectRace(k):
#        obj = DeepFace.analyze(img_path = "Frame"+str(k)+".jpg", enforce_detection=False)
#        print(obj)
#        print(k)
#
#    while True:
#        time.sleep(3)
#        detectRace(k)
#        k+=1
#
#
#except:
#    print("max photos")














#img1_path = some URL                                                          #img URL link

#Function raceDetector(img1_path)

    #img1 = DeepFace.detectFace(img1_path, enforce_detection=False)            #Detect face
    #plt.imshow(img1)                                                          #Show face crop

    #model_name_VGG = 'VGG-Face'                                               #Model being used

    #obj = DeepFace.analyze(img_path = img1_path, enforce_detection=False)     #Analyse face img

    #Return(    Race Element    )                                              #Return the race


