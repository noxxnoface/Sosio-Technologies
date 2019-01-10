from itertools import groupby
string = input()
for m, n in groupby(string):
    print(tuple([len(list(n)), int(m)]), end = " ")
