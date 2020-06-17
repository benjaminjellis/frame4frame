"""
Module to capture frames form a video
"""

import cv2
import os


def frameCapture(video, output_dir):

    if not os.path.exists("frames"):
        os.mkdir("frames")

    if not os.path.exists("frames/" + output_dir):
        os.mkdir("frames/" + output_dir)

    if not os.path.exists("frames/" + output_dir + "/raw"):
        os.mkdir("frames/" + output_dir + "/raw")

    if not os.path.exists("frames/" + output_dir + "/processed"):
        os.mkdir("frames/" + output_dir + "/processed")

    vidcap = cv2.VideoCapture("videos/"+video)
    count = 0
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    im_no = 0
    while success:
        success, image = vidcap.read()
        if count % (5 * fps) == 0:
            filename = "frames/" + output_dir + "/raw" + "/image_" + str(int(im_no)) + ".jpg"
            cv2.imwrite(filename, image)
            im_no += 1
        count += 1
