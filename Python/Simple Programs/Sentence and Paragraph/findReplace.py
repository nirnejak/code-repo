a=input("Enter Paragraph : ")
a=a.split()

search=input("Enter Word to Search : ")

if search in a:
	replace=input("Enter Word to Replace with : ")
	for i in range(0,len(a)):
		if(a[i]==search):
			a[i]=replace

	a=" ".join(a)
	print(a)
else:
	print("Word is not in Paragraph")