s=input("Enter String to Check : ")
s1=list()
s2=list()
for i in range(0,len(s)):
	s1.append(s[i])
for i in range(0,len(s)):
	s2.append(s1[len(s)-i-1])
if(s1==s2):
	print(1)
else:
	print(0)