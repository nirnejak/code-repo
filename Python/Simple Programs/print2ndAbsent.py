"Print the elements from 1st array which are not present in 2nd Array"

a = input().split()
a = map(int, a)
b = input().split()
b = map(int, b)

for i in a:
    if not i in b:
        print(i, end=" ")
