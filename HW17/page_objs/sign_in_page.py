from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HW17.page_objs.product_page import ProductPage
from HW17.utilities.web_ui.base_page import BasePage


class SignInPage(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __mail_input = (By.XPATH, "//input[@id='user-name']")
    __password_input = (By.XPATH, "//input[@id='password']")
    __login_button = (By.XPATH, "//input[@id='login-button']")
    __empty_fields_error = (By.XPATH, "//div[@class='error-message-container error']")

    def is_log_in_button_displayed(self):
        is_login_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__login_button))
        return is_login_button.is_displayed()

    def fill_email_field(self, user_mail: str):
        self._send_keys(locator=self.__mail_input, value=user_mail)
        return self

    def fill_password_field(self, user_password: str):
        self._send_keys(locator=self.__password_input, value=user_password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)
        return self

    def sign_in(self, mail, password):
        self.fill_email_field(mail).fill_password_field(password).click_login_button()
        return ProductPage(self.my_driver)

    def is_sign_in_page_empty_fields_error_displayed(self):
        error_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__empty_fields_error))
        return error_element.is_displayed()

    def is_sign_in_page_empty_fields_error_text_correct(self):
        error_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__empty_fields_error))
        return self._give_back_element_text(error_element)
