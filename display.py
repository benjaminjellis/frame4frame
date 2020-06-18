"""
Script that will display frames on the inky wHat e ink display
"""

from PIL import Image
from core.getFrames import getFrames
import time
from inky import InkyWHAT

film_to_show = "beemov"

#set up the display
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

#get the frames
frames = getFrames(film_to_show)

y = True

while y:
    #loop through the frames in the dir
    for frame in frames:
        #open a frame
        im = Image.open("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(film_to_show) + "/raw/" + str(
                frame))
        #push the frame to the display
        inky_display.set_image(im)
        inky_display.show()
        time.sleep(5*60) #sleep for 5 mins
