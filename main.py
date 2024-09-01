# Import the classes
from menu_item import MenuItem
from menu_manager import MenuManager

# Create new items and save them to the database
item1 = MenuItem('Burger', 35)
item1.save()
print("Saved 'Burger' item.")

item2 = MenuItem('Beef Stew', 50)
item2.save()
print("Saved 'Beef Stew' item.")

# Update the item's name and price
item1.update('Veggie Burger', 37)
print("Updated 'Burger' to 'Veggie Burger'.")

# Get an item by name
item3 = MenuManager.get_by_name('Beef Stew')
if item3:
    print(f'Found item: {item3.item_name}, Price: {item3.item_price}')
else:
    print('Item not found.')

# Get all items
items = MenuManager.all_items()
if items:
    for i in items:
        print(f'Item: {i.item_name}, Price: {i.item_price}')
else:
    print('No items found in the database.')