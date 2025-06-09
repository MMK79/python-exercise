def even_str(w):
    new_w = ""
    for i in range(len(w)):
        if i%2 == 0:
            new_w += w[i]
    return new_w
    # OR
    # print(new_w)
    # return None
    # OR
    # return w[::2]

word = input("enter your word")
print(even_str(word))
print(word[::2])
