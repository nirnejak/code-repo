import re


def fun(s):
    if s.count('@') == 1:
        temp = s.split('@')
        # Removing Empty Strings
        temp = [x for x in temp if x]
        if len(temp) == 2:
            username = temp[0]
            domain = temp[1]

            # Checking if email has only one domain
            if domain.count('.') == 1:
                temp = domain.split('.')
                websitename = temp[0]
                extension = temp[1]

                # validating length of extension
                if len(extension) <= 3 and len(re.findall('[^A-Za-z]', extension)) == 0:
                    if len(re.findall('[^A-Za-z0-9]', websitename)) == 0:
                        if len(re.findall('[^A-Za-z0-9_-]', username)) == 0:
                            return True
                        else:
                            # Special Character in username other than _ and -
                            return False
                    else:
                        # special character in website name
                        return False
                else:
                    # length of extension of more than 3
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


'''
5
itsme@gmail
@something
@something.com
@something.co1
sone.com
'''

'''
5
dheeraj-234@gmail.com
itsallcrap
harsh_1234@rediff.in
kunal_shin@iop.az
matt23@@india.in
'''
