"""
CP1404/CP5632 - Practical
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
When will a ValueError occur?
If a float number is entered as either the numerator or denominator.
The numbers entered need to be an integer.

When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when 0 is entered as the denominator.

Could you change the code to avoid the possibility of a ZeroDivisionError?
Add a while loop to add a constraint to the denominator to be greater than 0.

"""
