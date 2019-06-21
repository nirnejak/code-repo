a=input("Enter A Paragraph : ")

a=a.split()

max=a[0]

for i in range(0,len(a)):
	if len(max)<len(a[i]):
		max=a[i]

print("Longest Word is : ",max)