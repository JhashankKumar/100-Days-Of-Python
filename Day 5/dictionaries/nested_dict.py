# nested dictionaries

students = {
    "student1": {
        "name": "John",
        "age": 20,
        "major": "Computer Science"
    },
    "student2": {
        "name": "Alice",
        "age": 22,
        "major": "Mathematics"
    },
    "student3": {
        "name": "Bob",
        "age": 21,
        "major": "Physics"
    }
}

print(students["student1"]["name"])  # Output: John
print(students)


child_1 = {
    "name": "Emily",
    "age": 5
}

child_2 = {
    "name": "Michael",
    "age": 3
}

family = {
    "parents": {
        "father": "David",
        "mother": "Sarah"
    },
    "children": {
        "child1": child_1,
        "child2": child_2
    }
}

print(family["parents"]["father"])  # Output: David
print(family["children"]["child1"]["name"])  # Output: Emily
print(family)

# loop through nested dictionaries
for student, details in students.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

for parent, name in family["parents"].items():
    print(f"{parent.capitalize()}: {name}")

for child, details in family["children"].items():
    print(f"{child.capitalize()}: {details['name']}, Age: {details['age']}")

