"""Password with error checking prac_02"""

MINIMUM_LENGTH = 5


def main():
    password = get_password()

    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be Longer that {MINIMUM_LENGTH} characters")
        password = get_password()

    print_star(password)


def print_star(password: str):
    """Print *'s the length of password"""
    print("*" * len(password))


def get_password() -> str:
    """Get Password from user"""
    password = str(input("Set Password: "))
    return password


main()
