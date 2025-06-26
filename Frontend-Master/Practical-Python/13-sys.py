import sys

arguments = sys.argv
print(f"We receieved the following argument:")

for arg in arguments:
    print(f' - {arg}')

print(f"We are running {sys.platform} machine")
