import datetime

n = int(input())
for _ in range(n):
    t1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs(t1 - t2).total_seconds()))
