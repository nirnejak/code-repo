n=int(input("Enter End of Series : "))

for i in range(0,n+1):
	for j in range(i,-1,-1):
		print(n-j, end=" ")
	print("\r")

x=input()