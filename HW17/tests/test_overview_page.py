from pytest import mark


@mark.regression
def test_prices_stay_same(open_products_tab):
    price_in_cart = open_products_tab.add_item_and_go_to_cart().get_item_price_inside_cart()
    price_in_overview = open_products_tab.go_to_cart().go_to_checkout().finish_purchase().get_price_at_the_overview()
    assert price_in_cart == price_in_overview, "prices should be equal"


@mark.smoke
def test_happy_pass(open_products_tab):
    res = open_products_tab.add_item_and_go_to_cart().go_to_checkout().finish_purchase().happy_pass()
    assert res.check_final_page_message() == "Thank you for your order!"
    res.make_screen("Happy pass!")
    home = res.go_back_to_products_tab()
    assert home.is_product_page_title_displayed(), 'something wrong with title'

