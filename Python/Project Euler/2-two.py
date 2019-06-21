def main():
    term = 1
    sum = 0

    value = 1
    while (value < 4000000):
        value = fibb(term)
        if value % 2 == 0:
            sum += value
        term += 1

    print(sum)


def fibb(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        first = 1
        second = 2

        for i in range(num-2):
            fibb = first + second
            first = second
            second = fibb

        return fibb


if __name__ == '__main__':
    main()
