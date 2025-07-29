n = 1000
mabna_2 = ''
while n > 2:
    reminder = n%2
    quotient = n//2
    mabna_2 = str(reminder) + mabna_2
    n = quotient

if n <= 2:
    reminder = n%2
    quotient = n//2
    if quotient != 1:
        mabna_2 = str(reminder) + mabna_2
    else:
        mabna_2 = str(quotient) + str(reminder) + mabna_2

print(mabna_2)
