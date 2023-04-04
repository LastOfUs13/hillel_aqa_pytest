from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __checkout_title_locator = (By.XPATH, "//span[@class='title']")
    __first_name_field = (By.XPATH, "//input[@id='first-name']")
    __last_name_field = (By.XPATH, "//input[@id='last-name']")
    __postal_code = (By.XPATH, "//input[@id='postal-code']")
    __error_message = (By.XPATH, "//div[@class='error-message-container error']")
    __continue_button = (By.XPATH, "//input[@id='continue']")

    def is_checkout_page_title_displayed(self):
        title_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__checkout_title_locator))
        return title_element.is_displayed()

    def is_checkout_page_empty_fields_error_displayed(self):
        error_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__error_message))
        return error_element.is_displayed()

    def empty_first_name_field(self):
        self._send_keys(self.__last_name_field, "smith")
        self._send_keys(self.__postal_code, "1313")
        is_continue_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__continue_button))
        self._click(is_continue_button)
        return self

    def empy_last_name_field(self):
        self._send_keys(self.__first_name_field, "john")
        self._send_keys(self.__postal_code, "1313")
        is_continue_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__continue_button))
        self._click(is_continue_button)
        return self

    def empy_postal_code_field(self):
        self._send_keys(self.__first_name_field, "john")
        self._send_keys(self.__last_name_field, "smith")
        is_continue_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__continue_button))
        self._click(is_continue_button)
        return self

    def is_checkout_page_empty_postal_code_error_text_correct(self):
        error_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__error_message))
        return self._give_back_element_text(error_element)

    def finish_purchase(self):
        self._send_keys(self.__first_name_field, "john")
        self._send_keys(self.__last_name_field, "smith")
        self._send_keys(self.__postal_code, "1313")
        is_continue_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__continue_button))
        self._click(is_continue_button)
        from HW17.page_objs.overview_page import OverviewPage
        return OverviewPage(self.my_driver)

