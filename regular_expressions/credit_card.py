import re


def card_number(number):

    visa = r'(^4\d{3} \d{4} \d{4} \d{4}$)|(^4\d{15}$)|(^4\d{3}-\d{4}-\d{4}-\d{4}$)'
    mastercard = r'(^5\d{3} \d{4} \d{4} \d{4}$)|(^5\d{15}$)|(^5\d{3}-\d{4}-\d{4}-\d{4}$)'
    matchv = re.search(visa, number)
    matchm = re.search(mastercard, number)
    if matchv:
        return print('Number card is valid, payment system - Visa')
    elif matchm:
        return print('Number card is valid, payment system - MasterCard')
    else:
        return print('Number card is not valid')


card_number(input('Input card number:\n'))
