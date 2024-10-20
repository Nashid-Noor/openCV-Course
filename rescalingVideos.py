import cv2 as cv

def rescaleFrame(img,scale=0.75):
    height = int(img.shape[0]*scale)
    width = int(img.shape[1]*scale)
    dimension = (width,height)

    return cv.resize(img,dimension,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue,Frame = capture.read()
    cv.imshow('Video', Frame) # here we have cv.imshow because we are repeteadly showing images i.e. frames making it to be video.
    rescaledVideo = rescaleFrame(Frame)
    cv.imshow('Video Rescaled', rescaledVideo)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
