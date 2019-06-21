def display(ans):
	print("Answer is : ",ans)

#def operation(a,b,option):

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

print("What you want to do ? ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")
option=int(input())

#opration(a,b,option)

if option==1:
	ans=a+b
	display(ans)
elif option==2:
	ans=a-b
	display(ans)
elif option==3:
	ans=a*b
	display(ans)
elif option==4:
	ans=a/b
	display(ans)
elif option==5:
	ans=a%b
	display(ans)