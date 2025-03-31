import os
from os.path import join

def make_paths(*filenames):
    base_path=os.getcwd()
    path = join(base_path,*filenames)
    return path
