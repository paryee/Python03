# working with tuple

fruits = ("orange", "mango", "banana", "sweet apple", "kiwi", "cherry", "pineaples", "water mellon")
print(type (fruits))

# accessing your tuple items

# fruits = ("orange", "mango", "banana", "sweet apple", "kiwi", "cherry", "pineaples", "water mellon")

# print(fruits[3:5])

# fruits =("orange", "mango", "banana", "sweet apple", "kiwi", "cherry", "pineaples", "water mellon")
# fruits.insert(2, strawberry)
# print(fruits)

# # add to tuples
fruits = ("orange", "mango", "banana", "sweet apple", "kiwi", "cherry", "pineaples", "water mellon")
y = list(fruits)
y.append("strawberry")
fruits = tuple(y)
print(fruits)

# Dictionaries

student = {
    "name" : "Rafique",
    "country" : "Ghana",
    "sex" : "Male",
    "city" : "Kumasi"
}
print(student)

# accessing your dictionary

student = {
    "name" : "Rafique",
    "country" : "Ghana",
    "sex" : "Male",
    "city" : "Kumasi"
}
print(student["country"])

# update dictionaries

student = {
    "name" : "Rafique",
    "country" : "Ghana",
    "sex" : "Male",
    "city" : "Kumasi"
}
student.update({"city" : "Accra"})
print(student)

# conditional statement
# if statement

a = 33
b = 200
if b > a:
    print("b is greater than a")

    # elif condition

    a = 33
    b = 33
    if b > a :
        print("b is greater than a")
    elif a == b:
        print("a and b are the equal")

        # else statement

        a = 200
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
        else:
            print("a is greater than b")

# else with if statemen

a = 200
b= 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

    # And keyword

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("both conditions are true")

    # or statement
    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("at least one of the conditions is true")

#  Tutorial
tutorial = [("Ruth",85),("Beldwin",90),("Emmory",95),("Nelson",91),("Temesgen",80),("Rafique",89),("Samuel",81),("Prince",83)]
# Dict
tutorial_data ={}

# Iterate over the each student tuple
for name, grade in tutorial:
    if grade >= 90:
        tutorial_data[name] = "A"
    elif grade >= 80:
        tutorial_data[name] = "B"
    elif grade >= 70:
        tutorial_data[name] = "C"
    else:
        tutorial_data[name] = "D"
# Print the data
for name, grade in tutorial_data.items():
    print(f"{name} : {grade}")


    
