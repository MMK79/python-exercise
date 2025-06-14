def sum_total(a, b, c):
    """
    inputs are int
    a and b will add to each other
    then multiply by c
    return total
    """
    return (a+b)*c

print()
a = int(input("Enter your first number \n"))
print()
b = int(input("Enter your second number \n"))
print()
c = int(input("Enter your third number \n"))

assert type(a) and type(b) and type(c) == int,"Should enter Integer"
print(sum_total(a, b, c))
