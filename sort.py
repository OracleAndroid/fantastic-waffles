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
    print ("", im.size)
    src = os.getcwd()
    if im.size == [1920, 1080]: #Match Width and Height, then move to corresponding folder.
        shutil.copy((image_file),src,"1080P")
