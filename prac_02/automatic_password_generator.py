import random

SPECIAL_CHARACTERS = "!@#$%^&*+~?"

def main():
    upper_amount = int(input('Enter uppercase amount >: '))
    numeric_amount = int(input('Enter numeric amount >: '))
    special_amount = int(input('Enter specials amount >: '))
    total_amount = upper_amount + numeric_amount + special_amount

    length = int(input('Enter desired password length >: '))
    while True:
        if length < total_amount:
            print('Desired password length cannot be less than amount of nessacary characters.')
            length = int(input('Enter desired password length >: '))
        else:
            break
    password = []
    for i in range(upper_amount):
        password.append(chr(random.randint(65, 90)))
    for i in range(numeric_amount):
        password.append((chr(random.randint(48,57))))
    for i in range(special_amount):
        password.append(random.choice(SPECIAL_CHARACTERS))
    for i in range(total_amount, length):
        password.append(chr(random.randint(97, 122)))

    new_password = "".join(random.sample(password, len(password)))
    print(new_password)
def get_valid_amount(string):
    """Get a number that isn't higher than the length of the password or other requirements combined"""


main()