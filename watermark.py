#!/usr/bin/env python

import os
import glob

from PIL import Image


def main():
    wm = Image.open('watermark.png')
    for infile in glob.glob("*.png"):
        f, ext = os.path.splitext(infile)
        if f == "watermark":
            continue
        im = Image.open(infile)
        if im.mode != "RGBA":
            im = im.convert("RGBA")
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
        position = (im.size[0] - wm.size[0], im.size[1] - wm.size[1])
        layer.paste(wm, position)
        Image.composite(layer, im, layer).save('%s.wm.%s' % (f, ext))

if __name__ == "__main__":
    main()
