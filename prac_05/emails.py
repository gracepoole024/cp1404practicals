"""
CP1404/CP5632 Practical 5
Emails Program
"""

"""
Emails
Estimate: 30 minutes
Actual:   33 minutes
"""


def main():
    email = input("Enter email: ")
    email_to_name = {}
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation == 'n':
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


main()
