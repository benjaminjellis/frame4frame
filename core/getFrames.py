"""
Function to get list of frames in a directory so that they can read into memory
"""
from os import listdir
from os.path import isfile, join
from core.humanSort import humanSort


def getFrames(images_out):
    frames = [f for f in listdir("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/") if
              isfile(join("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/", f))]
    humanSort(frames)
    #remvove this, it's not a frame
    if ".DS_Store" in frames:
        frames.remove(".DS_Store")

    return frames
