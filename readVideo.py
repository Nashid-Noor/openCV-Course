# Reading Videos
capture = cv.VideoCapture('Resources/Videos/kitten.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
