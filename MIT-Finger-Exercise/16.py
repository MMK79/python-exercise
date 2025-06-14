def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    for i in range(len(L)):
        if type(L[i]) != list:
            L_copy.append(L[i])
        else:
            flatten(L[i])
    return L_copy

L_copy = []
# Unit-test:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L) == [1,4,6,2,3,2,4,5])
