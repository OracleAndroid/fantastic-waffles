from PIL import Image
import glob, os

input ('Press any key to sort.')

for image_file in glob.glob("*.*g"):
    file, ext = os.path.splitext(image_file)
    im = Image.open(image_file)
    print ("", im.size)
