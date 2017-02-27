from PIL import Image
import glob
import os
import shutil
import time

input ("Press any key to sort.")

#Get image dimensions
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    width = im.width()
    height = im.height()
    print ("", im.width, im.height)
    src = os.getcwd
#Match Width and Height, then move to corresponding folder.
    if width("1080"):
        shutil.move(src,"1080P")
