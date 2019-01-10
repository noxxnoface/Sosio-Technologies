import itertools
n = input()
letters = input().split()
k = int(input())
PofA=0
P_total=0
for e in itertools.permutations(letters, k):
	P_total+=1
	PofA+='a' in e[:k]
print(PofA/P_total)
