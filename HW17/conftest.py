import json
import pytest
from HW17.constants import ROOT_DIR
from HW17.page_objs.sign_in_page import SignInPage
from HW17.utilities.config_reader import get_user_data
from HW17.utilities.configutation import Configuration
from HW17.utilities.driver_factory import driver_factory


@pytest.fixture(scope="session", autouse=True)
def env():
    with open(f"{ROOT_DIR}/configurations/config.json", "r") as file:
        result = file.read()
        conf = json.loads(result)
        return Configuration(**conf)


@pytest.fixture()
def open_url(env):
    my_driver = driver_factory(int(env.browser_id))
    my_driver.maximize_window()
    my_driver.get(env.app_url)
    yield my_driver
    my_driver.quit()


@pytest.fixture()
def open_sign_in_page(open_url):
    return SignInPage(open_url)


@pytest.fixture()
def open_products_tab(open_sign_in_page):
    return open_sign_in_page.sign_in(get_user_data()[0], get_user_data()[1])

