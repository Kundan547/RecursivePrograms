fruits = {'apple': 3, 'banana': 5, 'orange': 2}
print("1. Fruit inventory:", fruits)

fruits['grape'] = 4
print("2. Updated fruit inventory:", fruits)

del fruits['banana']
print("3. Inventory after removing banana:", fruits)

key = 'apple'
if key in fruits:
    print(f"4. {key} is in the inventory with quantity: {fruits[key]}")
else:
    print(f"4. {key} is not in the inventory")

print("5. Current inventory:")
for fruit, quantity in fruits.items():
    print(f"   {fruit}: {quantity}")

def add_fruit(inventory, fruit, quantity):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory

def remove_fruit(inventory, fruit, quantity):
    if fruit in inventory:
        if inventory[fruit] <= quantity:
            del inventory[fruit]
        else:
            inventory[fruit] -= quantity
    return inventory

def display_inventory(inventory):
    print("Current Inventory:")
    for fruit, quantity in inventory.items():
        print(f"{fruit}: {quantity}")

inventory = {}
inventory = add_fruit(inventory, 'apple', 5)
inventory = add_fruit(inventory, 'banana', 3)
inventory = add_fruit(inventory, 'orange', 2)

display_inventory(inventory)

inventory = remove_fruit(inventory, 'apple', 2)
inventory = add_fruit(inventory, 'grape', 4)

display_inventory(inventory)