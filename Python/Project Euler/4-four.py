def main():
    num1 = 999
    num2 = 999

    evenTerm = False
    while(num1 > 99 and num2 > 99):
        product = num1 * num2
        if ispalindrome(product):
            print(product)
            break

        if evenTerm:
            num1 -= 1
        else:
            num2 -= 1
        evenTerm = not evenTerm


def ispalindrome(num):
    temp = int(num)
    rev = 0
    # Calculating Reverse
    while(num):
        rev = (rev*10) + num % 10
        num = int(num/10)

    if temp == rev:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
