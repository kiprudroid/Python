#data types
number = 45 #int
num = 56.78 #float

greeting = "hello there" #str

isPythonInteresting = True #bool

#variables storing multiple values

languages = ["Python" ,"PHP", "Kotlin" , "C"]  #lists

fruits = ("apple","banana","pineapple") #tuples
countries = {"Kenya","Uganda","USA"} #set

#Dictionary
details = {
    "FirstName" : "Grace",
    "Age" : 17,
    "Course": "MIT",
    "Nationality" : "Kenyan"
}

print(countries)
print(isPythonInteresting)
print(details["Age"])

#determining the data type
print(type(details))

#Type casting - coverting one data type to another

print(float(number))

print(int(num))

#rounding off
print(round(num))


