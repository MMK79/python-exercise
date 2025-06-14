def psz(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

print()
number = int(input("Enter your number \n"))
if type(number) != int:
    raise TypeError("Enter Int only")
psz(number)
print()

