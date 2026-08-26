
#! ----- Chapter 4 - Loops & Control Statements -----

#? While loop

food = input("Enter your favourite food (q to Quit): ")

while not food == "q":
    food = input("Enter your another favourite food (q to Quit): ")
    print(f"Your favourite food: {food}")

print("Thankyou")

#? For Loop
cart = ["Apple","Milk","Banana","Chocolate"]

for i in range(1,11):
    print(i)    # Prints from 1 - 10

for i in reversed(range(1,11)):
    print(i)    # Prints from 10 - 1

for i in range(1,11,2):
    print(i)    

for item in cart:
    print(item)

#? Break Statement
for i in range(1,11):
    if i == 5:
        break
    print(i)

#? Continue Statement
for i in range(1,11):
    if i == 5:
        continue
    print(i)