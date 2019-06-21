def main():
    nm = input().split()
    n = nm[0]
    m = nm[1]

    arr = input().split()  # array of n elements
    A = set(input().split())
    B = set(input().split())

    happiness = 0
    for i in arr:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1

    print(happiness)


if __name__ == '__main__':
    main()
