from helpers import (
    exit_program,
    list_categories,
    create_category,
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
    print("Welcome to StoreIM Store Manager.\n")
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
            create_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            list_products()
        elif choice == "7":
            find_product_by_name()
        elif choice == "8":
            list_category_products()
        elif choice == "9":
            calculate_total_category_cost()
        elif choice == "10":
            calculate_total_inventory_cost()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1: Add category")
    print("2. List all categories")
    print("3: Add a product to the inventory")
    print("4: Update product")
    print("5: Delete a product from the inventory")
    print("6. List all products in the inventory")
    print("7. Search product by name")
    print("8: List all products in a category")
    print("9: Get the total cost of a category")
    print("10: Get the total cost of the inventory")


if __name__ == "__main__":
    main()
