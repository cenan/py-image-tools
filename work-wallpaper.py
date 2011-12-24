#!/usr/bin/env python

import os
from PIL import Image, ImageDraw, ImageFont

WALLPAPER = '/home/cenan/Pictures/wallpaper.png'

def main():
    im = Image.new('RGB', (1920, 1080), (32, 32, 32, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("/home/cenan/HelveticaNeueLight.ttf", 196)
    draw.text((700, 400), "work!", (255, 255, 255), font=font)
    im.save(WALLPAPER)
    if open("/etc/issue").read().startswith("Linux Mint 11 LXDE"):
        os.system('pcmanfm --set-wallpaper "%s"' % WALLPAPER)

if __name__ == "__main__":
	main()


