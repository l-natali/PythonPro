import re


def mail_validation(mail):
    # pattern = r'^[^-_](a-z)|(A-Z)|(0-9)|@\w+\.\w+$'
    pattern = r'^[^-_][a-zA-Z0-9_-]+@\w+\.\w+$'
    match = re.search(pattern, mail)
    if match:
        return print('Valid')
    else:
        return print('Invalid')


mail_validation('_j6j@gh.bh')
