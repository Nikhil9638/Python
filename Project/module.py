# module.py

# PC Inventory data
inventory = {
    "Monitor": [
        {"PID": 101, "PNAME": "Dell 24 Inch Monitor", "PRICE": 8500},
        {"PID": 102, "PNAME": "LG 22 Inch Monitor", "PRICE": 7000},
        {"PID": 103, "PNAME": "Samsung 24 Inch Monitor", "PRICE": 9500}
    ],
    "Keyboard": [
        {"PID": 201, "PNAME": "Logitech K120", "PRICE": 900},
        {"PID": 202, "PNAME": "HP Wired Keyboard", "PRICE": 750},
        {"PID": 203, "PNAME": "Redragon Mechanical Keyboard", "PRICE": 2500}
    ],
    "Mouse": [
        {"PID": 301, "PNAME": "Logitech M90", "PRICE": 600},
        {"PID": 302, "PNAME": "HP Wireless Mouse", "PRICE": 900},
        {"PID": 303, "PNAME": "Redragon Gaming Mouse", "PRICE": 1800}
    ],
    "RAM": [
        {"PID": 401, "PNAME": "8GB DDR4 RAM", "PRICE": 1800},
        {"PID": 402, "PNAME": "16GB DDR4 RAM", "PRICE": 3200},
        {"PID": 403, "PNAME": "32GB DDR4 RAM", "PRICE": 6500}
    ],
    "SSD": [
        {"PID": 501, "PNAME": "500GB SATA SSD", "PRICE": 3000},
        {"PID": 502, "PNAME": "1TB NVMe SSD", "PRICE": 5500},
        {"PID": 503, "PNAME": "2TB NVMe SSD", "PRICE": 10500}
    ],
    "Graphic Card": [
        {"PID": 601, "PNAME": "GTX 1650 4GB", "PRICE": 15000},
        {"PID": 602, "PNAME": "RTX 3060 12GB", "PRICE": 28000},
        {"PID": 603, "PNAME": "RTX 4060 8GB", "PRICE": 32000}
    ],
    "Motherboard": [
        {"PID": 701, "PNAME": "MSI B550 Motherboard", "PRICE": 9500},
        {"PID": 702, "PNAME": "Gigabyte B760 Motherboard", "PRICE": 12500},
        {"PID": 703, "PNAME": "ASUS Z790 Motherboard", "PRICE": 28000}
    ],
    "Processor": [
        {"PID": 801, "PNAME": "Intel Core i5", "PRICE": 15000},
        {"PID": 802, "PNAME": "Intel Core i7", "PRICE": 28000},
        {"PID": 803, "PNAME": "AMD Ryzen 7", "PRICE": 25000}
    ],
    "Cabinet": [
        {"PID": 901, "PNAME": "Ant Esports Cabinet", "PRICE": 3500},
        {"PID": 902, "PNAME": "Corsair Gaming Cabinet", "PRICE": 7000},
        {"PID": 903, "PNAME": "Cooler Master Cabinet", "PRICE": 8500}
    ]
}

cart = []


def display_products(category):
    print("\n---------------- PC INVENTORY ----------------")
    print("PID     NAME                              PRICE")
    print("------------------------------------------------")
    for p in inventory[category]:
        print(f'{p["PID"]:<7} {p["PNAME"]:<33} Rs.{p["PRICE"]}')
    print("------------------------------------------------")


def add_product(category):
    pid = int(input("Enter Product ID: "))

    for p in inventory[category]:
        if p["PID"] == pid:

            product = {
                "PID": p["PID"],
                "PNAME": p["PNAME"],
                "PRICE": p["PRICE"]
            }

            cart.append(product)

            print("Product added to cart.")
            return

    print("Product not found.")

def update_product(category):
    print("\n========== UPDATE PRODUCT ==========")

    # Display products of selected category
    display_products(category)

    pid = int(input("Enter Product ID to add: "))

    # Find the selected product in inventory
    for p in inventory[category]:
        if p["PID"] == pid:

            # Remove old product of the same category from cart
            for item in cart:
                if item["PID"] // 100 == pid // 100:
                    cart.remove(item)
                    break

            # Add selected product to cart
            cart_item = {
                "PID": p["PID"],
                "PNAME": p["PNAME"],
                "PRICE": p["PRICE"]
            }

            cart.append(cart_item)

            print("Product updated successfully.")
            return

    print("Product not found.")


def delete_product(category):
    pid = int(input("Enter Product ID to delete: "))

    for item in cart:
        if item["PID"] == pid:
            cart.remove(item)
            print("Product removed from cart successfully.")
            return

    print("Product not found in cart.")


def search_product(category):
    pid = int(input("Enter Product ID to search: "))

    for p in inventory[category]:
        if p["PID"] == pid:
            print("\nProduct Found")
            print("ID    :", p["PID"])
            print("Name  :", p["PNAME"])
            print("Price :", p["PRICE"])
            return

    print("Product not found.")


def sort_by_price(category):
    inventory[category].sort(key=lambda x: x["PRICE"])
    print("Products sorted by price (Low to High).")
    display_products(category)

def add_to_cart(category):
    pid = int(input("Enter Product ID to purchase: "))

    for p in inventory[category]:

        if p["PID"] == pid:

            cart_item = {
                "PID": p["PID"],
                "PNAME": p["PNAME"],
                "PRICE": p["PRICE"]
            }

            cart.append(cart_item)

            print("Product added to cart.")
            return

    print("Product not found.")



def checkout():
    if len(cart) == 0:
        print("\nCart is empty. Add products before checkout.")
        return

    print("\n==================== BILL ====================")
    print("PID     NAME                              PRICE")
    print("------------------------------------------------")

    grand_total = 0

    for item in cart:
        print(
            f'{item["PID"]:<7} '
            f'{item["PNAME"]:<33} '
            f'Rs.{item["PRICE"]}'
        )

        grand_total += item["PRICE"]

    print("------------------------------------------------")
    print("TOTAL BILL : Rs.", grand_total)
    print("================================================")
    print("Thank you for shopping with PC Inventory System!")

    cart.clear()

def display_cart():
    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\n==================== YOUR CART ====================")
    print("PID     NAME                              PRICE")
    print("------------------------------------------------")
    total = 0
    for item in cart:
        print(f'{item["PID"]:<7} {item["PNAME"]:<33} Rs.{item["PRICE"]}')
        total += item["PRICE"]
    print("------------------------------------------------")
    print("Cart Total : Rs.", total)
    print("==================================================")
    
def category_menu(category):
    while True:
        print(f"\n========== {category.upper()} MENU ==========")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Sort by Price")
        print("7. Buy / Add to Cart")
        print("8. View Cart")
        print("9. Checkout")
        print("10. Back to Main Menu")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            display_products(category)
        elif choice == 2:
            add_product(category)
        elif choice == 3:
            update_product(category)
        elif choice == 4:
            delete_product(category)
        elif choice == 5:
            search_product(category)
        elif choice == 6:
            sort_by_price(category)
        elif choice == 7:
            add_to_cart(category)
        elif choice == 8:
            display_cart()
        elif choice == 9:
            checkout()
        elif choice == 10:
            break
        else:
            print("Invalid choice.")
