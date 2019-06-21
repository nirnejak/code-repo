from tenseNew import *

a=input("Enter a Sentence : ")

a=a.split()

con=input("Tense you want to convert it into : ")

def convert(a,con):
	current=checkTense(a)
	subject=a[0]
	objects=[]
	while(not(a[len(a)-1] in ['will','is','am','are','was','were','shall','has','have','had','not','did','does','do','be','been'])):
		objects.append(a.pop())

	if ('continuous' in con) and ('continuous' in current):
		pass
	
	if ('simple' in con) and ('simple' in current) and ('present' in con) and ('present' in current):
		pass


	if not('continuous' in con) and 'continuous' in current:
		objects[len(objects)-1]=removeING(objects[len(objects)-1])
	if ('perfect' in current) and not('continuous' in current) and not('perfect' in con):
		#remove en or ed
		temp=list(objects.pop())
		if (temp[len(temp)-1]=="d"):
			temp.pop()
			temp.pop()
		elif(temp[len(temp)-1]=="n"):
			temp.pop()
			temp.pop()
			if (temp[len(temp)-1]=="t"):
				temp[len(temp)-1]="e"
		temp="".join(temp)
		objects.append(temp)

	if ('continuous' in con) and not('continuous' in current):
		objects[len(objects)-1]=addING(objects[len(objects)-1])

	if ('perfect' in con) and ('perfect' in current) and not('continuous' in con) and not('continuous' in current):
		pass
	elif not('continuous' in con) and ('perfect' in con):
		temp=list(objects[len(objects)-1])
		if (temp.pop() in ['y','h','m']):
			objects[len(objects)-1]+="ed"
		elif (temp.pop() in ['e','h','m']):
			objects[len(objects)-1]+="en"

	if ('present' in con) and ('simple' in con):
		if not(subject in ['i','you','we','they']):
			objects[len(objects)-1]+="s"

	if ('past' in con) and ('simple' in con):
		verb=input("Enter 2nd Form of Verb : ")
		objects[len(objects)-1]=verb

	helpVerb = returnHV(con, subject)

	a=[]
	a.append(subject)
	a.append(helpVerb)
	while(objects!=[]):
		a.append(objects.pop())

	a=" ".join(a)
	
	print("From : ",con)
	print("To : ",current)
	return a

current=checkTense(a)
if (con==current):
	print("Already in Desired Tense")
else:
	a=convert(a,con)

print("Output is : ",a)