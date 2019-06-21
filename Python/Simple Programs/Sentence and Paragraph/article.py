def isVowel(char):
	if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
		return True
	else:
		return False


instr=input("Enter Word : ")

if isVowel(instr[0]):
	print("An",instr)
else:
	print("A",instr)