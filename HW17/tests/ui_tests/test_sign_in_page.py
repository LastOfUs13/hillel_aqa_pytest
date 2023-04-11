from HW17.tests.ui_tests.errors_text import signin_unfilled_password_message, signin_unfilled_mail_message
from HW17.utilities.config_reader import get_user_data
from pytest import mark


@mark.smoke
def test_positive_sign_in(open_products_tab):
    products_tab = open_products_tab
    assert products_tab.is_product_page_title_displayed(), "title isn't displayed"


@mark.regression
def test_that_empty_fields_message_displayed(open_sign_in_page):
    sign_in = open_sign_in_page
    wellcome_page = sign_in.click_login_button()
    assert wellcome_page.is_sign_in_page_empty_fields_error_text_correct(), "empty fields message isn't displayed"


@mark.regression
def test_that_empty_password_field_message_displayed(open_sign_in_page):
    sign_in = open_sign_in_page
    wellcome_page = sign_in.fill_email_field((get_user_data()[0])).click_login_button()
    assert wellcome_page.is_sign_in_page_empty_fields_error_displayed(), "empty password field message isn't displayed"


@mark.smoke
def test_that_empty_password_field_message_is_correct(open_sign_in_page):
    sign_in = open_sign_in_page
    wellcome_page = sign_in.fill_email_field((get_user_data()[0])).click_login_button()
    assert wellcome_page.is_sign_in_page_empty_fields_error_text_correct() == signin_unfilled_password_message


@mark.regression
def test_that_empty_username_field_message_displayed(open_sign_in_page):
    sign_in = open_sign_in_page
    wellcome_page = sign_in.fill_password_field((get_user_data()[1])).click_login_button()
    assert wellcome_page.is_sign_in_page_empty_fields_error_displayed(), "empty username field message isn't displayed"


@mark.smoke
def test_that_empty_username_field_message_is_correct(open_sign_in_page):
    sign_in = open_sign_in_page
    wellcome_page = sign_in.fill_password_field((get_user_data()[1])).click_login_button()
    assert wellcome_page.is_sign_in_page_empty_fields_error_text_correct() == signin_unfilled_mail_message
