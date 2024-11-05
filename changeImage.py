#!/usr/bin/env python3
"""In this script, we will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

Size: Change image resolution from 3000x2000 to 600x400 pixel

Format: Change image format from .TIFF to .JPEG

"""
from PIL import Image
import os
path = "./supplier-data/images/"
for f in os.listdir("./supplier-data/images"):
    if f.endswith(".tiff"):
        split_f = f.split(".")
        name = split_f[0] + ".jpeg"
        im = Image.open(path + f).convert("RGB")
        im.resize((600, 400)).save("./supplier-data/images/" + name, "JPEG")
