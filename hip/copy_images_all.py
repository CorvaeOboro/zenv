# copy images in subfolders , one deep to 

import os
import shutil
import glob
import pathlib


# for each folder , excluding images
# glob images
# copy images to images folder

#//==========================================
local_folders = []
rootdir = os.path.dirname(os.path.abspath(__file__))
print("ROOT DIR = " + str(rootdir))
#target_folder = rootdir + "/images"
target_folder = os.path.join(rootdir, "images")
print("TARGET DIR = " + str(target_folder))
if os.path.exists(target_folder):
    shutil.rmtree(target_folder)
if not os.path.exists(target_folder):
    os.mkdir(target_folder,0o666)

#//==========================================
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        local_folders.append(d)

#//==========================================
print("LOCAL FOLDERS = ")
print(local_folders)
for local_folder in local_folders:
    local_absolute = os.path.abspath(local_folder+"/")
    print(local_absolute)
    if local_absolute is not target_folder:
        local_images = glob.glob(local_absolute + '/*.jpg') + glob.glob(local_absolute + '/*.png')
        for name in local_images:
            local_file = pathlib.PurePath(str(name)).name
            print(name + " >>>> " + target_folder + "/" + local_file)
            target_file = target_folder + "/" + local_file
            if not os.path.exists(target_file):
                shutil.copy(name, target_file)
