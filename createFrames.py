"""
Script that will capture frames from a given video and then convert them to be displayed on the inky wHat e ink display
"""
from core.framecapture import framecapture
from core.convert import convert


#capture frames from source video
framecapture(video = "Blade.Runner.Final.Cut.1997.mp4", output_dir = "bladerunner")

#convert to format for e ink
convert(output_dir = "bladerunner")
