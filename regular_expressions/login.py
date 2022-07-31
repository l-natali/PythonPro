import re


def login(login):
    pattern = r'^[a-z0-9]{2,10}$'
    match = re.search(pattern, login)
    if match:
        return print(match.group())
    else:
        return print('Login invalid')


login('-8')
