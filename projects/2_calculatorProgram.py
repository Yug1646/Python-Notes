
#! Calculator Program

operator = input("Enter Operator (+,-,*,/): ")

num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

if operator == "+":
    print(f"Addition: {num1+num2}")
elif operator == "-":
    print(f"Subtraction: {num1-num2}")
elif operator == "*":
    print(f"Multiplication: {num1*num2}")
elif operator == "/":
    print(f"Division: {num1/num2}")
else:
    print("Invalid Operator")
