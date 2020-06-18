"""
Script that will display frames on the inky wHat e ink display
"""

from PIL import Image
from core.getFrames import getFrames
import time
from inky import InkyWHAT
import pathlib

film_to_show = "beemov"
path = pathlib.Path().absolute()

#set up the display
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

#get the frames
frames = getFrames(str(path) + "/" + film_to_show)

y = True


while y:
    for frame in frames:

        im = Image.open(str(path) + str(film_to_show) + "/" + str(frame))
        inky_display.set_image(im)
        inky_display.show()
        time.sleep(2)  #sleep for 5 mins
