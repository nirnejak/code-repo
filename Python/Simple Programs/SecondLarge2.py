a=input("Enter Numbers Saparated by Space : ")
a=a.split()
a=[int(i) for i in a]

firstLarge=max(a)

a.remove(firstLarge)

secondLarge=max(a)

print(secondLarge)