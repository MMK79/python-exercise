symbols = '$¢£¥€¤'
tup_cast = tuple(ord(symbol) for symbol in symbols)
print(tup_cast)

import array
# array.array return array whose items are restricted by type code, check help(array.array) 
# I is unsigned integer
arr_cast = array.array('I', (ord(symbol) for symbol in symbols))
print(type(arr_cast))
print(arr_cast)

# Instead of creating a list and then feed it to for loop let's do it directly with genexp
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# with list
tshirt = [(c, s) for c in colors for s in sizes]
print(tshirt)
# with genexp no need to have a list to print the thing we want
for tshirt in (f'{c}, {s}' for c in colors for s in sizes):
    print(tshirt)

