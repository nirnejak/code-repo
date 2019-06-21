num_str=input("Enter Numbers separated by space : ")
a=num_str.split()
for i in range(0,len(a)):
	a[i]=int(a[i])
max_var=max(a)
for i in range(max(a),0,-1):
	flag=0
	for j in range(0,len(a)):
		if(a[j]%i==0):
			flag+=1
	if(flag==len(a)):
		hcf=i
		break
print("HCF is ",i,"\n")