def repeat_hw(n):
    """Repeat hello world for n times"""
    # While loop
    if n > 0:
        i = 0
        while i < n:
            print("Hello World \n")
            i += 1
        # For loop
        # for i in range(n):
        #     print("Hello World \n")
    else:
        if type(n) != int:
            raise TypeError("insert positive integer number")
        elif n < 0:
            raise TypeError("insert positive integer number")

print()
n = int(input("Insert a number\n"))
repeat_hw(n)
