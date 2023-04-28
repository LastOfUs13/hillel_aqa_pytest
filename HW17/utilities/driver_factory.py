from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from HW17.utilities.config_reader import get_headless_status

__CHROME = 1
__FIRE_FOX = 2


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        chrome_options = Options()
        if get_headless_status():
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
        return Chrome(service=chrome_service(ChromeDriverManager().install()), options=chrome_options)
    elif int(driver_id) == __FIRE_FOX:
        return Firefox(service=firefox_service(GeckoDriverManager().install()))
    else:
        return Chrome(service=chrome_service(ChromeDriverManager().install()))