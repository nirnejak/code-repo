a=input("Enter A Paragraph : ")

a=a.split()

max=0
max_len=0

for i in range(0,len(a)):
	if len(a[i])>max_len:
		max=i
		max_len=len(a[i])

print("Longest Word is : ",a[max])