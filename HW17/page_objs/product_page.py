from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ProductPage(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __title_locator = (By.XPATH, "//span[@class='title']")
    __go_to_left_side_bar = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    __left_side_bar_about_link = (By.XPATH, "//a[@id='about_sidebar_link']")
    __left_side_bar_log_out_link = (By.XPATH, "//a[@id='logout_sidebar_link']")
    __left_side_bar_reset_app_state = (By.XPATH, "//a[@id='reset_sidebar_link']")
    __add_to_cart_sauce_labs_backpack = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    __first_item_price = (By.CSS_SELECTOR,
                          "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div")
    __last_item_price = (By.CSS_SELECTOR,
                         "#inventory_container > div > div:nth-child(6) > div.inventory_item_description > div.pricebar > div")
    __fb_social_link = (By.XPATH, "//a[normalize-space()='Facebook']")
    __item_in_cart = (By.XPATH, "//div[@class='inventory_item_name']")
    __filters = (By.XPATH, "//select[@class='product_sort_container']")
    __cart = (By.XPATH, "//a[@class='shopping_cart_link']")

    def get_first_item_price_inside_products_tab(self):
        is_item_price = self.__my_waiter.until(EC.visibility_of_element_located(self.__first_item_price))
        return self._give_back_element_text(is_item_price)

    def go_to_cart(self):
        is_cart = self.__my_waiter.until(EC.visibility_of_element_located(self.__cart))
        self._click(is_cart)
        from HW17.page_objs.your_cart import YourCart
        return YourCart(self.my_driver)

    def get_items_prices(self):
        first_item_price = self.get_first_item_price_inside_products_tab()
        last_item_price = self.__my_waiter.until(EC.visibility_of_element_located(self.__last_item_price))
        res = list()
        res.append(first_item_price)
        res.append(self._give_back_element_text(last_item_price))
        return res


    def apply_filter(self):
        is_filters_dropdown = self.__my_waiter.until(EC.visibility_of_element_located(self.__filters))
        select_filter = Select(is_filters_dropdown)
        select_filter.select_by_index(1)
        return self

    def go_to_fb_social_link(self):
        action = ActionChains(self.my_driver)
        fb_social_link = self.__my_waiter.until(EC.visibility_of_element_located(self.__fb_social_link))
        action.move_to_element(fb_social_link).perform()
        self._click(fb_social_link)
        self.my_driver.switch_to.window(self.my_driver.window_handles[-1])
        return self

    def is_product_page_title_displayed(self):
        title_element = self.__my_waiter.until(EC.visibility_of_element_located(self.__title_locator))
        return title_element.is_displayed()

    def go_to_about_link(self):
        self._click(self.__go_to_left_side_bar)
        self._click(self.__left_side_bar_about_link)
        return self

    def add_to_cart_sauce_labs_backpack(self):
        is_sauce_labs_backpack = self.__my_waiter.until(
            EC.visibility_of_element_located(self.__add_to_cart_sauce_labs_backpack))
        self._click(is_sauce_labs_backpack)
        return self

    def check_title(self):
        expected_title = self.my_driver.title
        return expected_title

    def logout_from_site(self):
        self._click(self.__go_to_left_side_bar)
        self._click(self.__left_side_bar_log_out_link)
        from HW17.page_objs.sign_in_page import SignInPage
        return SignInPage(self.my_driver)

    def reset_app_state(self):
        self._click(self.__go_to_left_side_bar)
        self._click(self.__left_side_bar_reset_app_state)
        return self

    def reset_purchase(self):
        self.add_to_cart_sauce_labs_backpack().reset_app_state().go_to_cart()
        return self

    def check_that_item_was_deleted(self):
        self._make_sure_that_element_not_displayed(self.__item_in_cart)
        return self

    def add_item_and_go_to_cart(self):
        self.add_to_cart_sauce_labs_backpack()
        self.go_to_cart()
        from HW17.page_objs.your_cart import YourCart
        return YourCart(self.my_driver)


