
#! ----- Chapter 3 - Conditional Statements -----

#? IF, ELIF, ELSE statments

age = int(input("Enter age: "))

if age >= 65:   
    print("You are Senior Citizen")
elif age >= 18:
    print("You are Adult")
elif age < 18:
    print("You are Child")
else:
    print("Enter valid Age")