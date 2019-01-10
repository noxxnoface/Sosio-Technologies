from itertools import groupby
from collections import OrderedDict

s = sorted(input())
dic = OrderedDict()
for m, n in groupby(s):
    dic.update({m:len(list(n))})

dic = OrderedDict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
for i in range(3):
    print(list(dic.keys())[i], list(dic.values())[i])
