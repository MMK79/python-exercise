
## EXTRA CONTENT: towers of hanoi
def print_move(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

# towers(4, 'a', 'b', 'c')


###########################################
########## ANSWERS TO YOU TRY IT #############
###########################################

def total_len_recur(L):
    """ Returns the total length of all strings inside L """
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])

# test = ["ab", "c", "defgh"]
# print(total_len_recur(test))  # should print 8

def in_lists_of_list(L, e):
    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within sublists of L
    and False otherwise. 
    """
    if len(L) == 1:
        return e in L[0]
    else:
        if e in L[0]:
            return True
        else:
            return in_lists_of_list(L[1:], e)


# test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 3))  # prints True

# test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 0))  # prints False


######################################################
################### AT HOME ##############
######################################################
# Q1. Memoize the code to find possible scores in basketball
def score_count(x, d):
    pass
    
d = {1:1, 2:2, 3:3}
# print(score_count(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431

# Q2. 
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or 
    sublists of L and False otherwise. 
    """
    # your code here


# test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False

# Q3. 
def my_deepcopy(L):
    """ 
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that 
    contains copies (recursively) of every sublist 
    """
    # your code here

# myL = ["abc", ['d'], ['e', ['f', 'g']]]
# my_newL = my_deepcopy(myL)
# print(myL)
# print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]


# Q4. Here are 3 recursive functions that are incorrectly implemented.
# Debug them to have them do what the specs say.
def f(L):
    """ L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet. """
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f((L[0])):
            return L[0]
        
# print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'


def g(L, e):
    """ L is list of ints, e is an int
    Returns a count of how many times e occurrs in L  """
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            1+g(L[1:], e)
        else:
            return 1
    
# print(g([1,2,3,1], 1))     # should print 2
# print(g([1,1,2,3,1,1], 1)) # should print 4
    

def h(L, e):
    """ L is list, e is an int
    Returns a count of how many times e occurrs in L or 
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0])==int:
            if L[0] == e:
                return 1+h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0])== list:
            return h(L[1:], e)
    
# print(h([1,2,[3],1], 1))        # should print 2
# print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4
    
#####################################################    


####################################################################
############## ANSWERS TO AT HOME #######################
####################################################################
# Q1. Memoize the code to find possible scores in basketball
def score_count(x, d):
    if x in d:
        return d[x]
    else:
        score = score_count(x-1, d)+score_count(x-2, d)+score_count(x-3, d) 
        d[x] = score
        return score
    
# d = {1:1, 2:2, 3:3}
# print(score_count(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431

# Q2
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or 
    sublists of L and False otherwise. 
    """
    if len(L)==1 and type(L[0])!=list:
        return e==L[0]
    elif len(L)==1 and type(L[0])==list:
        return e in L[0]
    elif type(L[0])!=list:
        if e==L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)
    elif type(L[0])==list:
        if e in L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)


# test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False

# Q3
def my_deepcopy(L):
    """ 
    Implements a recursive version of copy.deepcopy().
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that 
    contains copies (recursively) of every sublist 
    """
    pass
    if len(L) == 0:
        return []
    elif type(L[0]) != list:
        return [L[0]] + my_deepcopy(L[1:])
    else:
        return [my_deepcopy(L[0])] + my_deepcopy(L[1:])

# myL = ["abc", ['d'], ['e', ['f', 'g']]]
# my_newL = my_deepcopy(myL)
# print(myL)
# print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]

# Q4
def f(L):
    """ L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet. """
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f((L[1:])):
            return L[0]
        else:
            return f(L[1:])
        
# print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'


def g(L, e):
    """ L is list of ints, e is an int
    Returns a count of how many times e occurrs in L  """
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            return 1+g(L[1:], e)
        else:
            return g(L[1:], e)
    
# print(g([1,2,3,1], 1))     # should print 2
# print(g([1,1,2,3,1,1], 1)) # should print 4
    

def h(L, e):
    """ L is list, e is an int
    Returns a count of how many times e occurrs in L or 
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0])==int:
            if L[0] == e:
                return 1+h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0])== list:
            if e in L[0]:
                return h(L[0], e)+h(L[1:], e)
            else:
                return h(L[1:], e)
    
# print(h([1,2,[3],1], 1))        # should print 2
# print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4
