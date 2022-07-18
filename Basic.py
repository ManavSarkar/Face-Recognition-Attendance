import cv2
import numpy as np
import face_recognition

#Convert images from BGR to RBG
imgBasic = face_recognition.load_image_file('BasicImages/BillGates.jpg')
imgBasic = cv2.cvtColor(imgBasic,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('TestImages/MukeshAmbani.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLocBasic = face_recognition.face_locations(imgBasic)[0]
encodeBasic = face_recognition.face_encodings(imgBasic)[0]
cv2.rectangle(imgBasic,(faceLocBasic[3],faceLocBasic[0]),(faceLocBasic[1],faceLocBasic[2]),(255,0,245),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,245),2)

results = face_recognition.compare_faces([encodeBasic],encodeTest)
print(results)

faceDistance = face_recognition.face_distance([encodeBasic],encodeTest)
print("Face Distance: ",faceDistance)

cv2.putText(imgTest,f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)

cv2.imshow('Image Basic',imgBasic)
cv2.imshow('Image Test',imgTest)

cv2.waitKey(0)