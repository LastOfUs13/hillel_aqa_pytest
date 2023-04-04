import configparser

from HW17.constants import ROOT_DIR

path_to_config_file = f"{ROOT_DIR}/configurations/config.ini"
my_config = configparser.RawConfigParser()
my_config.read(path_to_config_file)


def get_site_url():
    return my_config.get('testing_resource_data', 'site_url')


def get_user_data():
    return (my_config.get('site_user_data', 'user_name_data'),
            my_config.get('site_user_data', 'password_data'))


def get_browser_id():
    return my_config.get('browser_id', 'id')


def get_headless_status():
    result = my_config.get("browser_id", "headless")
    if result in ["True", "true", "1"]:
        return True
    else:
        return False

