import cv2 as cv

# Reading Images

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)

cv.waitKey(0)

# Check if a key was pressed
if key == ord('q'): # Check if 'q' key was pressed
  print("You pressed the 'q' key.")

