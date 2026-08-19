import math

#! ----- Chapter 2 - Math & Operators -----

friends = 5

#? Arithmetic Operators

friends = friends + 1   #* Addition
friends = friends - 1   #* Subtraction
friends = friends * 1   #* Multiplication
friends = friends / 1   #* Division
friends = friends % 1   #* Modules (Remainder)
friends = friends ** 2   #* Exponent
friends = friends // 2   #* Floor Division

#? Augmented Operators

friends +=  1   #* Addition
friends -=  1   #* Subtraction
friends *=  1   #* Multiplication
friends /=  1   #* Division
friends %=  1   #* Modules (Remainder)
friends **=  2   #* Exponent
friends //=  2   #* Floor Division

print(f"You have {friends} friends")

#? Math Functions
x = 3.14
y = -4
z = 5

result = round(x)   #* Round Function       
result = abs(y)     #* ABS Function    
result = pow(4,2)   #* Power Function
result = max(x,y,z) #* Maximum Function
result = min(x,y,z) #* Minimum Function

print(math.pi)          #* Returns the PI value
result = math.sqrt(4)   #* Returns the square root of number
result = math.ceil(4.2) #* rounds a number UPWARD to the nearest integer
result = math.floor(4.9) #* rounds a number Down to the nearest integer
print(result)