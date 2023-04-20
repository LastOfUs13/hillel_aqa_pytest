import psycopg2

connect = psycopg2.connect(user='sirius_black',
                           password='black 123',
                           host='127.0.0.1',
                           port='5432',
                           database='store')
try:
    cursor = connect.cursor()
    cursor.execute("create table products(id SERIAL PRIMARY KEY ,name varchar(20) unique, price int);")
    cursor.execute(
        "insert into products(name,price) values ('tomato', 5),('banana', 3),('pickle', 2),('carrot' ,4),('milk' ,6);")
    cursor.execute(
        "create table orders(id SERIAL PRIMARY KEY ,product_id int, quantity int, constraint fk_product_id foreign key(product_id) references products(id));")
    cursor.execute("insert into orders(product_id,quantity) values (5,2),(2,4),(4,1),(3,4),(1,1);")
    connect.commit()
    res = cursor.execute(
        "select p.name, p.price, o.quantity, p.price * o.quantity AS total from products as p join orders as o on  p.id = o.product_id;")
    final_res = cursor.fetchall()
    for items in final_res:
        print(items)
finally:
    cursor.close()
    connect.close()