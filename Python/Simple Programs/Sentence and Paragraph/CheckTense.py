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


a=input("Enter a Sentence : ")


a=a.split()

if (len(a)>=2):
	if isinterogative(a):
		print("From Interogative : \n\t", end="")
		if a[0] in ['is','am','are']:
			print("Present Continuous")
		elif a[0] in ['was','were']:
			print("Past Continuous")
		elif a[0] == 'had' and a[2] != 'been':
			print("Past Perfect")
		elif a[0] == 'had' and a[2] == 'been':
			print("Past Perfect Continuous")
		elif a[0] in ['has','have'] and a[2]=='been':
			print("Present Perfect Continuous")
		elif a[0] in ['has','have'] and a[2]!='been':
			print("Present Perfect")
		elif a[0] in ['will','shall'] and not(a[2] in ['have','be']):
			print("Future Simple")
		elif a[0] in ['will','shall'] and a[2] == 'be':
			print("Future Continuous")
		elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
			print("Future  Perfect")
		elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
			print("Future Perfect Continuous")
		elif a[0] in ['do','does']:
			print("Present Simple")
		elif a[0] == 'did':
			print("Past Simple")
		
	elif isnegative(a):
		print("From Negative : \n\t", end="")
		if a[1] in ['is','am','are']:
			print("Present Continuous")
		elif a[1] in ['was','were']:
			print("Past Continuous")
		elif a[1] == 'had' and a[3] != 'been':
			print("Past Perfect")
		elif a[1] == 'had' and a[3] == 'been':
			print("Past Perfect Continuous")
		elif a[1] in ['has','have'] and a[3]=='been':
			print("Present Perfect Continuous")
		elif a[1] in ['has','have'] and a[3]!='been':
			print("Present Perfect")
		elif a[1] in ['will','shall'] and not(a[3] in ['have','be']):
			print("Future Simple")
		elif a[1] in ['will','shall'] and a[3] == 'be':
			print("Future Continuous")
		elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] != 'been':
			print("Future  Perfect")
		elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] == 'been':
			print("Future Perfect Continuous")
		elif a[1] in ['do','does']:
			print("Present Simple")
		elif a[1] == 'did':
			print("Past Simple")

	else:
		print("From Affermative : \n\t", end="")
		if a[1] in ['is','am','are']:
			print("Present Continuous")
		elif a[1] in ['was','were']:
			print("Past Continuous")
		elif a[1] == 'had' and a[2] != 'been':
			print("Past Perfect")
		elif a[1] == 'had' and a[2] == 'been':
			print("Past Perfect Continuous")
		elif a[1] in ['has','have'] and a[2]=='been':
			print("Present Perfect Continuous")
		elif a[1] in ['has','have'] and a[2]!='been':
			print("Present Perfect")
		elif a[1] in ['will','shall'] and not(a[2] in ['have','be']):
			print("Future Simple")
		elif a[1] in ['will','shall'] and a[2] == 'be':
			print("Future Continuous")
		elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
			print("Future  Perfect")
		elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
			print("Future Perfect Continuous")
		else:
			print(checkVerb(a[1]))
		
else:
	print("Please Enter a sentence not a Word")