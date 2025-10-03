# Create a function named calculate_discount(price, discount_percent) that calculates 
# the final price after applying a discount. The function should take the original price 
# (price) and the discount percentage (discount_percent) as parameters. If the discount 
# is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        d_price = price * (discount_percent/100)
        new_price = price - d_price
        return new_price
    else:
        return price

print(calculate_discount(100,18))

#Using the calculate_discount function, prompt the user to enter the original 
#price of an item and the discount percentage. Print the final price after 
# applying the discount, or if no discount was applied, print the original price.

try:
    price = float(input("Enter Price: "))
    d_price = float(input("Enter discount(%): "))


    cost = calculate_discount(price, d_price)
    if d_price < 20:
        print(f"Ohps! No discount charge for you. Your total cost is {cost.2f}")
    else:
        print(f"Discount awarded. Your total cost is {cost.2f}")
        
except ValueError:
    print("Invalid input! Please enter numeric values only.")
