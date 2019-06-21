from itertools import groupby
import re


def main():
    for i in range(int(input())):
        card_no = input()

        if len(re.findall('[^0-9-]', card_no)) == 0:
            if '-' in card_no:
                card_no = card_no.split('-')
                # Checking for pair of 4 digits
                if len(card_no) == 4:
                    if len(card_no[0]) == len(card_no[1]) == len(card_no[2]) == len(card_no[3]):
                        card_no = ''.join(card_no)
                        validate_card(card_no)
                    else:
                        # Not a pair of 4 digits
                        print('Invalid')
                else:
                    # More than 4 pairs
                    print('Invalid')
            else:
                # Card No not group in 4
                validate_card(card_no)
        else:
            # Characters other than digits and - seperators
            print('Invalid')


def validate_card(card_no):
    if len(card_no) == 16 and card_no[0] in ['4', '5', '6']:
        # Checking for consecutive repeated digits
        groups = groupby(card_no)
        repeat = [(label, sum(1 for _ in group)) for label, group in groups]

        if max(repeat, key = lambda x: x[1])[1] >= 4:
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()