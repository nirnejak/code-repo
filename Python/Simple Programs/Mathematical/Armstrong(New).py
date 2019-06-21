a=int(input("Enter Number : "))
b=str(a)
b=list(b)
for i in range(0,len(b)):
	b[i]=int(b[i])
for i in range(0,len(b)):
	b[i]=b[i]*b[i]*b[i]
if a==sum(b):
	print("Number is Armstrong Number")
else:
	print("Number is not Armstrong Number")