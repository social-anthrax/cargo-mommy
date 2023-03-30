#! /usr/bin/env python3
import glob
import os

files = glob.glob("./*")
files.remove("./" + os.path.basename(__file__))
for file in files:
    file_name = os.path.basename(file)
    try:
        os.remove(f"../.git/hooks/{file_name}")
    except:
        pass
    os.symlink(f"../../hooks/{file_name}", f"../.git/hooks/{file_name}")
