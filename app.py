import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime

path = 'people'
image=[]
names=[]
nameList=[]
list=os.listdir(path)

#print(list)

for cl in list:
    Img= cv2.imread(f'{path}/{cl}')
    image.append(Img)
    names.append(os.path.splitext(cl)[0])
#print(names)

def Encode(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAtt(name):
    
    with open ('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList=[]
        
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            #print(nameList)
        if name not in nameList:
            now= datetime.now()
            dtString=now.strftime('%H:%M:%S')
            
            f.writelines(f'\n{name},{dtString}')
    


encodeList = Encode(image)
print("Done")

cap = cv2.VideoCapture(0)

while True:
    success, img= cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame =  face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeList,encodeFace)
        faceDis = face_recognition.face_distance(encodeList,encodeFace)
       # print(faceDis) 
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name=names[matchIndex].upper()
            y1,x2,y2,x1= faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255,2))
            markAtt(name)
        else:
            y1,x2,y2,x1= faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,"NPC",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255,2))
            


            

    cv2.imshow('webcam',img)
    cv2.waitKey(1)


