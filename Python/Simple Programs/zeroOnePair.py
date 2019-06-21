n=int(input())
num=int(n)
while(True):
	b=set(str(num))
	if(len(b)==2):
		if('0' in b and '1' in b):
			print(num)
			break
	if(len(b)==1):
		if('1' in b):
			print(num)
			break
	num+=n