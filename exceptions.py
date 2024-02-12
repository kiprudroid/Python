try:
    print(x)
    
except:
    print("Name Error occured")
finally:
    print('success')
  


num1 =20
num2 = 0

try:
    print(num1/num2)
except:
    print('ZeroDivisionError occured')

try:
    def multiply(x,y):
        return x*y
except:
    print("Exception occured")
finally:
    print("success")

print(multiply(10,20))
