from models.__init__ import CURSOR, CONN


class ProductCategory:
    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS product_categories (
            product_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (category_id) REFERENCES categories(id),
            PRIMARY KEY (product_id, category_id)
        )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(cls, product_id, category_id):
        sql = "INSERT INTO product_categories (product_id, category_id) VALUES (?, ?)"
        CURSOR.execute(sql, (product_id, category_id))
        CONN.commit()

    @classmethod
    def create(cls, product_id, category_id):
        new_product_category = cls(product_id, category_id)
        new_product_category.save()
        return new_product_category

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS product_categories"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def delete(cls, product_id, category_id):
        sql = "DELETE FROM product_categories WHERE product_id=? AND category_id=?"
        CURSOR.execute(sql, (product_id, category_id))
        CONN.commit()


    # @classmethod
    # def find_by_product_id(cls, product_id):
    #     sql = "SELECT * FROM product_categories WHERE product_id=?"
    #     CURSOR.execute(sql, (product_id,))
    #     rows = CURSOR.fetchall()
    #     return rows

    # @classmethod
    # def find_by_category_id(cls, category_id):
    #     sql = "SELECT * FROM product_categories WHERE category_id=?"
    #     CURSOR.execute(sql, (category_id,))
    #     rows = CURSOR.fetchall()
    #     return rows

    # @classmethod
    # def find_by_ids(cls, product_id, category_id):
    #     sql = "SELECT * FROM product_categories WHERE product_id=? AND category_id=?"
    #     CURSOR.execute(sql, (product_id, category_id))
    #     row = CURSOR.fetchone()
    #     return row
