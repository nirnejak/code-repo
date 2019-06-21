from itertools import groupby


def main():
    S = list(input())
    S = [int(i) for i in S]
    groups = groupby(S)
    repeat = [(sum(1 for _ in group), label) for label, group in groups]

    for i in repeat:
        print(i, end=' ')


if __name__ == '__main__':
    main()
