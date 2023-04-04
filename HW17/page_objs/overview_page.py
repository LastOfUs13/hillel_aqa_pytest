
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OverviewPage(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __title = (By.XPATH, "//span[@class='title']")
    __price = (By.XPATH, "//div[@class='inventory_item_price']")
    __finish = (By.XPATH, "//button[@id='finish']")

    def click_via_js(self, locator):
        self.my_driver.execute_script("arguments[0].click()", self._wait_until_element_clickable(locator))

    def get_price_at_the_overview(self):
        is_item_price = self.__my_waiter.until(EC.visibility_of_element_located(self.__price))
        return self._give_back_element_text(is_item_price)

    def is_checkout_page_title_displayed(self):
        title_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__title))
        return title_element.is_displayed()

    def is_overview_page_title_correct(self):
        error_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__title))
        return self._give_back_element_text(error_element)

    def happy_pass(self):
        is_finish = self.__my_waiter.until(EC.visibility_of_element_located(self.__finish))
        self.click_via_js(is_finish)
        from HW17.page_objs.checkout_complete_page import CheckOutComplete
        return CheckOutComplete(self.my_driver)

