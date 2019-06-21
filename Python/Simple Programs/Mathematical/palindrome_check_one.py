string=input()
arr=list(string)
temp=list(arr)
arr.reverse()
if temp==arr:
	print("It is Palindrome")
else:
	print("It's not Palindrome")