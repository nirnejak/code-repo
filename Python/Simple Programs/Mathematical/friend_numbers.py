n=int(input("Enter N : "))

friends=[]

for m1 in range(2,n+1):
	friend=[]
	flag=0
	div=[]
	for i in range(1,m1):
		if m1%i==0:
			div.append(i)
	m2=sum(div)

	div=[]
	for i in range(1,m2):
		if m2%i==0:
			div.append(i)
	m3=sum(div)

	if m1==m3 and m3<n:
		friend=[m1,m2]
	if friend!=[]:
		friends.append(friend)

print(friends)