from PIL import Image
import glob
import os
import shutil

input ('Press any key to sort.')

#Get image dimensions
for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    print ("", im.width, im.height)
    width = im.width
    height = im.height
    src = os.getcwd
#Match Width and Height, then move to corresponding folder.
    if width('1920'):
        shutil.move(src,'1080P')
