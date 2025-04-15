
# 1. create a shopping cart program
# 2. ask user for item name, price, quantity
# 3. calculate total price
# 4. print total price in fstring
# 5. ask user for discount
# 6. calculate total price after discount
# 7. print total price after discount in fstring
# 8. ask user for tax
# 9. calculate total price after tax
# 10. print total price after tax in fstring
# 11. ask user for shipping
# 12. calculate total price after shipping

# 13. print total price after shipping in fstring
name = "Jewel Osco Shopping Cart Program"
item_name = "Heinz Ketchup"
num1 = 4.49
quantity = 2
number = 8.49
percentage = 15
number1 = 7.2165
percentage1 = 10
decimal_percentage1 = percentage1 / 100
decimal_percentage = percentage / 100
Shipping = 3.49
number2 = 6.27835
total_price = 9.49
print(f"{item_name} is {num1}")
print(f" for {quantity} {item_name} it is") 
print("-----")
print(int(num1) + num1)
print("-----")
print(" total price is 8.49 ")
print("Since you are a first-time user,")
print("you recieve 15% off your first order.")
print("your new total is,")
print("-----")
print(int(num1) + (num1) - number * decimal_percentage)
print("-----")
print("After tax your total is,")
print("-----")
print(int(7.2165) - number1 * decimal_percentage1)
print("-----")
print("After shipping, your total is,")
print(int(number2) + Shipping)
print(f"For {quantity} {item_name} your total price is {total_price}")
