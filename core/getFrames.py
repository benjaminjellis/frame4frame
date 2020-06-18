"""
Function to get list of frames in a directory so that they can read into memory
"""
from os import listdir
from os.path import isfile, join
from core.naturalSort import naturalSort
import pathlib


def getFrames(directory):
    frames = [f for f in listdir(directory) if isfile(join(directory, f))]
    naturalSort(frames)
    #remvove this, it's not a frame
    if ".DS_Store" in frames:
        frames.remove(".DS_Store")
    return frames
