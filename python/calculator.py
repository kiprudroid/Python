#create a calculator code in which i input the first number the second number and the operator and it gives me the result
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == "+":
    print("Result is: ",x+y)
elif operator == "-":
    print("Result is: ",x-y)
elif operator == "*":
    print("Result is: ",x*y)
elif operator == "/":
    print("Result is: ",x/y)
else:
    print("Invalid operator")




