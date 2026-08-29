
#! ----- Chapter 5 - Data Structures: List, Sets, Tuples, Dictionaries -----

#? List: []
fruits = ["Apple","Apple","Banana","Mango","Watermelon","Strawberry","Litchi"]
cart = ["Milk","Chocolate","Shampoo"]

#* Length
print(len(fruits))

#* Accessing Lists
print(fruits[0])

#* Insert 
fruits.insert(0,"Grapes")

#* Append 
fruits.append("Kiwi")

#* Extend 
fruits.extend(cart)

#* Remove
fruits.remove("Shampoo")

#* Pop
fruits.pop(0)
fruits.pop()

#* Del
del fruits[2]
#! del fruits   #Removes whole list

#* Clear
# fruits.clear()

#* Sort
fruits.sort()
fruits.sort(reverse=True)

#* Reverse
fruits.reverse()

#* Count
elementCount = fruits.count("Apple")

#* Index 
elementIndex = fruits.index("Litchi")

print(fruits)
print(elementCount)
print(elementIndex)