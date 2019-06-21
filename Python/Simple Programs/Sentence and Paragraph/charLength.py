a=input("Enter Paragraph : ")

a=a.split()

one_char=0
two_char=0
three_char=0
four_char=0
five_char=0
six_char=0

for i in range(0,len(a)):
	if len(a[i])==1:
		one_char+=1
	if len(a[i])==2:
		two_char+=1
	if len(a[i])==3:
		three_char+=1
	if len(a[i])==4:
		four_char+=1
	if len(a[i])==5:
		five_char+=1
	if len(a[i])==6:
		six_char+=1

print("One Character Word : ",one_char)
print("Two Character Word : ",two_char)
print("Three Character Word : ",three_char)
print("Four Character Word : ",four_char)
print("Five Character Word : ",five_char)
print("Six Character Word : ",six_char)
