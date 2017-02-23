from PIL import Image
import glob
import os
import shutil

input ('Press any key to sort.')

#Get image dimensions
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.load(image_file)
    im.size = width, height
    print("", im.size)
    src = os.getcwd
    if width("1920"):
        shutil.move(src,'1080P')
