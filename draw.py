import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# 1.) Paint the image a certain color.

blank[200:500,300:400]=0,0,255
cv.imshow('Blank1',blank)

# 2.) Draw a Rectangle

#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=5) #thickness gives the border
# when thickeness if cv.filled or -1 , it basically fills the shape with the specified color.
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) # instead of cv.filled we can also specify -1.

cv.imshow('Blank2',blank)


# 3.) Draw a Circle

cv.circle(blank,(250,250),40,(0,0,255),thickness=9)

cv.imshow('Blank3',blank)

# 4.) Draw a line

cv.line(blank,(0,0),(250,250),(255,0,0),thickness=2)
cv.imshow('Blank4',blank)

# 5.) Draw a Text

cv.putText(blank,"Hello my name's Nashid",(0,250),cv.FONT_HERSHEY_SCRIPT_COMPLEX,2.0,(0,130,0),10)
# Here is cv.font is the font style while 2.0 is font scale, then its the color and finally its the thickness.
cv.imshow('Blank5', blank)


cv.waitKey(0)
