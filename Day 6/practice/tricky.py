a = "33"
b = "200"
"""
for a = 33 and b = 200, the output will be:
b is greater than a

for a = "200" and b = "33", the output will be:
none of the above
"""
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a < b:
    print("a is less than b")
else:
    print("none of the above")

# string comparison
a = "200"
b = "33"
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a < b:     
    print("a is less than b")
else:    
    print("none of the above")


# number comparison
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:    
    print("a and b are equal")
elif a < b:     
    print("a is less than b")
else:    
    print("none of the above")

a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:    
    print("a and b are equal")
elif a < b:     
    print("a is less than b")
else:    
    print("none of the above")
    
# while loop with break and continue statements
count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1