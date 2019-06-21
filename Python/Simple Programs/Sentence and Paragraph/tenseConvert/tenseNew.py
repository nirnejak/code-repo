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
		return "present simple"
	else:
		return "past simple"

def checkTense(a):
	if (len(a)>=2):
		if isinterogative(a):
			if a[0] in ['is','am','are']:
				return "present continuous"
			elif a[0] in ['was','were']:
				return "past continuous"
			elif a[0] == 'had' and a[2] != 'been':
				return "past perfect"
			elif a[0] == 'had' and a[2] == 'been':
				return "past perfect continuous"
			elif a[0] in ['has','have'] and a[2]=='been':
				return "present perfect continuous"
			elif a[0] in ['has','have'] and a[2]!='been':
				return "present perfect"
			elif a[0] in ['will','shall'] and not(a[2] in ['have','be']):
				return "future simple"
			elif a[0] in ['will','shall'] and a[2] == 'be':
				return "future continuous"
			elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
				return "future  perfect"
			elif a[0] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
				return "future perfect continuous"
			elif a[0] in ['do','does']:
				return "present simple"
			elif a[0] == 'did':
				return "past simple"
			
		elif isnegative(a):
			if a[1] in ['is','am','are']:
				return "present continuous"
			elif a[1] in ['was','were']:
				return "past continuous"
			elif a[1] == 'had' and a[3] != 'been':
				return "past perfect"
			elif a[1] == 'had' and a[3] == 'been':
				return "past perfect continuous"
			elif a[1] in ['has','have'] and a[3]=='been':
				return "present perfect continuous"
			elif a[1] in ['has','have'] and a[3]!='been':
				return "present perfect"
			elif a[1] in ['will','shall'] and not(a[3] in ['have','be']):
				return "future simple"
			elif a[1] in ['will','shall'] and a[3] == 'be':
				return "future continuous"
			elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] != 'been':
				return "future  perfect"
			elif a[1] in ['will','shall'] and a[3] == 'have' and a[4] == 'been':
				return "future perfect continuous"
			elif a[1] in ['do','does']:
				return "present simple"
			elif a[1] == 'did':
				return "past simple"

		else:
			if a[1] in ['is','am','are']:
				return "present continuous"
			elif a[1] in ['was','were']:
				return "past continuous"
			elif a[1] == 'had' and a[2] != 'been':
				return "past perfect"
			elif a[1] == 'had' and a[2] == 'been':
				return "past perfect continuous"
			elif a[1] in ['has','have'] and a[2]=='been':
				return "present perfect continuous"
			elif a[1] in ['has','have'] and a[2]!='been':
				return "present perfect"
			elif a[1] in ['will','shall'] and not(a[2] in ['have','be']):
				return "future simple"
			elif a[1] in ['will','shall'] and a[2] == 'be':
				return "future continuous"
			elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] != 'been':
				return "future  perfect"
			elif a[1] in ['will','shall'] and a[2] == 'have' and a[3] == 'been':
				return "future perfect continuous"
			else:
				return checkVerb(a[1])

def returnHV(tense, subject):
	if tense=="present simple" or tense=="past simple":
		return ""
	elif tense=="present continuous":
		if subject == 'i':
			return 'am'
		elif subject in ['you','they','we']:
			return 'are'
		else:
			return 'is'
	elif tense=="present perfect":
		if subject in ['i','we','they','you']:
			return 'have'
		else:
			return 'has'
	elif tense=="present perfect continuous":
		if subject in ['i','we','they','you']:
			return 'have been'
		else:
			return 'has been'
	elif tense=="past continuous":
		if subject in ['we','they','you']:
			return 'were'
		else:
			return 'was'
	elif tense=="past perfect":
		return 'had'
	elif tense=="past perfect continuous":
		return 'had been'
	elif tense=="future simple":
		return "will"
	elif tense=="future continuous":
		return "will be"
	elif tense=="future perfect":
		return "will have"
	elif tense=="future perfect continuous":
		return "will have been"

def addING(verb):
	if verb[len(verb)-1]=='e':
		verb=list(verb)
		verb.pop()
		verb="".join(verb)
		verb+="ing"
	else:
		verb+="ing"
	return verb
def removeING(verb):
	verb=list(verb)
	verb.pop()
	verb.pop()
	verb.pop()
	verb="".join(verb)
	verb+='e'
	return verb