email_to_name = {}
email = input("Email: ")
while email != "":
    modified_email = email.replace(",", " ").replace(".", " ")
    name = " ".join([char for char in (modified_email[:modified_email.find("@")].split()) if not char.isdigit()]).title()
    confirm = input(f"Is your name {name}? (Y/n)").lower()
    if confirm == 'y' or "":
        email_to_name[email] = name
    elif confirm == 'n' or 'no':
        name = input('Name: ')
        email_to_name[email] = name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} {email}")