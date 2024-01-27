students = { }

for i in range(3):
    number = input("Enter student number " + str(i+1) + ": ")
    name = input("Enter first name " + str(i+1) + ": ")
    students[number] = name

snumber = []
for x, y in students.items():
    print(x, y)
    snumber.append(x)

del students[snumber[2]]

number = input("Enter student number 3: ")
name = input("Enter first name 3: ")
students[number] = name

for x, y in students.items():
    print(x, y)
