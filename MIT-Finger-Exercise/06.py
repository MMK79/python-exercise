def guess_check_bisection(N, detail = False):
    """
    bisection search to guess a number
    N is an integer lower than 1000
    """
    low = 0
    high = 1000
    guess = ( high + low )//2
    count = 0
    while guess != N:
        if N > guess:
            low = guess
            guess = ( high + low )//2
            count += 1
            if detail == True:
                print(f"your low point is {low}, your high point is {high}, and your guess is {guess} in {count}")
        else:
            high = guess
            guess = ( high + low )//2
            count += 1
            if detail == True:
                print(f"your low point is {low}, your high point is {high}, and your guess is {guess} in {count}")
    return (guess, count)

print()
n = int(input("Enter your number\n"))
guess, count = guess_check_bisection(n, True)
print(f"We guess your number is {guess} and we achieve it with {count} of guess")
