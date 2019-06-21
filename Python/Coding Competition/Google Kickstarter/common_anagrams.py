T = int(input())
num = 1

def anagram_check(str1, str2):
    if len(str1) == len(str2) and set(str1) == set(str2):
        return True
    else:
        False

'''
# Get the string
str = input("Enter String:")
substring = []
# find all possible substrings for a given string
for counter in range (0,len(str)):
    substring.append(str[counter:len(str)])
print(substring)
'''

while(num<=T):
    L = int(input())
    A = input()
    B = input()

    substring = []

    for bound in range(1, len(A)+1):
        str1 = ''
        for i in range(0, bound):
            str1 += A[i]
        print(str1)
    print("Case #", num, " ", ans)