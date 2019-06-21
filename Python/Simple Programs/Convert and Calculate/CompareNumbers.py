a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))

if a>b and a>c:
	print(a, end=" ")
	if b>c:
		print(b,c,end=" ")
	else:
		print(c,b,end=" ")
elif b>a and b>c:
	print(b, end=" ")
	if a>c:
		print(a,c,end=" ")
	else:
		print(c,a,end=" ")
elif c>a and c>c:
	print(c, end=" ")
	if a>b:
		print(a,b,end=" ")
	else:
		print(b,a,end=" ")