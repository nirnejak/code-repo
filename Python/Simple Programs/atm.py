amt=int(input("How much money you want to withdraw : "))
tempAmt=amt
var500=0
var100=0
var50=0
var20=0
var10=0
var5=0
var2=0
var1=0
if(amt>=500):
	var500=int(amt/500)
	amt=int(amt%500)
if(amt>=100):
	var100=int(amt/100)
	amt=int(amt%100)
if(amt>=50):
	var50=int(amt/50)
	amt=int(amt%50)
if(amt>=20):
	var20=int(amt/20)
	amt=int(amt%20)
if(amt>=10):
	var10=int(amt/10)
	amt=int(amt%10)
if(amt>=5):
	var5=int(amt/5)
	amt=int(amt%5)
if(amt>=2):
	var2=int(amt/2)
	amt=int(amt%2)
if(amt>=1):
	var1=int(amt)


if (var500!=0):
	print("500 Notes : ",var500)
if (var100!=0):
	print("100 Notes : ",var100)
if (var50!=0):
	print("50 Notes : ",var50)
if (var20!=0):
	print("20 Notes : ",var20)
if (var10!=0):
	print("10 Notes : ",var10)
if (var5!=0):
	print("5 Coins : ",var5)
if (var2!=0):
	print("2 Coins : ",var2)
if (var1!=0):
	print("1 Coins : ",var1)

