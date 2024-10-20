import cv2 as cv


def rescaleFrame(img,scale=0.75):
    height = int(img.shape[0]*scale)
    width = int(img.shape[1]*scale)
    dimension = (width,height)

    return cv.resize(img,dimension,interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)
resizedImage = rescaleFrame(img)
cv.imshow('Resized Cat',resizedImage)


cv.waitKey(0)

