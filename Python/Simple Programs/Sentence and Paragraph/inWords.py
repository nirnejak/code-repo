def SingletoWord(strFirst):
	if strFirst=='0':
		return 'ignore'
	if strFirst=='1':
		return 'One'
	if strFirst=='2':
		return 'Two'
	if strFirst=='3':
		return 'Three'
	if strFirst=='4':
		return 'Four'
	if strFirst=='5':
		return 'Five'
	if strFirst=='6':
		return 'Six'
	if strFirst=='7':
		return 'Seven'
	if strFirst=='8':
		return 'Eight'
	if strFirst=='9':
		return 'Nine'

def tensWord(strFirst):
	if strFirst=='1':
		return 'Ten'
	if strFirst=='2':
		return 'Twenty'
	if strFirst=='3':
		return 'Thirty'
	if strFirst=='4':
		return 'Fourty'
	if strFirst=='5':
		return 'Fifty'
	if strFirst=='6':
		return 'Sixty'
	if strFirst=='7':
		return 'Seventy'
	if strFirst=='8':
		return 'Eighty'
	if strFirst=='9':
		return 'Ninty'

def tensToWord(strFirst):	# for twenty one, thirty five
	if strFirst=='2':
		return 'Twenty'
	if strFirst=='3':
		return 'Thirty'
	if strFirst=='4':
		return 'Fourty'
	if strFirst=='5':
		return 'Fifty'
	if strFirst=='6':
		return 'Sixty'
	if strFirst=='7':
		return 'Seventy'
	if strFirst=='8':
		return 'Eighty'
	if strFirst=='9':
		return 'Ninty'

def teens(strFirst):
	if strFirst=='0':
		return 'Ten'
	if strFirst=='1':
		return 'Eleven'
	if strFirst=='2':
		return 'Twelve'
	if strFirst=='3':
		return 'Thirteen'
	if strFirst=='4':
		return 'Fourteen'
	if strFirst=='5':
		return 'Fifteen'
	if strFirst=='6':
		return 'Sixteen'
	if strFirst=='7':
		return 'Seventeen'
	if strFirst=='8':
		return 'Eighteen'
	if strFirst=='9':
		return 'Ninteen'

def DoubletoWord(part):
	if part[0]=='0' and part[1]=='0':
		return 'ignore'
	elif part[0]=='0' and part[1]!='0':
		return SingletoWord(part[1])
	elif part[1]=='0' and part[0]!='0':
		return tensWord(part[0])
	elif part[0]=='1' and part[1]!='0':
		return teens(part[1])
	else:
		return tensToWord(part[0])+" "+SingletoWord(part[1])

	if part[1]=='0' and part[0]=='1':
		return 'Ten'

strIn=input("Enter Number : ")

if strIn.isnumeric():
	if(len(strIn)==5):
		partThree=strIn[len(strIn)-5]+strIn[len(strIn)-4]
		partThree=DoubletoWord(partThree)
		if partThree!='ignore':
			print(partThree+" Thousand")

		partTwo=strIn[len(strIn)-3]
		partTwo=SingletoWord(partTwo)
		if partTwo!='ignore':
			print(partTwo+" Hundred")

		partOne=strIn[len(strIn)-2]+strIn[len(strIn)-1]
		partOne=DoubletoWord(partOne)
		if partOne!='ignore':
			print(partOne)

		if partOne==partTwo==partThree=='ignore':
			print("Zero")
	if(len(strIn)==4):
		partThree=strIn[len(strIn)-4]
		partThree=SingletoWord(partThree)
		if partThree!='ignore':
			print(partThree+" Thousand")

		partTwo=strIn[len(strIn)-3]
		partTwo=SingletoWord(partTwo)
		if partTwo!='ignore':
			print(partTwo+" Hundred")

		partOne=strIn[len(strIn)-2]+strIn[len(strIn)-1]
		partOne=DoubletoWord(partOne)
		if partOne!='ignore':
			print(partOne)
		
		if partOne==partTwo==partThree=='ignore':
			print("Zero")
	if(len(strIn)==3):
		partTwo=strIn[len(strIn)-3]
		partTwo=SingletoWord(partTwo)
		if partTwo!='ignore':
			print(partTwo+" Hundred")

		partOne=strIn[len(strIn)-2]+strIn[len(strIn)-1]
		partOne=DoubletoWord(partOne)
		if partOne!='ignore':
			print(partOne)

		if partOne==partTwo=='ignore':
			print("Zero")
	if(len(strIn)==2):
		partOne=strIn[len(strIn)-2]+strIn[len(strIn)-1]
		print(partOne)
		partOne=DoubletoWord(partOne)
		if partOne!='ignore':
			print(partOne)
		else:
			print("Zero")
	if(len(strIn)==1):
		partOne=strIn[len(strIn)-1]
		partOne=SingletoWord(partOne)
		if partOne!='ignore':
			print(partOne)
		else:
			print("Zero")

else:
	print("Please Enter a Number")