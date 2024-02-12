number = 100

if number > 1 :
    for i in range(2,number):
        if number % i == 0 :
            print(number,"is not a prime number")
            print(i,"times",number//i, "equals", number)
            break
    else:
        print(number,"Is a prime number")
else:
    print(number,"is not a prime number")