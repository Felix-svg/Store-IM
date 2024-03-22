from helpers import (
    exit_program,
    list_categories,
    create_category,
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
    print("Welcome to StoreIM Store Manager.\n")
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_category()
            print("\n")
        elif choice == "2":
            list_categories()
            print("\n")
        elif choice == "3":
            delete_category()
            print("\n")
        elif choice == "4":
            create_product()
            print("\n")
        elif choice == "5":
            update_product()
            print("\n")
        elif choice == "6":
            list_products()
            print("\n")
        elif choice == "7":
            delete_product()
            print("\n")
        elif choice == "8":
            find_product_by_name()
            print("\n")
        elif choice == "9":
            list_category_products()
            print("\n")
        elif choice == "10":
            calculate_total_category_cost()
            print("\n")
        elif choice == "11":
            calculate_total_inventory_cost()
            print("\n")
        else:
            print("Invalid choice, please try again")
            print("\n")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1: Add category")
    print("2. List all categories")
    print("3: Delete a category")
    print("4: Add a product to the inventory")
    print("5: Update product")
    print("6. List all products in the inventory")
    print("7: Delete a product from the inventory")
    print("8. Search product by name")
    print("9: List all products in a category")
    print("10: Get the total cost of a category")
    print("11: Get the total cost of the inventory")


if __name__ == "__main__":
    main()
