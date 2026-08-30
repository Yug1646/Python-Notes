
#! ----- Chapter 6 - Functions -----


#? Normal Function
def message():
    print("Hello World !")
message()

#? Function with Arguments
def happy_birthday(personName,years):
    print(f"Happy birthday {personName}")
    print(f"You are {years} old")
happy_birthday("Yug",21)

#? Return Function
def add(x,y):
    return x + y
result = add(5,6)
print(result)


#? Default Arguments
def stud_details(stud_name, branch = "CS", dept = "B.Tech"):
    return {
        "Student Name" : stud_name,
        "Branch" : branch,
        "Department" : dept
    }
print(stud_details("Tony"))


#? Keyword Arguments
def greetings(msg,firstName,middleName,lastName):
    return msg + " " + firstName + " " + middleName + " " + lastName
greetUser = greetings("Hello", firstName = "Tony", lastName = "Stark", middleName = "Howard")
print(greetUser)

#? Arbitary Arguments

#* *args
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(f"Sum : {add(1,2,3,4,5)}")

#* **kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_address(street = "123 Fake ST.",
            apt = "100",
            city = "NYC",
            state = "W. DC",
            zip = "1646")