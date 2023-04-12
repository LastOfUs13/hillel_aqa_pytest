import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, my_driver):
        self.my_driver = my_driver
        self.__my_waiter = WebDriverWait(self.my_driver, 10, 2)

    def _wait_until_element_located(self, locator):
        return self.__my_waiter.until(EC.presence_of_element_located(locator))

    def _wait_until_element_clickable(self, locator):
        return self.__my_waiter.until(EC.element_to_be_clickable(locator))

    @allure.step
    def _send_keys(self, locator, value):
        element = self._wait_until_element_located(locator)
        element.send_keys(value)

    @allure.step
    def _click(self, locator):
        self._wait_until_element_clickable(locator).click()

    @allure.step
    def _get_url(self):
        return self.my_driver.current_url

    @allure.step
    def _refresh_page(self):
        return self.my_driver.refresh()

    @allure.step
    def _make_sure_that_element_not_displayed(self, locator):
        try:
            self.__my_waiter.until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return True

    @allure.step
    def _give_back_element_text(self, element):
        return element.text


