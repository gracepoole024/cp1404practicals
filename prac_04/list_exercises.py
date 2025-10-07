"""
CP1404/CP5632 Practical 4
Basic list operations, and woefully inadequate security checker
"""

# Basic list operations
numbers = []
for i in range(5):
    numbers = int(input("Numbers: "))
    numbers.append(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter Username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")
