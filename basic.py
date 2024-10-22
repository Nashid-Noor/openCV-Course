import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

# Converting to GrayScale.
Grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',Grey)

# Blur
blur = cv.GaussianBlur(img,(33,33),cv.BORDER_DEFAULT) # The kernel should be an odd number.
cv.imshow('Blur',blur)

# Edge Cascade

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

# Dilating

dilate = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilate',dilate)

# Eroding

erode = cv.erode(dilate,(7,7),iterations=3)
cv.imshow('Erode',erode)

# Resizing

resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resize)
# cv.INTER_AREA is used when we are trying to shrink the image
# cv.INTER_LINEAR or cv.INTER_CUBIC are used while enlarging the image.
# INTER_CUBIC is the slowest transformation but the resultant quality is the highest.


# crop

cropped = img[300:400,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)