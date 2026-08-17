
#! ----- Chapter 1 - Data Types -----
#? Strings
firstName = "Yug"
food = "Pizza"
print(f"{firstName}'s favourite food is {food}")

print(type(firstName))

#? Integer
age = 20
print(f"Age of {firstName} is {age}")

#? Float
gpa = 9.8
price = 12.99
print(f"{firstName}'s GPA is {gpa}")
print(f"Price of {food} is ${price}")

#? Boolean
isStudent = True
isChild = False
print(f"Is {firstName} a student: {isStudent}")
print(f"Is {firstName} a child: {isChild}")

#? Typecasting
isUsernameGiven = bool(firstName)
exactAge = float(age)
overallGPA = int(gpa)
strPrice = str(price)

print(f"Is user's name given: {isUsernameGiven}")
print(f"What's the overall GPA: {overallGPA}")

#? Input
fullName = input("Enter your full name: ")
userWeight = int(input("Enter your weight: "))    #* This is typecasting the String to Integer
print(f"You are {fullName} and you weigh {userWeight} KG")