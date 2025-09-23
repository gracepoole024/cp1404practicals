"""Password with error checking prac_02"""

MINIMUM_LENGTH = 5


def main():
    password = get_name()

    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be Longer that {MINIMUM_LENGTH} characters")
        password = get_name()

    print_star(password)


def print_star(password: str):
    print("*" * len(password))


def get_name() -> str:
    password = str(input("Set Password: "))
    return password


main()
