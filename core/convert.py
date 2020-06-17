"""
Function to convert frames into a format that can displayed on a inky eWhat display
"""
from PIL import Image
from core.getFrames import getFrames

def convert(images_out):
    frames = getFrames(images_out)
    for frame in frames:
        frame_out = frame.replace(".jpg", ".png")
        im = Image.open("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + str(
            frame))
        im = im.resize((400,300), Image.ANTIALIAS)
        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
        im = im.convert("RGB").quantize(palette = pal_img)
        im.save("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/processed/" + str(
            frame_out))

        """
        im.save("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + frame)
        
        os.system("convert /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + str(
            frame) + " -dither FloydSteinberg -define dither:diffusion-amount=20% -remap  /Users/BEN/PycharmProjects/frame4frame/core/remap/eink-3color.png -type truecolor /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/processed/" + str(
            frame_out))
        """
