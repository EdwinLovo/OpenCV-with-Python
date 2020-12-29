import cv2 as cv

# Works on images, videos and live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Works only in live video
def changeResolution(width, height, capture):
    capture.set(3, width)
    capture.set(4, height)


# Images Rescale
img = cv.imread('./Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)

image_resized = rescaleFrame(img, scale=0.3)
cv.imshow('Cat Resized', image_resized)
cv.waitKey(0)


# Videos Rescale
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     frame_resized = rescaleFrame(frame, scale=0.3)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()