print("What you want to do ? ")
print("A. Decimal to Binary")
print("B. Binary to Decimal")
option=input()

if option=='A':
	n=float(input("Enter Number in Decimal : "))
	binary=0
	i=1
	while(n):
		remainder=int(n%2)
		n=int(n/2)
		binary=binary+(remainder*i)
		i=i*10
	print("Number in Binary is :",binary)
elif option=='B':
	base=1
	num=float(input("Enter Number in Binary : "))
	binary_num=num
	decimal=0
	while(num>0):
		rem=int(num%10)
		decimal=decimal+int(rem*base)
		num=int(num/10)
		base=int(base*2)
	print("Number in Decimal is :",decimal)