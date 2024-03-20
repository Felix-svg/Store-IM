from helpers import (
    exit_program,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_items,
    find_item_by_name,
    find_item_by_id,
    create_item,
    update_item,
    delete_item,
    list_category_items
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == "4":
            create_category()
        elif choice == "5":
            update_category()
        elif choice == "6":
            delete_category()
        elif choice == "7":
            list_items()
        elif choice == "8":
            find_item_by_name()
        elif choice == "9":
            find_item_by_id()
        elif choice == "10":
            create_item()
        elif choice == "11":
            update_item()
        elif choice == "12":
            delete_item()
        elif choice == "13":
            list_category_items()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Find category by id")
    print("4: Create category")
    print("5: Update category")
    print("6: Delete category")
    print("7. List all items")
    print("8. Find item by name")
    print("9. Find item by id")
    print("10: Create item")
    print("11: Update item")
    print("12: Delete item")
    print("13: List all items in a category")


if __name__ == "__main__":
    main()