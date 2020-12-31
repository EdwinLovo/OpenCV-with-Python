import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# 1. Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

# 2. Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# 3. Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# 4. Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
