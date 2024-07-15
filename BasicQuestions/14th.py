#Finding Unique Items in Collections by using Differene() or "-" operator
purchased_ids = {100, 202, 314}
all_customer_ids = {100, 202, 314, 401, 523}

potential_customers = all_customer_ids.difference(purchased_ids)
print(potential_customers)  


#Comparing Inventory and Orders
inventory = {"shirt_S", "shirt_M", "pants_L"}
orders = {"shirt_S", "shirt_M", "pants_XL"}

out_of_stock = orders.difference(inventory)
print(out_of_stock)  
