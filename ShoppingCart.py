# Shopping Cart Program
# Initialize an empty shopping cart list
shopping_cart = []
# Welcome message
print("Welcome to the Shopping Cart program!")
while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Add item")
    print("2. Display items")
    print("3. Calculate total cost")
    print("4. Exit")
    
    # Get the user's choice
    choice = input("\nEnter your choice: ")
    
    # Add item to the shopping cart
    if choice == "1":
        name = input("\nInput the item's name: ")
        price = input("\nInput item's price: ")
        quantity = input("\nHow many of the item: ")
        
        item = {"name": name, "price": price, "quantity": quantity}
        shopping_cart.append(item)
        print("Item added successfully.")
        
    # Display the items in the shopping cart
    elif choice == "2":
            print("\nCurrent items in the shopping cart:")
            for item in shopping_cart:
                print(f"{item['quantity']}x {item['name']} at ${item['price']} each")
            
    # Calculate the total cost of items in the shopping cart
    elif choice == "3":
        total_cost = 0
        for item in shopping_cart:
            total_cost += int(item['quantity']) * float(item['price'])
        print("\nTotal cost of items: $" + str(total_cost))
        
    # Exit the program
    elif choice == "4":
        print("Goodbye!")
        break
    
    # Handle invalid choices
    else:
        print("Invalid choice. Please try again.")