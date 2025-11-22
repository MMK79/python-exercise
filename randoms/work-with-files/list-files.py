# to list everything even directories
from os import listdir

# to list only files
from os.path import isfile, join
import kagglehub
from pprint import pprint

# Download latest version
path = kagglehub.dataset_download("hojjatk/mnist-dataset")
# print("Path to dataset files:", path)

# help(os.path.join), join 2 or more paths
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# print(onlyfiles[0])
# print(type(onlyfiles[0]))
# new_lsit = [element for iterable expression condition]

# test = onlyfiles[0].split(".")
# print(test[1])

file_types = set()
for i in range(len(onlyfiles)):
    file_types.add(onlyfiles[i].split(".")[1])
print(file_types)


# print("result of only listdir()")
# pprint(listdir(path))
#
# print("result of using os.path.isfile")
# pprint(onlyfiles)
#
# print(join(path, onlyfiles[0]))
