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

def checkVerb(verb):
	verb=list(verb)
	if verb.pop()=='s':
		return "Present Simple"
	else:
		return "Past Simple"
def checkTense(a):
	if (len(a)>=2):
		if isinterogative(a):
			if a[0] in ['is','am','are']:
				return "Present Continuous"
			elif a[0] in ['was','were']:
				return "Past Continuous"
			elif a[0] == 'had' and a[2] != 'been':
				return "Past Perfect"
			elif a[0] == 'had' and a[2] == 'been':
				return "Past Perfect Continuous"
			elif a[0] in ['has','have'] and a[2]=='been':
				return "Present Perfect Continuous"
			elif a[0] in ['has','have'] and a[2]!='been':
				return "Present Perfect"
			elif a[0] in ['will','shall'] and not(a[2] in ['have','be']):
				return "Future Simple"
			elif a[0] in ['will','shall'] and a[2] == 'be':
				return "Future Continuous"
			elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
				return "Future  Perfect"
			elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
				return "Future Perfect Continuous"
			elif a[0] in ['do','does']:
				return "Present Simple"
			elif a[0] == 'did':
				return "Past Simple"
			
		elif isnegative(a):
			if a[1] in ['is','am','are']:
				return "Present Continuous"
			elif a[1] in ['was','were']:
				return "Past Continuous"
			elif a[1] == 'had' and a[3] != 'been':
				return "Past Perfect"
			elif a[1] == 'had' and a[3] == 'been':
				return "Past Perfect Continuous"
			elif a[1] in ['has','have'] and a[3]=='been':
				return "Present Perfect Continuous"
			elif a[1] in ['has','have'] and a[3]!='been':
				return "Present Perfect"
			elif a[1] in ['will','shall'] and not(a[3] in ['have','be']):
				return "Future Simple"
			elif a[1] in ['will','shall'] and a[3] == 'be':
				return "Future Continuous"
			elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] != 'been':
				return "Future  Perfect"
			elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] == 'been':
				return "Future Perfect Continuous"
			elif a[1] in ['do','does']:
				return "Present Simple"
			elif a[1] == 'did':
				return "Past Simple"

		else:
			if a[1] in ['is','am','are']:
				return "Present Continuous"
			elif a[1] in ['was','were']:
				return "Past Continuous"
			elif a[1] == 'had' and a[2] != 'been':
				return "Past Perfect"
			elif a[1] == 'had' and a[2] == 'been':
				return "Past Perfect Continuous"
			elif a[1] in ['has','have'] and a[2]=='been':
				return "Present Perfect Continuous"
			elif a[1] in ['has','have'] and a[2]!='been':
				return "Present Perfect"
			elif a[1] in ['will','shall'] and not(a[2] in ['have','be']):
				return "Future Simple"
			elif a[1] in ['will','shall'] and a[2] == 'be':
				return "Future Continuous"
			elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
				return "Future  Perfect"
			elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
				return "Future Perfect Continuous"
			else:
				return checkVerb(a[1])
		
	else:
		print("Please Enter a sentence not a Word")

a=input("Enter a Sentence : ")

a=a.split()

con=input("Tense you want to convert it into : ")


if checkTense(a)=="Present Simple":
	if con[0]=="Present Simple":
		print("Already in Present Simple")
	elif con[0]=="Present Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("is")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Present Perfect":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("has")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb.append('e')
		verb.append('d')
		verb="".join(verb)
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Present Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("has been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Simple":
		temp=input("Enter 2nd Form of Verb : ")
		a[1]=temp
	elif con[0]=="Past Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("was")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Perfect":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("had")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb.append('e')
		verb.append('d')
		verb="".join(verb)
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("had been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Simple":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will")
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will be")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Perfect":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will have")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb.append('e')
		verb.append('d')
		verb="".join(verb)
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will have been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
elif checkTense(a)=="Present Continuous":
	verb=a[2]
	verb=list(verb)
	verb.pop()
	verb.pop()
	verb.pop()
	verb.append("e")
	verb="".join(verb)
	a[2]=verb
	if con[0]=="Present Simple":
		del(a[1])
		a[1]+="s"
	elif con[0]=="Present Continuous":
		print("Already in Present Continuous")
	elif con[0]=="Present Perfect":
		temp=[]
		a[1]="has"
		a[2]+="ed"
	elif con[0]=="Present Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("has been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Simple":
		temp=input("Enter 2nd Form of Verb : ")
		a[1]=temp
	elif con[0]=="Past Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("was")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Perfect":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("had")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb.append('e')
		verb.append('d')
		verb="".join(verb)
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Past Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("had been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Simple":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will")
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will be")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Perfect":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will have")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb.append('e')
		verb.append('d')
		verb="".join(verb)
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
	elif con[0]=="Future Perfect Continuous":
		temp=[]
		for i in range(len(a)-1,0,-1):
			temp.append(a[i])
		a.append("will have been")
		verb=temp[len(temp)-1]
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
		temp[len(temp)-1]=verb
		while(len(temp)>=0):
			a.append(temp.pop())
elif checkTense(a)=="Present Perfect":
	pass
elif checkTense(a)=="Present Perfect Continuous":
	pass
elif checkTense(a)=="Past Simple":
	pass
elif checkTense(a)=="Past Continuous":
	pass
elif checkTense(a)=="Past Perfect":
	pass
elif checkTense(a)=="Past Perfect Continuous":
	pass
elif checkTense(a)=="Future Simple":
	pass
elif checkTense(a)=="Future Continuous":
	pass
elif checkTense(a)=="Future Perfect":
	pass
elif checkTense(a)=="Future Perfect":
	pass
elif checkTense(a)=="Future Perfect Continuous":
	pass

