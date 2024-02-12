# temperature = 25
# if temperature > 25 :
#   #  print("It is Hot")
# if temperature == 25 :
#   #  print("Room temperature")
# # else:
#    # print("It is Cold")

# # A program that returns the largest number among three numbers

# num1 = 6
# num2 = 58
# num3 = 58.5

# if num1 > num2 and num1 > num3 :
#     #print(num1 ,"is the largest number")
# elif num2 > num1 and num2 > num3:
#    #  print(num2 ,"is the largest number")
# else:
#    # print(num3,"Is the largest number")

# # A Program that checks whether a number is even or odd

# number = 71

# if number % 2 == 0:
#    # print(number," is Even")
# else:
#   #  print(number ,"is odd")


#prime or not
number = 4

if number > 1:
# check for factors
    for i in range(2,number):
        if (number % i) == 0:            
            print(number,"is not a prime number")
            print(i,"times",number//i,"is",number)
            
            break
    else:
        print(number,"is a prime number")
          
else:

# if input number is less than
# or equal to 1, it is not prime
    print(number,"is not a prime number")