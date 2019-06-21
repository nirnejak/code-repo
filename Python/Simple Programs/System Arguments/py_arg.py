import sys
no=len(sys.argv)
print("Number of arguments is ",no)
print("arguments are"+str(sys.argv))

#sys.argv[0] is always the name of the file

for i in range(0,len(sys.argv)):
	print(sys.argv[i])