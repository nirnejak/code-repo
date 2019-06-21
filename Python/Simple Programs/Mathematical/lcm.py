a=input("Enter Numbers Saparated by Space : ")
a=a.split()
a=[int(i) for i in a]
mul=1

for i in range(0,len(a)):
	mul*=a[i]

for i in range(max(a),mul+1):
	flag=0
	for j in range(0,len(a)):
		if int(i%a[j])==0:
			flag=flag+1
	if flag==len(a):
		lcm=i
		break
print("LCM of ",a,"is ", lcm)