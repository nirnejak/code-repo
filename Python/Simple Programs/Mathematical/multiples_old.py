a=input("Enter Numbers separated by space : ")
a=a.split()
a=[int(i) for i in a]

mul_var=list()
temp_mul_var=list()

#finding multiples and storing them in mul_var
for i in range(0,len(a)):
	temp_mul_var=list()
	for j in range(1,a[i]+1):
		if a[i]%j==0:
			temp_mul_var.append(j)
	for j in range(0,len(temp_mul_var)):
		mul_var.append(list(temp_mul_var))
print(mul_var)