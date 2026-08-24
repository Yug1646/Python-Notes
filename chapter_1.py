
#! ----- Chapter 1 - Data Types -----
#? Strings
firstName = "Yug"
food = "Pizza"
print(f"{firstName}'s favourite food is {food}")

print(type(firstName))

#? --- String Methods 

#* len - Returns the Length of the string
result = len(firstName)

#* find - Used to find a character in string (Returns Integer)
result = firstName.find("u")

#* rfind - Used to find a character in string from the end (Returns Integer)
result = firstName.find("g")

#* capitalize - Used to capitialize the first character
result = firstName.capitalize()

#* upper - Used to capitialize the whole string
result = firstName.upper()

#* lower - Used to lower the whole string
result = firstName.lower()

#* isdigit - Used to check if string has numbers (Return Boolean)
result = firstName.isdigit()

#* isalpha - Used to check if string has alphabets (Returns Boolean)
result = firstName.isalpha()

#* count - Used to count a character
result = firstName.count("-")

#* replace - Used to replace a character
result = firstName.replace("u","o")

#? --- String Indexing

credit_number = "1234-5678-1646-2006"
last_digit = credit_number[-4:]
rev_credit = credit_number[::-1]

#* Number at specific index
print(credit_number[0])

#* Number from start to end 
print(credit_number[0:4])

#* Starting from 0 till the specified index 
print(credit_number[:9])

#* Everything upto the end
print(credit_number[5:]) 

#* Using negative index
print(credit_number[-1])

#* Using Step
print(credit_number[::3]) 

print(f"XXXX-XXXX-{last_digit}")
print(rev_credit)

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