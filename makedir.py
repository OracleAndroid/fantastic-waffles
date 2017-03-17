from PIL import Image
import glob
import os

#get and print current path
cpath = os.getcwd()
print ("Current directory:", cpath);

#get path from user
print ("Please input the path to folder:")
pathin = input();
if os.path.exists(pathin):
    os.chdir(pathin)
    print("Changed to path:", pathin)
if not os.path.exists(pathin):
    print("Directory not found! Create Directory? Yes(1) or No(2):")
nopath = input()
usrin = "1"
if nopath == usrin:
    os.mkdir(pathin)
    os.chdir(pathin)
else:
    quit()

#Print current path
npath = os.getcwd()
inpath = os.listdir()
print ("Current directory:", npath)
print ("Files in directory:", inpath);
input ('Press any key to create folders for images.');

#Create Directories for sorting
newpath = r"1080P"
if os.path.exists(newpath):
    print ("1080P Folder already exists")
if not os.path.exists(newpath):
        os.makedirs(newpath)
newpath = r"OtherSize"
if os.path.exists(newpath):
    print ("OtherSize Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"Ultrawide"
if os.path.exists(newpath):
    print ("Ultrawide Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"FourByThree"
if os.path.exists(newpath):
    print ("FourByThree Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r"Phone"
if os.path.exists(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
