import re


def rep(c):
    if c == '&&':
        return 'and'
    if c == '||':
        return 'or'


def main():
    for i in range(int(input())):
        line = input()
        line = (re.sub("\s\|\|\s", ' or ', line))
        line = (re.sub("\s&&\s", ' and ', line))
        print(line)


if __name__ == '__main__':
    main()
