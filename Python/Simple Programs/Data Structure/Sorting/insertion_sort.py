arr_temp = input("Enter Numbers : ")
arr = arr_temp.split()

for i in range(0, len(arr)):
    arr[i] = int(arr[i])

# insertion sort

for i in range(0, len(arr)):
    temp = arr[i]
    j = i - 1
    while temp > arr[j] and j >= 0:
    	arr[j+1]=arr[j]
    	j=j-1
    j=j+1
    arr[j]=temp

print(arr)