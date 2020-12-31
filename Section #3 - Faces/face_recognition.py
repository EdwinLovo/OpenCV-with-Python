import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('./Resources/haar_cascades/haar_face.xml')

people = ['Ben Afflek', 'Elton John',
          'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('./Resources/OpenCVModel/features.npy')
# labels = np.load('./Resources/OpenCVModel/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('./Resources/OpenCVModel/face_train.yml')

img = cv.imread(r'./Resources/Faces/val/madonna/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print('Label = {} with a confidence of {}'.format(
        people[label], confidence))

    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow('Detected Face', img)

cv.waitKey(0)
