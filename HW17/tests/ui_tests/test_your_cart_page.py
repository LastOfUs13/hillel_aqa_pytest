import pytest


@pytest.mark.regression
def test_price_on_the_products_tab_and_inside_the_cart(open_products_tab):
    price_on_the_products_tab = open_products_tab.get_first_item_price_inside_products_tab()
    price_inside_the_cart = open_products_tab.add_item_and_go_to_cart().get_item_price_inside_cart()
    assert price_on_the_products_tab == price_inside_the_cart, 'prices should be equal'


@pytest.mark.smoke
def test_opportunity_to_continue_shopping(open_products_tab):
    on_the_products_tab = open_products_tab.add_item_and_go_to_cart().continue_shopping()
    assert on_the_products_tab.is_product_page_title_displayed(), "title isn't displayed"


@pytest.mark.smoke
def test_opportunity_remove_item_inside_the_cart(open_products_tab):
    add_to_cart_then_remove = open_products_tab.add_item_and_go_to_cart().remove_item()
    assert add_to_cart_then_remove.check_that_item_was_deleted_inside_the_cart(), "maybe item was not removed"


@pytest.mark.smoke
def test_twitter_social_button(open_products_tab):
    inside_cart = open_products_tab.go_to_cart().go_to_fb_social_link()
    assert inside_cart._get_url() == "https://twitter.com/saucelabs", "url is wrong"


@pytest.mark.smoke
def test_checkout(open_products_tab):
    from_cart_to_checkout = open_products_tab.go_to_cart().go_to_checkout()
    assert from_cart_to_checkout.is_checkout_page_title_displayed(), 'you are on the checkout page'
