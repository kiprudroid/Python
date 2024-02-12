number = 0

if number > 1 :
    for i in range(2,number):
        if number % i == 0:
            print(number ,"is  a not prime number")
            print(i,"times", number//i, "equals",number)
            break
    else:
        print(number,"is a prime number")
            
else:
    print(number,"is a prime number")

