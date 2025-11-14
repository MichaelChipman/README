'''
mini_receipt_calculator.py
This is the week 1 review
Purpose: put everything learned in week 1 into a working project
Author: Michael Chipman
Date: 2025-11-08

Techinical Skills Demonstrated
 - Gathering user input and placing them into variables for calulation and output
 - Defining functions to calculate each item's total and the overall cost, then
   print a neatly formatted reciept showing both items, their prices, quantities, and totals.
   Make sure the pricess are shown with two decimal places, like a real store receipt.
 
'''

item1 = input("Please enter your first purchase item (use only letters)")
item1_price = float(input("Enter the item price (use only numbers)"))
item1_qty = int(input("Enter the quantity purchased (use only numbers)"))

item2 = input("Please enter your second purchase item (use only letters)")
item2_price = float(input("Enter the item price (use only numbers)"))
item2_qty = int(input("Enter the quantity purchased (use only numbers)"))

def total_item_price(item_price, item_qty):
    '''
    calculates the item total price
    Args:
        item_price: stores item price
        item_qty: stores item quantity
    Returns:
        subtotal: item price multiplied by item quanity
    '''
    subtotal = item_price * item_qty
    return subtotal

#show name, price, quantity, and subtotal for first item
print(f"Item: {item1}")
print(f"Price: {item1_price:.2f}$")
print(f"Quantity: {item1_qty}")
item1_subtotal = total_item_price(item1_price, item1_qty)

#used for dynamic border
msg = f"Total price: {item1_subtotal:.2f}$"
print(msg)

#print border between items
print("-" * len(msg))

#show name, price, quanity, and subtotal for second item
print(f"Item: {item2}")
print(f"Price: {item2_price:.2f}$")
print(f"Quantity: {item2_qty}")
item2_subtotal = total_item_price(item2_price, item2_qty)
msg = f"Total price: {item2_subtotal:.2f}$"
print(msg)

# print empty line before total and border
print()

def total_bill(item1_sub, item2_sub):
    total = item1_sub + item2_sub
    msg = f"Total cart price: {total:.2f}$"
    border = "#" * len(msg)
    print(border)
    print(msg)
    print(border)

total_bill(item1_subtotal, item2_subtotal)

# end mini_receipt_calulator.py
