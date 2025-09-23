"""Password with error checking
prac_02"""

get_password = str(input("Set Password: "))
minimum_length = 5

while len(get_password) < minimum_length:
    print(f"Password must be Longer that {minimum_length} characters")
    get_password = str(input("Set Password: "))

print("*" * len(get_password))
