# nested if 

age = 20
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior")
else:
    print("Minor")

# nested if with multiple conditions
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    if marks >= 85:
        print("Grade: B+")
    else:
        print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# driving eligibility
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("You are eligible to drive.")
    else:
        print("You need a valid driver's license to drive.")    
else:
    print("You are not eligible to drive.")

# multiple nested if statements
number = 15
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# nested vs logical operators
age = 20
has_license = True
if age >= 18 and has_license:   
    print("You are eligible to drive.")
else:    print("You are not eligible to drive.")

# login validation
username = "admin"
password = "password123"
if username == "admin":
    if password == "password123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:    print("Username not found.")