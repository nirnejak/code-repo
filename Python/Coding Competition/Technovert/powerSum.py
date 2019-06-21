import itertools
import math

def findsubsets(S,m):
	return set(itertools.combinations(S, m))

# findsubsets = lambda S,m : set(itertools.combinations(S,m))

x = int(input("Enter X : "))
n = int(input("Enter N : "))

nums = list(range(1, int(x**(1/float(n)))+1))

num_comb = set()

for i in range(1, max(nums)+1):
    num_comb.update(findsubsets(nums,i))

ans = 0

for i in num_comb:
    sum = 0
    for j in i:
        sum+= j**n
    if sum == x:
        ans += 1
print(num_comb)
print(ans)
