import cv2
face_cascade = cv2.CascadeClassifier('/home/lenovo/haarcascade_frontalface.xml')

#img = cv2.imread('/home/lenovo/naman.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
cap = cv2.VideoCapture(0)


#for (x,y,w,h) in faces:
    #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cv2.imshow('img',img)


cv2.waitKey(0)
cv2.destroyAllWindows()