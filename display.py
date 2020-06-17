"""
Script that will display frames from a given video on the inky wHat e ink display
"""
from PIL import Image
from core.getFrames import getFrames
import inky

#get the frames
images_out = "sopr"
frames = getFrames(images_out =images_out )
for frame in frames:
    im = Image.open("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + str(
            frame))
    inky_display.set_image(img)
    inky_display.show()