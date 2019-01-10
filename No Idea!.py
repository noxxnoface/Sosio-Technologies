n, m = (int(i) for i in input().split())
arr = map(int, input().strip().split(' '))
a = set(map(int, input().strip().split(' ')))
b = set(map(int, input().strip().split(' ')))
happiness = 0
for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness += -1
print(happiness)
