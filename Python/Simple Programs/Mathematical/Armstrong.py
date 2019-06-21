num=int(input("Enter Number to Check : "))
numa=num%10
numb=int(((num%100)-numa)/10)
numc=int(((num%1000)-(numa+numb))/100)
if (num==(numa*numa*numa)+(numb*numb*numb)+(numc*numc*numc)):
    print("Number is an armstrong Number")
else:
    print("Number is not armstrong Number")
