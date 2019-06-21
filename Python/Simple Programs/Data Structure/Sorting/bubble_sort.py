arr=input("Enter the Numbers Separated by Space : ")
arr=arr.split()
for i in range(0,len(arr)):
	arr[i]=int(arr[i])
print(arr)
for j in range(len(arr),1,-1):
	for i in range(0,len(arr)-1):
		if arr[i]>arr[i+1]:
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
print(arr)