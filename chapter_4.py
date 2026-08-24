
#! ----- Chapter 4 - Loops -----

#? While loop

food = input("Enter your favourite food (q to Quit): ")

while not food == "q":
    food = input("Enter your another favourite food (q to Quit): ")
    print(f"Your favourite food: {food}")

print("Thankyou")