a=input()
b=a.split()
s1=list(b[0])
s1.sort()
s2=list(b[1])
s2.sort()
if s1==s2:
	print(1)
else:
	print(0)