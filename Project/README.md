# PC Inventory System

A simple **console-based PC Inventory System** built in Python using core concepts like lists, dictionaries, functions, and modules.

## Overview

This project simulates a PC components store where a user can browse categories, manage inventory, add items to a cart, update or remove cart items, and checkout to generate a final bill.

## Features

- Categories: Monitor, Keyboard, Mouse, RAM, SSD, Graphic Card, Motherboard, Processor, Cabinet
- Product data stored using **lists and dictionaries**
- Add, display, update, delete, and search products
- Sort products by price
- Add products to cart using Product ID
- Update a cart item by selecting another Product ID from the same category
- Delete items from the cart (inventory stays untouched)
- View cart with running total
- Checkout anytime to generate a final bill and clear the cart
- Clean separation between `main.py` (menu/UI) and `module.py` (logic/data)

## Project Structure

```
PC-Inventory-System/
├── main.py
├── module.py
└── README.md
```

- **main.py** — Displays the main menu and handles category selection.
- **module.py** — Contains inventory data, cart data, and all core functions.

## Product Data

Each product is stored as a dictionary with three fields (no stock field is used in this project):

```python
{
    "PID": 401,
    "PNAME": "8GB DDR4 RAM",
    "PRICE": 1800
}
```

## Data Structures

Inventory is a dictionary of lists of dictionaries:

```python
inventory = {
    "RAM": [
        {"PID": 401, "PNAME": "8GB DDR4 RAM", "PRICE": 1800},
        {"PID": 402, "PNAME": "16GB DDR4 RAM", "PRICE": 3200}
    ]
}
```

The cart is a simple list:

```python
cart = []
```

## CRUD Operations

| Operation | Function | Works On | Purpose |
|-----------|----------|----------|---------|
| Create | `add_product()` | Inventory | Add a new product |
| Read | `display_products()` / `search_product()` | Inventory | View or search products |
| Update | `update_product()` | Cart | Replace a cart item with another product |
| Delete | `delete_product()` | Cart | Remove a product from the cart only |

## Main Functions (module.py)

- `display_products()` — Show all products in a category
- `add_product()` — Add a new product to inventory
- `update_product()` — Replace a cart item with another product from the same category
- `delete_product()` — Remove an item from the cart
- `search_product()` — Search inventory by Product ID
- `sort_by_price()` — Sort products low to high by price
- `add_to_cart()` — Copy a product from inventory into the cart
- `display_cart()` — Show current cart contents and total
- `checkout()` — Generate the final bill and clear the cart
- `category_menu()` — Sub-menu shown for a selected category

## How the Cart Works

**Add to Cart**
```
Inventory → Enter Product ID → Find Product → Copy PID + Name + Price → Add to Cart
```
The original inventory item is not removed.

**Update Cart**

Example — cart currently has:
```
201  Logitech K120        Rs.900
```
User goes to Keyboard → Update → enters `202`:
```
202  HP Wired Keyboard    Rs.750
```
The old item (201) is removed from the cart and the new one (202) is added.

**Delete from Cart**

Removes the item from the cart only — inventory is never modified.

## Checkout

The checkout process:

1. Checks if the cart is empty
2. Displays all cart items
3. Calculates the total price
4. Prints the final bill
5. Clears the cart

Example output:

```
==================== BILL ====================
PID     NAME                              PRICE
------------------------------------------------
401     8GB DDR4 RAM                     Rs.1800
202     HP Wired Keyboard                Rs.750
------------------------------------------------
TOTAL BILL : Rs.2550
================================================
Thank you for shopping with PC Inventory System!
```

## Module Usage

`main.py` imports `module.py` and calls its functions:

```python
import module as a

a.category_menu("RAM")
a.display_cart()
a.checkout()
```

## How to Run

1. Keep `main.py` and `module.py` in the same folder.
2. Run:

```bash
python main.py
```

3. The main menu will appear:

```
==============================================
          PC INVENTORY SYSTEM
==============================================
1. Monitor
2. Keyboard
3. Mouse
4. RAM
5. SSD
6. Graphic Card
7. Motherboard
8. Processor
9. Cabinet
10. View Cart
11. Checkout
12. Exit
==============================================
```

## Technologies Used

- Python
- Lists & Dictionaries
- Functions & Modules
- Loops & Conditional Statements
- CRUD Operations
- Searching & Sorting
- Basic Billing Logic

## Project Objective

This project was built to practice combining core Python concepts — lists, dictionaries, functions, modules, loops, conditionals, CRUD operations, sorting, and searching — into one practical, beginner-friendly console application.
