
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

#? Sets: {}

cart = {"Milk","Milk","Chocolate","Fruits","Vegetables","Screwdriver","Tester"}
fruits = ["Mango","Coconut"]

set1 = {"a", "b", "c"}
set2 = {"a", 2, 3}

#* Add
cart.add("Frames")

#* Update
cart.update(fruits)

#* Remove
cart.remove("Tester")

#* Discard
cart.discard("Screwdriver")

#* Clear
cart.clear()

print(cart)

#* Union
set3 = set1.union(set2)
set3 = set1 | set2

#* Intersection
set3 = set1.intersection(set2)
set3 = set1 & set2

#* Difference
set3 = set1.difference(set2)
set3 = set1 - set2

#* Symmetric Differences
set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2

print(set3)


#? Tuples : ()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

#* Count
result = thistuple.count(5)

#* Index
result = thistuple.index(8)

print(result)