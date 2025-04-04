#there are different types of variables
#strings are text
name = "John" #quotation marks
name2 = "Lucy"
# integers are whole numbers
num1 = 10 #no quotation marks
num2 = 20
print(int(num1) + num2) #when you have a plus sign between two variables it's called concatenation
# print(name +"and"+ name2 + "have"+ num1 + str(num2) + "apples")
# f strinmgs allow us to insert variables into strings
# using f before the string
print(f"{name} and {name2} have {num1} apples")
# floats are decimals
dollars = 10.99
#it can be positive or negative 
print(f"{name} has {dollars} dollars")
# booleans are true or false
is_student = True
print(f"{name} is a student: {is_student}")
# lists are collections of values
# dictionaries are collections of key-value pairs
#problem set #1
#1. Create 5 different variables
#2 print them out
#3. use f strings to format the strings
name3 = "Benji"
name4 = "Frank"
num3 = 5
num4 = 10
is_bad = True
print(f"{name3} has {num3} trophies. {name4} has {num4} trophies. Benji is bad at volleyball: {is_bad}")