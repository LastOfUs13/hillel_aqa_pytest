from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class YourCart(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __continue_shopping = (By.XPATH, "//button[@id='continue-shopping']")
    __checkout = (By.XPATH, "//button[@id='checkout']")
    __remove_item = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    __item_name = (By.XPATH, "//div[@class='inventory_item_name']")
    __item_price = (By.XPATH, "//div[@class='inventory_item_price']")
    __twitter_social_link = (By.XPATH, "//a[normalize-space()='Twitter']")

    def get_item_price_inside_cart(self):
        is_item_price = self.__my_waiter.until(EC.visibility_of_element_located(self.__item_price))
        return self._give_back_element_text(is_item_price)

    def continue_shopping(self):
        self._click(self.__continue_shopping)
        from HW17.page_objs.product_page import ProductPage
        return ProductPage(self.my_driver)

    def remove_item(self):
        is_remove_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__remove_item))
        self._click(is_remove_button)
        return self

    def check_that_item_was_deleted_inside_the_cart(self):
        self._make_sure_that_element_not_displayed(self.__item_name)
        return self

    def go_to_fb_social_link(self):
        action = ActionChains(self.my_driver)
        twitter_social_link = self.__my_waiter.until(EC.visibility_of_element_located(self.__twitter_social_link))
        action.move_to_element(twitter_social_link).perform()
        self._click(twitter_social_link)
        self.my_driver.switch_to.window(self.my_driver.window_handles[-1])
        return self

    def go_to_checkout(self):
        self._click(self.__checkout)
        from HW17.page_objs.checkout_page import CheckoutPage
        return CheckoutPage(self.my_driver)
