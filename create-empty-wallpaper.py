#!/usr/bin/env python

from PIL import Image

def main():
    im = Image.new('RGB', (1920, 1080), (32, 32, 32, 255))
    im.save('/home/cenan/Pictures/out.png')
    return

if __name__ == "__main__":
	main()


