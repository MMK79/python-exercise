def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        # Complexity = a
        product *= i
        # Complexity in best case, product be equal in the first step = 1
        # Complexity in the worst case, product be equal in the last step = a
        if product == a:
            return True
    return False
# Overall Complexity = \Theta(n)
def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        # Complexity = len(L) = n
        if e1 in L2:
            # Complexity = len(L) = n
            inL = True
    # Overall complexity with multiplication law = n^2
    inL2 = False
    for e2 in L2:
        # Complexity = len(L) = n
        if e2 in L:
            # Complexity = len(L) = n
            inL2 = True
    # Overall complexity with multiplication law = n^2
    return inL and inL2
# Overall complexity with multiplication law = 2*n^2 = \Theta n^2
def sum_f(n):
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer
# Complexity = \Theta(log(n))
