import cv2
vidcap = cv2.VideoCapture('Прорыв Феттеля с последнего до 4-го места Малайзия - 2017.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*15000))
    cv2.imwrite("jpg\\frame%d.jpg" % count, image) 
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1