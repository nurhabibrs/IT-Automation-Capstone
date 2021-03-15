#! /usr/bin/env python3
from PIL import Image
import os, glob

size = (128, 128)

for files in glob.glob("ic_*"):
  img = Image.open(files).convert('RGB')
  result = img.rotate(270).resize(size)
  result.save("/opt/icons/" + files, "JPEG")
