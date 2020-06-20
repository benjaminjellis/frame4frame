"""
Script that will display frames on the inky wHat e ink display
"""

from PIL import Image
from core.getframes import getframes
import time
from inky import InkyWHAT
import pathlib

film_to_show = ["bladerunner", "beemov"]
path = pathlib.Path().absolute()

# set up the display
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

y = True

while y:
    # loop through the films to show
    for film in film_to_show:
        # for given filem
        frames = getframes(str(path) + "/" + film)
        for frame in frames:
            im = Image.open(str(path) + "/" + str(film) + "/" + str(frame))
            inky_display.set_image(im)
            inky_display.show()
            time.sleep(3)  # sleep for given time
