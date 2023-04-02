from HW17.tests.errors_text import checkout_unfilled_zip
from pytest import mark


@mark.regression
def test_empy_first_name_field_validation_is_appeared(open_products_tab):
    go_to_checkout_page = open_products_tab.add_item_and_go_to_cart().go_to_checkout()
    go_to_checkout_page.empty_first_name_field().is_checkout_page_empty_fields_error_displayed(), "validation message isn't displayed"


@mark.regression
def test_empy_last_name_field_validation_is_appears(open_products_tab):
    go_to_checkout_page = open_products_tab.add_item_and_go_to_cart().go_to_checkout()
    go_to_checkout_page.empy_last_name_field().is_checkout_page_empty_fields_error_displayed(), "validation message isn't displayed"


@mark.regression
def test_empy_postal_code_field_validation_is_appears(open_products_tab):
    go_to_checkout_page = open_products_tab.add_item_and_go_to_cart().go_to_checkout()
    go_to_checkout_page.empy_postal_code_field().is_checkout_page_empty_fields_error_displayed(), "validation message isn't displayed"


@mark.regression
def test_empty_postal_code_message_is_appears(open_products_tab):
    checkout_page = open_products_tab.add_item_and_go_to_cart().go_to_checkout().empy_postal_code_field()
    assert checkout_page.is_checkout_page_empty_postal_code_error_text_correct() == checkout_unfilled_zip


@mark.smoke
def test_overview_page_open(open_products_tab):
    overview = open_products_tab.add_item_and_go_to_cart().go_to_checkout()
    assert overview.finish_purchase().is_overview_page_title_correct() == "Checkout: Overview", 'something went wrong with title'
