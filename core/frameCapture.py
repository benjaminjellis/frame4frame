"""
Module to capture frames form a video
"""

import cv2
import os


def frameCapture(video, images_out):

    if not os.path.exists("frames"):
        os.mkdir("frames")

    if not os.path.exists("frames/" + images_out):
        os.mkdir("frames/" + images_out)

    if not os.path.exists("frames/" + images_out + "/raw"):
        os.mkdir("frames/" + images_out + "/raw")

    if not os.path.exists("frames/" + images_out + "/processed"):
        os.mkdir("frames/" + images_out + "/processed")

    vidcap = cv2.VideoCapture("videos/"+video)
    count = 0
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    im_no = 0
    while success:
        success, image = vidcap.read()
        if count % (5 * fps) == 0:
            filename = "frames/" + images_out + "/raw" + "/image_" + str(int(im_no)) + ".jpg"
            cv2.imwrite(filename, image)
            im_no += 1
        count += 1
