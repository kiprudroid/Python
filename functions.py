#In Built Functions
number = max(1,3,45)
print(number)

x = min(36,54,75,532,23,45,67,7)

print(x)

#User defined function

def name(n):
    print("My name is ,",n)

name("shadrack")              #Calling a function

#one student
def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name,age,course)


def students(name,age, course):
    print(name,age,course)

student()

students("Shadrack" , 16 ,"MIT")
students("Victor" , 18 ,"Cyber security")
students("Shadrack" , 19 ,"Artificial Intelligence")