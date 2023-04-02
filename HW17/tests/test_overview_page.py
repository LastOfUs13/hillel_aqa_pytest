from pytest import mark


@mark.regression
def test_prices_stay_same(open_products_tab):
    price_in_cart = open_products_tab.add_item_and_go_to_cart().get_item_price_inside_cart()
    price_in_overview = open_products_tab.go_to_cart().go_to_checkout().finish_purchase().get_price_at_the_overview()
    assert price_in_cart == price_in_overview, "prices should be equal"


@mark.smoke
def test_happy_pass(open_products_tab):
    overview = open_products_tab.add_item_and_go_to_cart().go_to_checkout().finish_purchase()
    overview.happy_pass()
