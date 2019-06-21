def main():
    words = []
    for i in range(int(input())):
        words.append(input())

    unique = [words[0]]
    for i in words:
        if i not in unique:
            unique.append(i)
    print(len(unique))

    for i in unique:
        print(words.count(i), end=' ')


if __name__ == '__main__':
    main()
