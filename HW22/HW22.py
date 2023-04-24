
from database_repo.products_repo import ProductsRepo
from database_repo.orders_repo import OrdersRepo


def test_create_table(create_db_connect):
    products_repo = ProductsRepo(create_db_connect).create_products_table().put_data_in_products_table()
    OrdersRepo(create_db_connect).create_orders_table().put_data_in_orders_table()
    final_res = products_repo.get_name_price_quantity_total()
    for values in final_res:
        print(values)




