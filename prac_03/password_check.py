MINIMUM_LENGTH = 6


def main():
    password = get_password()
    method_name(password)


def method_name(password):
    print('*' * len(password))


def get_password():
    password = input('Enter password: ')
    while len(password) < MINIMUM_LENGTH:
        print(f'Password must be at least {MINIMUM_LENGTH} characters long.')
        password = input('Enter password: ')
    return password


main()
