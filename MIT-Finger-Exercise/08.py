def uniqe_char(s):
    s_l = []
    for i in s:
        if i not in s_l:
            s_l.append(i)
    s_l.sort()
    return s_l

def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    return uniqe_char(s1) == uniqe_char(s2)


# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False
