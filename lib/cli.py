from helpers import (
    exit_program,
    list_categories,
    create_category,
    update_category,
    delete_category,
    list_products,
    find_product_by_name,
    create_product,
    update_product,
    delete_product,
    list_category_products,
    calculate_total_category_cost,
    calculate_total_inventory_cost,
)


def main():
    print("Welcome to StoreIM Store Manager. What do you want to do today?\n")
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_category()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            update_category()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            create_product()
        elif choice == "6":
            update_product()
        elif choice == "7":
            delete_product()
        elif choice == "8":
            list_products()
        elif choice == "9":
            find_product_by_name()
        elif choice == "10":
            list_category_products()
        elif choice == "11":
            calculate_total_category_cost()
        elif choice == "12":
            calculate_total_inventory_cost()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1: Add category")
    print("2. List all categories")
    print("3: Update a category")
    print("4: Delete a category from the inventory")
    print("5: Add a product to the inventory")
    print("6: Update product")
    print("7: Delete a product from the inventory")
    print("8. List all products in the inventory")
    print("9. Search product by name")
    print("10: List all products in a category")
    print("11: Get the total cost of a category")
    print("12: Get the total cost of the inventory")


if __name__ == "__main__":
    main()
