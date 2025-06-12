def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    count = 0
    L_new = []
    for i in L:
        if type(i) == list:
            for j in i:
                L_new.append(j)
        else:
            L_new.append(i)
    for i in range(len(L_new)):
        print(L_new[i])
        if type(L_new[i]) != str:
            raise ValueError(f"Your value is not a string, it is {type(L_new[i])}")
        count += len(L_new[i])
    return count

# Unit-test:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError
