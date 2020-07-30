no_of_items = int(input("Number of items:"))
total_price = 0
while no_of_items < 0:
    print("Invalid entry")
    no_of_items = int(input("Number of items:"))
for i in range(no_of_items):
    price = float(input("Price of item:"))
    total_price += price
if total_price > 100:
    total_price = total_price*0.9
print("Total price for {} item(s) is ${:.2f}".format(no_of_items, total_price))





