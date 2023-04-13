import json
from contextlib import suppress
import allure
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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
@pytest.fixture()
def open_url(env,request):
    my_driver = driver_factory(int(env.browser_id))
    my_driver.maximize_window()
    my_driver.get(env.app_url)
    yield my_driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(my_driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    my_driver.quit()


@pytest.fixture()
def open_sign_in_page(open_url):
    return SignInPage(open_url)


@pytest.fixture()
def open_products_tab(open_sign_in_page):
    return open_sign_in_page.sign_in(get_user_data()[0], get_user_data()[1])

