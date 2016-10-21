import os

#Create Directories for sorting
newpath = r'/home/dave/Workspace/Projects/WallpaperSort/1080P'
if os.path.exists(newpath):
    print ("1080P Folder already exists")
if not os.path.exists(newpath):
        os.makedirs(newpath)
newpath = r'/home/dave/Workspace/Projects/WallpaperSort/OtherSize'
if os.path.exists(newpath):
    print ("OtherSize Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r'/home/dave/Workspace/Projects/WallpaperSort/Ultrawide'
if os.path.exists(newpath):
    print ("Ultrawide Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r'/home/dave/Workspace/Projects/WallpaperSort/FourByThree'
if os.path.exists(newpath):
    print ("FourByThree Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = r'/home/dave/Workspace/Projects/WallpaperSort/Phone'
if os.path.exists(newpath):
    print ("Phone Folder already exists")
if not os.path.exists(newpath):
    os.makedirs(newpath)
