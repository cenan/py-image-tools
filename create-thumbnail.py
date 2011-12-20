#!/usr/bin/env python

import glob, os
from PIL import Image

def main():
	for infile in glob.glob("*.jpg"):
		file, ext = os.path.splitext(infile)
		im = Image.open(infile)
		im.thumbnail((200, 200), Image.ANTIALIAS)
		im.save(file + ".thumb" + ext)

if __name__ == "__main__":
	main()

