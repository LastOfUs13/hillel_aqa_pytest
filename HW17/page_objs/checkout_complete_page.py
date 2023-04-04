import os
import datetime
from HW17.constants import ROOT_DIR
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from HW17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckOutComplete(BasePage):

    def __init__(self, my_driver):
        super().__init__(my_driver)
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    __thank_for_order = (By.XPATH, "//h2[@class='complete-header']")
    __back_home = (By.XPATH, "//button[@id='back-to-products']")

    def make_screen(self, what_kind_pict_you_need: str):
        now_date = datetime.datetime.utcnow().strftime('%d.%m_%H.%M')
        name_screen = what_kind_pict_you_need + '_' + now_date + '.png'
        screenshot_path = os.path.join(ROOT_DIR, 'screenshots', name_screen)
        self.my_driver.save_screenshot(screenshot_path)

    def check_final_page_message(self):
        is_finish_message = self.__my_waiter.until(EC.visibility_of_element_located(self.__thank_for_order))
        return self._give_back_element_text(is_finish_message)

    def go_back_to_products_tab(self):
        back_home_button = self.__my_waiter.until(EC.visibility_of_element_located(self.__back_home))
        self._click(back_home_button)
        from HW17.page_objs.product_page import ProductPage
        return ProductPage(self.my_driver)
