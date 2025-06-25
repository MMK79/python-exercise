# uncaught exception cause your program to exit
# int("a")
# print("end of the program!")

# catch exception
# try:
#     int("a")
# except:
#     print('An exception happend!')
#
# print("end of the program!")

# We can be more specific with our exceptions
# try:
#     int("a")
# except ValueError:
#     print('An exception happend!')
#
# print("end of the program!")

# multiple exceptions
# try:
#     d = {}
#     d["a"]
#     int("a")
# except KeyError:
#     print('Something happend with dictionary!')
# When we get the first error in try block, we throw exception for it, and then we don't continue running try block
# except ValueError:
#     print('An exception happend!')
#
# print("end of the program!")

try:
    d = {}
    d["a"]
except KeyError:
    print('Something happend with dictionary!')
try:
    int("a")
except ValueError:
    print('An exception happend!')

print("end of the program!")
