user_name = str(input("Enter Name: "))

MENU = """(H)ello\n(G)oodbye\n(Q)uit"""
print(MENU)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"hello {user_name}")
    elif choice == "G":
        print(f"goodbye {user_name}")
    else:
        print("Invalid Choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
