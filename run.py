#! /usr/bin/env python3
"""In this script, we process the text files from the supplier-data directory and turn the data into a JSON dictionary by adding all the required fields,
 including the image associated with the fruit (image_name), and upload it to http://[external-IP-address]/fruits using the Python requests library."""
import os
import requests
fruits = {}
keys = ["name", "weight", "description", "image_name"]
index = 0
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"
for file in os.listdir("./supplier-data/descriptions"):
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if "lbs" in line:
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except:
                    fruits[keys[2]] = line
        index = 0
        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        for fle in os.listdir("./supplier-data/images"):
            if fle == name:
                fruits["image_name"] = name
        response = requests.post("http://<External_IP>/fruits/", json=fruits)
        fruits.clear()
