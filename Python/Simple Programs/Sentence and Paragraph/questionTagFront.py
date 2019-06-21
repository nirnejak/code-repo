def isinterogative(a):
	if a[0] in [
	'is','am',
	'are','do',
	'does','did',
	'was','were',
	'has','have',
	'had','will',
	'shall','should',
	'would','can',
	'could'
	]:
		return True
	else:
		return False
def isnegative(a):
	if 'not' in a:
		return True
	else:
		return False

a=input("Enter a Sentence : ")

a=a.split()

if (len(a)>=2):
	if isinterogative(a):
		print("From Interogative : \n\t", end="")
		if(a[0]=='can'):
			a[0]=a[0]+'\'t'
		elif (a[0]=='will'):
			a[0]='wouldn\'t'
		elif (a[0]=='shall'):
			a[0]='shouldn\'t'
		else:
			a[0]=a[0]+'n\'t'
		a=" ".join(a)
		
	elif isnegative(a):
		print("From Negative : \n\t", end="")
		if(a[1]=='can'):
			que=a[1]+'\'t'
		elif (a[1]=='will'):
			que='wouldn\'t'
		elif (a[1]=='shall'):
			que='shouldn\'t'
		else:
			que=a[1]+'n\'t'
		del(a[1])
		temp=list()
		temp.append(que)
		for i in range(0,len(a)):
			temp.append(a[i])

		del(temp[2])	#uncomment this to remove 'not'

		a=" ".join(temp)
	else:
		if 'n\'t' in a[0]:
			print("Already in Desired Format : \n\t", end="")
			a=" ".join(a)
		elif a[0]=='how' or a[0]=='where' or a[0]=='when' or a[0]=='why' or a[0]=='who' or a[0]=='what':
			print("WH Sentence : \n\t", end="")
			a=" ".join(a)
		else:
			print("From Affermative : \n\t", end="")
			if(a[1]=='can'):
				que=a[1]+'\'t'
			elif (a[1]=='will'):
				que='wouldn\'t'
			elif (a[1]=='shall'):
				que='shouldn\'t'
			else:
				que=a[1]+'n\'t'
			del(a[1])
			temp=list()
			temp.append(que)
			for i in range(0,len(a)):
				temp.append(a[i])
			a=" ".join(temp)
		
	a=list(a)
	if(a[len(a)-1]=='.' or a[len(a)-1]=='?'):
		a[len(a)-1]='?'
	else:
		a.append('?')
	a="".join(a)
	print(a)
else:
	print("Please Enter a sentence not a Word")