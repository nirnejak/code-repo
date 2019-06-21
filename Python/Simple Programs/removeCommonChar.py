'Remove the common characters from both the strings'
str1 = list(input())
str2 = list(input())

common = []

for ch in str1:
    if ch in str2:
        str2.remove(ch)
        common.append(ch)
for ch in common:
    str1.remove(ch)

print(''.join(str1))
print(''.join(str2))
print(common)
