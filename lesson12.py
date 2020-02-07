user_items_number = int(input("Input the number of items you want to buy: "))
user_prefered_items = []
market_stock = ["apple", "ice-cream", "banana"]
user_available_items = []

for i in range(user_items_number):
	item = input("Enter item name you want to buy: ")
	user_prefered_items.append(item)

for item in user_prefered_items:
	if item in market_stock:
		user_available_items.append(item)

print(user_available_items)
