def main():
    S = input()
    lower = sorted([i for i in S if i.islower()])
    upper = sorted([i for i in S if i.isupper()])
    even = sorted([i for i in S if i.isnumeric() and int(i) % 2 == 0])
    odd = sorted([i for i in S if i.isnumeric() and int(i) % 2 != 0])

    result = ''.join(lower)
    result += ''.join(upper)
    result += ''.join(odd)
    result += ''.join(even)

    print(result)


if __name__ == '__main__':
    main()
