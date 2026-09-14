# main.py

import module as a

while True:
    print("\n")
    print("==============================================")
    print("          PC INVENTORY SYSTEM")
    print("==============================================")
    print("1. Monitor")
    print("2. Keyboard")
    print("3. Mouse")
    print("4. RAM")
    print("5. SSD")
    print("6. Graphic Card")
    print("7. Motherboard")
    print("8. Processor")
    print("9. Cabinet")
    print("10. View Cart")
    print("11. Checkout")
    print("12. Exit")
    print("==============================================")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        a.category_menu("Monitor")
    elif choice == 2:
        a.category_menu("Keyboard")
    elif choice == 3:
        a.category_menu("Mouse")
    elif choice == 4:
        a.category_menu("RAM")
    elif choice == 5:
        a.category_menu("SSD")
    elif choice == 6:
        a.category_menu("Graphic Card")
    elif choice == 7:
        a.category_menu("Motherboard")
    elif choice == 8:
        a.category_menu("Processor")
    elif choice == 9:
        a.category_menu("Cabinet")
    elif choice == 10:
        a.display_cart()
    elif choice == 11:
        a.checkout()
    elif choice == 12:
        print("Thank you for using PC Inventory System.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
