
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