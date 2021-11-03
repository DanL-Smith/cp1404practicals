"""
CP1404/CP5632 Practical
Emails
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (y/n)").lower()
        if confirm != 'y' and confirm != '':
            name = input('Name: ')
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    modified_email_string = email.replace(",", " ").replace(".", " ")
    names_split = modified_email_string[:modified_email_string.find("@")].split()
    full_name_string = " ".join(names_split).title()
    return full_name_string


if __name__ == '__main__':
    main()
