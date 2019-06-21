print("What you want to do ? ")
print("A. Celsius to Farenheit")
print("B. Farenheit to Celsius")
option=input()

if option=='A':
	temp=float(input("Enter Temperature in Celsius : "))
	ans=temp*(9/5)+32
	print("Temperature in Farenheit is :",ans)
elif option=='B':
	temp=float(input("Enter Temperature in Farenheit : "))
	ans=(temp-32)/(9/5)
	print("Temperature in Celsius is :",ans)