students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 70
}

name = input("Enter the student's name: ")

if name in students:
    print(name + "'s marks:", students[name])
else:
    print("Student not found.")