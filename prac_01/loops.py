# a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Number of Stars: "))

for i in range(number_of_stars):
    print('*', end=' ')
print()

# d
number_of_lines = int(input("Number of Lines: "))

for i in range(1, number_of_lines + 1):
    print('*' * i)
print()
