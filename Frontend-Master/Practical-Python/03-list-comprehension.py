a = 'abcdefghijklmnopqrstuvwxyz'
l = []
d = {}

# create a dictionary
for i in range(len(a)):
    d[i] = a[i]

# create a list
for i in a:
    l.append(i)

# print(l)
# print(d)

# Enumerator function + Tuple unpacking
# for i, v in enumerate(l):
#     print(f"in index {i} value is {v}")

# tuple unpacking on dictionary items
# for k, v in d.items():
#     print(f"whit key of {k}, your value is {v}")

# List Comprehension
new_l = [elem*2 for elem in l if l.index(elem)%2==0]
# print(new_l)

# Convert string to list
names = "ali,ahmad,reza,hossein"
names_l = names.split(',')
# print(names_l)

names = "ali ahmad reza hossein"
names_l = names.split(' ')
# print(names_l)

names = "ali, ahmad, reza, hossein"
names_l = names.split(', ')
# print(names_l)

# Convert list to string
names_ls = " - ".join(names_l)
# print(names_ls)

# Now lets combine list comprehension and converting to string
n_l = []
for i in range(10):
    n_l.append(i)
# print(n_l)
comb_ls = " ,".join([str(elem**2) for elem in n_l if elem%2 == 1])
# print(comb_ls)

# Generator Comprehension + Generator type
gen_com = (i*2 for i in range(10) if i%3 == 0)
# print(gen_com, type(gen_com))
# for i in gen_com:
#     print(i, type(i))
# for i in gen_com:
#     print(f"After using Generator, now it is exhusted as you don't see this massage")
# print("there is a hidden message that you didn't see :D")

sentence = "Hello World!"
# for c, i in enumerate(sentence):
#     print(c, i)
# Slicing
# print(sentence[:5])
# print(sentence[6:])
# print(sentence[6:])
# print(sentence[-1:])
# print(sentence[:-1])
# print(sentence[-1:-5:-1])
# print(sentence[::-1])
