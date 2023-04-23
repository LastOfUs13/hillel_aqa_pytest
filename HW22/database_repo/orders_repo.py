class OrdersRepo:

    def __init__(self, cursor):
        self.__cursor = cursor

    def create_orders_table(self):
        self.__cursor.execute("create table orders(id SERIAL PRIMARY KEY ,product_id int, quantity int, constraint fk_product_id foreign key(product_id) references products(id));")
        self.__cursor.connection.commit()
        return self

    def put_data_in_orders_table(self):
        self.__cursor.execute("insert into orders(product_id,quantity) values (5,2),(2,4),(4,1),(3,4),(1,1);")
        self.__cursor.connection.commit()
        return self

    def get_all(self):
        self.__cursor.execute("select * from products")
        return self.__cursor.fetchall()
