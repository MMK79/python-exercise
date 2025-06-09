import time

def cube(N, inc = 0.1, eps = 0.1):
    """
    N positive int number
    inc is a increament
    eps is our epsilon, our error bound 
    return the cube root of a N
    """
    count = 0
    b_guess = 0
    while abs( N - b_guess**3 )> eps:
        if b_guess**3 == N:
            print(f"Your number is perfect cube of {b_guess}")
            return None
        elif b_guess**3 > N:
            b_guess -= inc
            count += 1
        else:
            b_guess += inc
            count += 1
    print(f"Your number is not a perfect cube but its cube root is around {b_guess} with {count} of guess")
    return None

def binary_cube(N, eps = 0.1, counter = 1000):
    """
    binary version of finding cube root
    """
    count = 0
    low = 0
    high = N/2
    guess = ( low + high )/2
    while abs( N - guess**3 ) > eps and count < counter:
        if guess**3 == N:
            print(f"Your number is perfect cube of {guess}")
            return None
        elif guess**3 > N:
            high = guess/2
            count += 1
        else:
            low = guess/2
            count += 1
    print(f"Your number is not a perfect cube but its cube root is around {guess} with {count} of guess")
    return None

def func_perf(N, func):
    t0 = time.perf_counter()
    func(N)
    td = time.perf_counter() - t0
    print(f"for function of {func} with input {N} it took {td} sec")
    return None

print()
N = int(input("Enter a positive integer Number \n"))

assert N > 0,"Positive integer"
func_perf(N, cube)
func_perf(N, binary_cube)
