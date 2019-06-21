def main():
    num = int(input("Enter Number : "))
    multiples = []

    for i in range(1,num):
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            multiples.append(i)
    
    print(sum(multiples))

if __name__ == '__main__':
    main()