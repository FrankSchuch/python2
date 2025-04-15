# if conditionals
# if statements are used to check if a condition is true or false
# if condition is true, do something
# if condition is false, do something else

# if conditional statements always start with if 
# and depend on a boolean value (true or false)
# example
classStarted = True #boolean variable
if classStarted:
    print("class has started")
else: 
    print("class has not started")

#logical and comparison operators
# == equal to
# ! not equal to 
# > greater than
# < less than
# >= greater than or equal to 
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
    age = 18
    if age>= 18:
        print("you are an adult")
    elif age == 17:
        print("you are almost an adult")
    else: 
        print("you are a minor")
# problem set #2
# 1. create a program that checks if a number
# is even or odd
# 2. ask user for a number
number = int(input("what is your number?"))
#3. check if number is even or odd
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")