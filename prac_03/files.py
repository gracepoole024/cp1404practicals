# 1
out_file = open("name.txt", 'w')
name = input("Enter Name: ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Hi {name}")
in_file.close()

# 3
with open("numbers.txt", 'r') as in_file:
    number_01 = int(in_file.readline())
    number_02 = int(in_file.readline())
print(number_01 + number_02)

# 4
lines = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        lines += number
print(lines)
