#!/usr/bin/env python

import glob
import os
from PIL import Image


def main():
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.crop((0, 0, 240, 320)).save(file + ".1.jpg", "JPEG")
        im.crop((240, 0, 480, 320)).save(file + ".2.jpg", "JPEG")
        im.crop((480, 0, 720, 320)).save(file + ".3.jpg", "JPEG")

if __name__ == "__main__":
    main()
