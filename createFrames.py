"""
Script that will capture frames from a given video and then convert them to be displayed on the inky wHat e ink display
"""
from core.frameCapture import frameCapture
from core.convert import convert


#capture frames from source video
frameCapture(video = "Bee.Movie.2007.mp4", images_out = "beemov")

#convert to format for e ink
convert(images_out = "beemov")
