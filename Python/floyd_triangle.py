def main(max_row):
    column_count = 1
    num = 1
    for row in range(max_row):
        for column in range(column_count):
            print(num, end=" ")
            num += 1
        print()
        column_count += 1



if __name__ == '__main__':
    num = int(input("Enter now of rows : "))
    main(num)