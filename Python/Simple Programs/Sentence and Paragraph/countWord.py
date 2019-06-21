a=input("Enter Paragraph : ")
a=a.split()

b=set(a)
b=list(b)
count=list()
for i in range(0,len(b)):
	count.append(0)

for j in range(0,len(b)):
	for i in range(0,len(a)):
		if(b[j]==a[i]):
			count[j]+=1

print("\nNo of times per word is in Paragraph : ")
for i in range(0,len(b)):
	print(b[i]," is ",count[i]," times")