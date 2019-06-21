a=input("Enter Numbers saparated by space : ")
a=a.split()
a=[int(i) for i in a]


firstLarge=0
secondLarge=0

for i in a:
	if i>firstLarge:
		secondLarge=firstLarge
		firstLarge=i

print(firstLarge)
print(secondLarge)