import os
import sys
from os import listdir
from os.path import isfile, join


def script_directory():
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    return directory


def delete_dsstore():
    extra_file = ".DS_Store"
    path, onlyfiles, _ = get_files()
    if extra_file in onlyfiles:
        os.remove(join(path, ".DS_Store"))


def get_files(path=script_directory()):
    path = r"/Volumes/ADATA HD330/Courses/Downloads/FrontendMaster Courses/"
    ls = listdir(path)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    folders = list(set(ls) - set(files))
    return path, files, folders


def name_changer(path, folders_name: list):
    for folder_name in folders_name:
        src = join(path, folder_name)
        if folder_name.find("_"):
            splits = folder_name.split("_")
        else:
            splits = folder_name.split(" ")
        try:
            splits.remove("Downloadly")
        except:
            pass
        finally:
            count = 0
            for split in splits:
                stop_words = ["of", "with"]
                if split not in stop_words:
                    split[0].upper()
                    split = split[0].upper() + split[1:]
                    splits[count] = split
                count += 1
            changed_name = " ".join(splits)
            if changed_name.find("-") != -1:
                changed_name = changed_name.split("-")
                changed_name.pop()
                changed_name = "".join(changed_name)
            dest = join(path, changed_name)
            try:
                os.rename(src, dest)
            except:
                pass


path, files, folders = get_files()
name_changer(path, folders)
