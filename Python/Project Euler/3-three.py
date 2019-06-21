def main():
    num = 13195

    largest = 0

    for i in range(1, num):
        if num % i == 0 and isprime(i) and i > largest:
            largest = i

    print(largest)


def isprime(num):
    testvar = 0

    if num == 1:
        return False

    for i in range(1, num+1):
        if num % i == 0:
            testvar += 1

    if testvar > 2:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
    # Program is taking longer to calculate result for large number
