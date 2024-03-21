from models.category import Category
from models.product import Product
from models.product_category import ProductCategory


def seed_database():
    # Drop existing tables if any
    Product.drop_table()
    Category.drop_table()
    ProductCategory.drop_table()

    # Create tables
    Category.create_table()
    Product.create_table()
    ProductCategory.create_table()

    # Seed data
    # Create categories
    food = Category("Food")
    clothing = Category("Clothing")
    electronics = Category("Electronics")
    home = Category("Home")
    others = Category("Others")

    # Save categories to the database
    food.save()
    clothing.save()
    electronics.save()
    home.save()
    others.save()

    # Create products
    apple = Product("Apple", 100, 25, food.id)
    bread = Product("Bread", 200, 50, food.id)
    t_shirt = Product("T-shirt", 50, 500, clothing.id)
    computers = Product("Computer", 20, 70000, electronics.id)
    bed = Product("Bed", 10, 20000, home.id)
    cosmetics = Product("Cosmetics", 20, 2000, others.id)
    dresses = Product("Dresses", 150, 1000, clothing.id)
    trousers = Product("Trousers", 100, 1200, clothing.id)
    tv = Product("TVs", 50, 50000, electronics.id)
    fridge = Product("Fridge", 10, 30000, electronics.id)
    books = Product("Books", 200, 200, others.id)

    # Save products to the database
    apple.save()
    bread.save()
    t_shirt.save()
    computers.save()
    bed.save()
    cosmetics.save()
    dresses.save()
    trousers.save()
    tv.save()
    fridge.save()
    books.save()

    # Create product-category associations
    ProductCategory.save(apple.id, food.id)
    ProductCategory.save(bread.id, food.id)
    ProductCategory.save(t_shirt.id, clothing.id)
    ProductCategory.save(computers.id, electronics.id)
    ProductCategory.save(bed.id, home.id)
    ProductCategory.save(cosmetics.id, others.id)
    ProductCategory.save(dresses.id, clothing.id)
    ProductCategory.save(trousers.id, clothing.id)
    ProductCategory.save(tv.id, electronics.id)
    ProductCategory.save(fridge.id, electronics.id)
    ProductCategory.save(books.id, others.id)


seed_database()
print("Seeded database")
