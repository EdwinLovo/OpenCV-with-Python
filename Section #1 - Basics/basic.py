import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

# 1. Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur an image (reduce some noise)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# 4. Edge Cascade (with edges reduced)
cannyFromBlur = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges reduced', cannyFromBlur)

# 5. Dilating the image
dilated = cv.dilate(cannyFromBlur, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 6. Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)

# 7. Resize ignoring the aspect ratio
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 8. Cropping
cropped = img[50: 200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
