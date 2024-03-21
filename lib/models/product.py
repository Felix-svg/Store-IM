from models.__init__ import CURSOR, CONN
from models.category import Category


class Product:
    all = {}

    def __init__(self, name, quantity, price, category_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category_id = category_id

    def __repr__(self):
        return f"<Product ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, category ID: {self.category_id}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative integer")

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int) and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError(
                "category_id must reference a category in the database and be an integer"
            )

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        quantity INTEGER,
        price INTEGER,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS products"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO products (name, quantity, price, category_id) VALUES (?,?,?,?)"""
        CURSOR.execute(sql, (self.name, self.quantity, self.price, self.category_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """UPDATE products SET name=?, quantity=?, price=?, category_id=? WHERE id=?"""
        CURSOR.execute(
            sql, (self.name, self.quantity, self.price, self.category_id, self.id)
        )
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM products WHERE id=?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

    @classmethod
    def create(cls, name, quantity, price, category_id):
        new_product = cls(name, quantity, price, category_id)
        new_product.save()
        return new_product

    @classmethod
    def instance_from_db(cls, row):
        if row:
            product = cls.all.get(row[0])
            if product:
                product.name = row[1]
                product.quantity = row[2]
                product.price = row[3]
                product.category_id = row[4]
            else:
                product = cls(row[1], row[2], row[3], row[4], row[0])
                cls.all[product.id] = product
            return product
        return None

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM products"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM products WHERE id=?"""
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """SELECT * FROM products WHERE name=?"""
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def calculate_total_inventory_cost(cls):
        total_cost = 0
        products = cls.get_all()
        for product in products:
            total_cost += product.quantity * product.price
        return total_cost
