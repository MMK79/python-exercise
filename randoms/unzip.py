import os
from os.path import join
import zipfile

name_of_zipfile = "hello.zip"
with zipfile.ZipFile(join(os.getcwd(), name_of_zipfile), "r") as zip_ref:
    zip_ref.extractall(os.getcwd())
