import pytest


@pytest.mark.smoke
def test_that_it_is_possible_to_log_out_from_products_page(open_products_tab):
    sign_in_form = open_products_tab.logout_from_site()
    assert sign_in_form.is_log_in_button_displayed(), "something went wrong"


@pytest.mark.regression
def test_that_about_link_open_relevant_page(open_products_tab):
    about_page = open_products_tab.go_to_about_link()
    title = about_page.check_title()
    assert title == "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"


@pytest.mark.smoke
def test_that_it_is_possible_reset_purchases(open_products_tab):
    add_to_cart_then_reset = open_products_tab.reset_purchase()
    assert add_to_cart_then_reset.check_that_item_was_deleted(), "maybe item was not removed"


@pytest.mark.smoke
def test_that_fb_link_open_relevant_resource(open_products_tab):
    result = open_products_tab.go_to_fb_social_link()
    assert result._get_url() == "https://www.facebook.com/saucelabs", "url is wrong"


@pytest.mark.regression
def test_that_after_filter_applied_items_order_reverse(open_products_tab):
    before_filter = open_products_tab.get_items_prices()
    expected_after_filter = before_filter[::-1]
    actual_after_filter = open_products_tab.apply_filter().get_items_prices()
    assert actual_after_filter == expected_after_filter
