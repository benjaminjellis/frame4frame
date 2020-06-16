from os import listdir
from os.path import isfile, join
from core.human_sort import sort_nicely
import os

def convert(images_out):
    frames = [f for f in listdir("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/") if
              isfile(join("/Users/BEN/PycharmProjects/frame4frame/frames/"+ str(images_out) + "/raw/", f))]
    sort_nicely(frames)

    for frame in frames:
        frame_out = frame.replace(".jpg", ".bmp")
        os.system("convert /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + str(
            frame) + " -dither FloydSteinberg -define dither:diffusion-amount=75% -remap  /Users/BEN/PycharmProjects/frame4frame/core/remap/eink-3color.png -type truecolor /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/processed/" + str(
            frame_out))
