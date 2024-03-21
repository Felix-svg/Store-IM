from models.category import Category
from models.product import Product


def exit_program():
    print("Exiting program...")
    print("Goodbye!")
    exit()


def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)


def find_category_by_name():
    name = input("Enter category name: ")
    category = Category.find_by_name(name)
    print(category) if category else print(f"Department {name} not found")


# def find_category_by_id():
#     id_ = input("Enter category id: ")
#     category = Category.find_by_id(id_)
#     print(category) if category else print(f"Department {id_} not found")


def create_category():
    name = input("Enter category name: ")
    try:
        category = Category.create(name)
        print(f"Successsfully created {category}")
    except Exception as exc:
        print("Error creating category: ", exc)


# def update_category():
#     id_ = input("Enter category id: ")
#     if category := Category.find_by_id(id_):
#         try:
#             name = input("Enter the category's new name: ")
#             category.name = name
#             category.update()
#             print(f"Successfully updated {category}")

#         except Exception as exc:
#             print("Error updating category: ", exc)
#     else:
#         print(f"Category not found")


# def delete_category():
#     id_ = input("Enter category id: ")
#     if category := Category.find_by_id(id_):
#         category.delete()
#         print(f"Category {id_} successfully deleted")
#     else:
#         print(f"Department {id_} not found")


def list_products():
    products = Product.get_all()
    for product in products:
        print(products)


def find_product_by_name():
    name = input("Enter product's Name: ")
    product = Product.find_by_name(name)
    print(product) if product else print(f"Product {name} not found")


# def find_product_by_id():
#     id_ = input("Enter product's id: ")
#     product = Product.find_by_id(id_)
#     print(product) if product else print(f"Product {id_} not found")


def create_product():
    name = input("Enter product's name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter product's price: "))
    category_id = int(input("Enter product's category id: "))
    try:
        product = Product.create(name, quantity, price, category_id)
        print(f"Successsfully created {product}")
    except Exception as exc:
        print("Error creating product: ", exc)


def update_product():
    id_ = input("Enter product id: ")
    if product := Product.find_by_id(id_):
        try:
            name = input("Enter the product's new name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter product's price: "))
            category_id = int(input("Enter product's category id: "))
            product.name = name
            product.quantity = quantity
            product.price = price
            product.category_id = category_id
            product.update()
            print(f"Successfully updated {product}")

        except Exception as exc:
            print("Error updating product: ", exc)


def delete_product():
    id_ = input("Enter product id: ")
    if product := Product.find_by_id(id_):
        product.delete()
        print(f"Product {id_} successfully deleted")
    else:
        print(f"Product {id_} not found")


def list_category_products():
    id_ = int(input("Enter the category id: "))
    if category := Category.find_by_id(id_):
        products = category.products()
        for product in products:
            print(product)
    else:
        print(f"Category {id_} not found")


def calculate_total_inventory_cost():
    total_inventory_cost = Product.calculate_total_inventory_cost()
    print("Total inventory cost:", f"Ksh. {total_inventory_cost}")


def calculate_total_category_cost():
    try:
        category_id = int(input("Enter the category id: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    total_category_cost = Category.calculate_total_category_cost(category_id)
    if total_category_cost is not None:
        print(
            f"Total cost of category {category_id} is:", f"Ksh. {total_category_cost}"
        )
    else:
        print("No products found for the given category ID.")
