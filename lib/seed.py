from models.__init__ import CONN, CURSOR
from models.category import Category
from models.item import Item


def seed_database():
    Item.drop_table()
    Category.drop_table()
    Category.create_table()
    Item.create_table()

    # Create seed data
    food = Category.create('Food')
    clothing = Category.create('Clothing')
    electronics = Category.create('Electronics')
    home = Category.create('Home')
    others = Category.create('Others')

    Item.create("Apple", 100, 2000, food.id)
    Item.create("Bread", 200, 1000, food.id)
    Item.create("Milk", 200, 12000, food.id)
    Item.create("Eggs", 200, 6000, food.id)
    Item.create("Computers", 20, 1200000, electronics.id)
    Item.create("Fridge", 10, 300000, electronics.id)
    Item.create("Bed", 5, 100000, home.id)
    Item.create("TVs", 50, 200000, electronics.id)
    Item.create("T-shirts", 100, 80000, clothing.id)
    Item.create("Dresses", 150, 30000, clothing.id)
    Item.create("Trousers", 100, 120000, clothing.id)
    Item.create("Cosmetics", 60, 30000, others.id)
    Item.create("Books", 200, 100000, others.id)

seed_database()
print("Seeded database")
