import cv2
import os
import math



def frameCapture(video, images_out):

    if not os.path.exists("frames"):
        os.mkdir("frames")

    if not os.path.exists("frames/" + images_out):
        os.mkdir("frames/" + images_out)

    if not os.path.exists("frames/" + images_out + "/raw"):
        os.mkdir("frames/" + images_out + "/raw")

    if not os.path.exists("frames/" + images_out + "/processed"):
        os.mkdir("frames/" + images_out + "/processed")

    vidObj = cv2.VideoCapture("videos/"+video)
    frameRate = vidObj.get(5)  #frame rate

    while (vidObj.isOpened()):
        frameId = vidObj.get(1)  #current frame number
        ret, frame = vidObj.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = "frames/" + images_out + "/raw" + "/image_" + str(int(frameId)) + ".jpg"
            cv2.imwrite(filename, frame)
    vidObj.release()
    print("done")

