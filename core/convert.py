"""
Function to convert frames into a format that can displayed on a inky eWhat display
"""
from PIL import Image
from core.getFrames import getFrames
import pathlib


def convert(output_dir):
    path = pathlib.Path().absolute()
    raw_loc = str(path) + "/frames/" + output_dir + "/raw/"

    processed_loc = str(path) + "/frames/" + output_dir + "/processed/"
    frames = getFrames(raw_loc)

    for frame in frames:
        frame_out = frame.replace(".jpg", ".png")
        im = Image.open(str(raw_loc) + str(frame))
        w, h = im.size
        h_new = 300
        w_new = int((float(w) / h) * h_new)
        w_cropped = 400
        im = im.resize((w_new, h_new), resample = Image.LANCZOS)
        x0 = (w_new - w_cropped) / 2
        x1 = x0 + w_cropped
        y0 = 0
        y1 = h_new
        im = im.crop((x0, y0, x1, y1))
        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
        im = im.convert("RGB").quantize(palette = pal_img)
        im.save(str(processed_loc) + str(frame_out))

        """
        im.save("/Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + frame)
        
        os.system("convert /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/raw/" + str(
            frame) + " -dither FloydSteinberg -define dither:diffusion-amount=20% -remap  /Users/BEN/PycharmProjects/frame4frame/core/remap/eink-3color.png -type truecolor /Users/BEN/PycharmProjects/frame4frame/frames/" + str(images_out) + "/processed/" + str(
            frame_out))
        """
