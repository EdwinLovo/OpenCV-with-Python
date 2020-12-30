import cv2 as cv
import numpy as np

# Blank Image generation
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (10, 10), (250, 250), (0, 255, 0), thickness=1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2,
#                   blank.shape[0]//2), 40, (0, 0, 255), thickness=1)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (0, 0), (blank.shape[1]//2,
#                         blank.shape[0]//2), (255, 0, 0), thickness=1)
# cv.imshow('Line', blank)

# 5. Draw text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)


# Reading images
# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)
