def clearRem(remainder):
	if remainder==10:
		return 'A'
	if remainder==11:
		return 'B'
	if remainder==12:
		return 'C'
	if remainder==13:
		return 'D'
	if remainder==14:
		return 'E'
	if remainder==15:
		return 'F'

def putNum(num,pos):
	if(num[pos].isalpha()):
		if num[pos]=='A' or num[pos]=='a':
			return 10
		elif num[pos]=='B' or num[pos]=='b':
			return 11
		elif num[pos]=='C' or num[pos]=='c':
			return 12
		elif num[pos]=='D' or num[pos]=='d':
			return 13
		elif num[pos]=='E' or num[pos]=='e':
			return 14
		elif num[pos]=='F' or num[pos]=='f':
			return 15
	else:
		return int(num[pos])

print("What you want to do ? ")
print("A. Decimal to Hexadecimal")
print("B. Hexadecimal to Decimal")
option=input()

if option=='A':
	n=float(input("Enter Number in Decimal : "))
	hexadecimal=str()
	i=1
	while(n):
		remainder=int(n%16)
		if(remainder>9):
			remainder=clearRem(remainder)
		n=int(n/16)
		hexadecimal=str(remainder)+hexadecimal
		i=i*10
	print("Number in Hexadecimal is :", hexadecimal)
elif option=='B':
	base=1
	num=input("Enter Number in Hexadecimal : ")
	decimal=0
	pos=len(num)-1
	while(pos>=0):
		rem=putNum(num, pos)
		decimal=decimal+int(rem*base)
		pos-=1
		base=int(base*16)
	print("Number in Decimal is :", decimal)