# This Question is solving using Django  Also

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Item:
    def __init__(self, name, sku_code, price, create_timestamp, created_by):
        self.name = name
        self.sku_code = sku_code
        self.price = price
        self.create_timestamp = create_timestamp
        self.created_by = created_by

class Order:
    def __init__(self, date, item, quantity, ordered_by):
        self.date = date
        self.item = item
        self.quantity = quantity
        self.ordered_by = ordered_by

# Simulated data
user1 = User("John Doe", "john@example.com")
user2 = User("Jane Smith", "jane@example.com")

item_id_23= Item("Samsung ", "SGS21", 999.99, "2023-08-24", user1)
item_id_24 = Item("iPhone 13", "IP13", 1099.99, "2023-08-24", user2)

order1 = Order("2023-08-24", item_id_23, 5, user1)
order2 = Order("2023-08-23", item_id_24, 15, user2)
order3 = Order("2023-08-22", item_id_23, 8, user1)

orders = [order1, order2, order3]

# List the Orders with quantity more than 10
orders_more_than_10 = [order for order in orders if order.quantity > 10]
names_orders_more_than_10 = [order.item.name for order in orders_more_than_10]

# List the Orders which are having "Samsung" in their Item's name
orders_with_samsung = [order for order in orders if "Samsung" in order.item.name]
dates_orders_with_samsung = [order.date for order in orders_with_samsung]

# Print the total sum of the quantity of all orders of the item_id 23
total_quantity_item_23 = sum(order.quantity for order in orders if order.item == item_id_23)

print("Names of orders with quantity more than 10:", names_orders_more_than_10)
print("List  of orders Dates with 'Samsung' in Item name:", dates_orders_with_samsung)
print("Total quantity for item_id 23:", total_quantity_item_23)
