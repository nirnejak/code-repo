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

def convert(a):
	if a=='is':
		return "isn't"
	if a=='am':
		return "amn't"
	if a=='are':
		return "are't"
	if a=='was':
		return "wasn't"
	if a=='were':
		return "weren't"
	if a=='will':
		return "wouldn't"
	if a=='shall':
		return "shouldn't"
	if a=='would':
		return "wouldn't"
	if a=='should':
		return "shouldn't"
	if a=='do':
		return "don't"
	if a=='does':
		return "doesn't"
	if a=='did':
		return "didn't"
	if a=='has':
		return "'hasn't"
	if a=='have':
		return "haven't"
	if a=='had':
		return "hadn't"
	if a=='can':
		return "can't"
	if a=='could':
		return "couldn't"

a=input("Enter a Sentence : ")

a=list(a)
if(a[len(a)-1]=='.' or a[len(a)-1]=='?'):
		a[len(a)-1]=','
else:
	a.append(",")
a="".join(a)
print(a)

a=a.split()

if (len(a)>=2):
	if isinterogative(a):
		print("From Interogative : \n\t", end="")
		word=""
		word+=convert(a[0])
		word+=" "
		word+=a[1]
		word+="?"
		a.append(word)
		a=" ".join(a)
		
	elif isnegative(a):
		print("From Negative : \n\t", end="")
		word=""
		word+=convert(a[1])
		word+=" "
		word+=a[0]
		word+="?"
		a.append(word)
		#del(a[2])	#uncomment this to remove 'not'
		a=" ".join(a)
		
	else:
		print("From Affermative : \n\t", end="")
		word=""
		word+=convert(a[1])
		word+=" "
		word+=a[0]
		word+="?"
		a.append(word)
		a=" ".join(a)
	
	print(a)
else:
	print("Please Enter a sentence not a Word")