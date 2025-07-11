products = {}

while True:
    print("\n1. Add product")
    print("2. Update price")
    print("3. Find products by price range")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter product name to add: ")
        if name in products:
            print("Product already exists.")
        else:
            price = float(input("Enter price: "))
            products[name] = price
            print("Product added.")

    elif choice == '2':
        name = input("Enter product name to update: ")
        if name in products:
            price = float(input("Enter new price: "))
            products[name] = price
            print("Price updated.")
        else:
            print("Product not found.")

    elif choice == '3':
        low = float(input("Enter minimum price: "))
        high = float(input("Enter maximum price: "))
        found = False
        for name in products:
            price = products[name]
            if low <= price <= high:
                print(name, ":", price)
                found = True
        if not found:
            print("No products found in this range.")

    elif choice == '4':
        break

    else:
        print("Invalid choice.")
