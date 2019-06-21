def main():
    num = 20

    while(True):
        flag = 0
        for i in range(1,21):
            if num % i == 0:
                flag += 1
        if flag == 20:
            break

        num += 20

    print(num)


if __name__ == '__main__':
    main()