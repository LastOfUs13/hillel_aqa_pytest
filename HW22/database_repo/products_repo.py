class ProductsRepo:

    def __init__(self, cursor):
        self.__cursor = cursor

    def create_products_table(self):
        self.__cursor.execute("create table products(id SERIAL PRIMARY KEY ,name varchar(20) unique, price int);")
        self.__cursor.connection.commit()
        return self

    def put_data_in_products_table(self):
        self.__cursor.execute("insert into products(name,price) values ('tomato', 5),('banana', 3),('pickle', 2),('carrot' ,4),('milk' ,6);")
        self.__cursor.connection.commit()
        return self

    def get_all(self):
        self.__cursor.execute("select * from products")
        return self.__cursor.fetchall()

    def get_name_price_quantity_total(self):
        self.__cursor.execute("select p.name, p.price, o.quantity, p.price * o.quantity AS total from products as p join orders as o on  p.id = o.product_id;")
        return self.__cursor.fetchall()

