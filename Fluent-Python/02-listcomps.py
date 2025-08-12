symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    # ord() return a unicode for a character
    codes.append(ord(symbol))
# print(codes)

# with list comprehension
codes = [ord(symbol) for symbol in symbols]

# with filter and map
# map(ord, symbols) --> apply ord function on symbols and return an iterator
# filter() return an iterator which applied function (lambda c: c > 127) on the given iterator (map(ord, symbols)) return true
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
beyond_ascii = list(filter(lambda c:c > 127, map(ord, symbols)))
print(codes==beyond_ascii)

codes_dic = {}
symbols_lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols_upper = 'abcdefghijklmnopqrstuvwxyz'
for symbol_lower in symbols_lower:
    codes_dic[symbol_lower] = ord(symbol_lower)
for symbol_upper in symbols_upper:
    codes_dic[symbol_upper] = ord(symbol_upper)
from pprint import pprint
# pprint(codes_dic)

# with dict comprehension
codes_dic_comp = {symbol:ord(symbol) for symbol in symbols_lower+symbols_upper}
# pprint(codes_dic_comp)
print(codes_dic_comp==codes_dic)
