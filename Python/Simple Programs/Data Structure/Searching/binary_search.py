arr=input("Enter the Numbers Separated by Space : ")
arr=arr.split()
for i in range(0,len(arr)):
	arr[i]=int(arr[i])
arr.sort()
print(arr)
num=int(input("Enter Number to Search : "))
mid=int(len(arr)/2)
pos=0
if num>=arr[mid]:
	for i in range(mid,len(arr)):
		if arr[i]==num:
			pos=i
			break
else:
	for i in range(mid,0,-1):
		if arr[i]==num:
			pos=i
			break
if pos==0:
	print("Number is not found")
else:
	print("Number is found at Position ",pos+1)