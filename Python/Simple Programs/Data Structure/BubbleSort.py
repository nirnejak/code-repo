a=input("Enter Numbers to Sort : ")
a=a.split()
a=[int(i) for i in a]

for j in range(len(a),1,-1):
	for i in range(0,len(a)-1):
		if a[i]>a[i+1]:
			temp=a[i]
			a[i]=a[i+1]
			a[i+1]=temp
print(a)