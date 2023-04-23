import json
import psycopg2
import pytest
from constant import ROOT_DIR
from Configuration import Configuration


@pytest.fixture(scope="session", autouse=True)
def my_env():
    with open(f"{ROOT_DIR}/config.json", "r") as file:
        result = file.read()
        conf = json.loads(result)
        return Configuration(**conf)


@pytest.fixture()
def create_db_connect(my_env):
    __connection = psycopg2.connect(user=my_env.db_user,
                                    password=my_env.db_password,
                                    host=my_env.host,
                                    port=my_env.port,
                                    database=my_env.database)
    __cursor = __connection.cursor()
    yield __cursor
    if __connection:
        __connection.close()
        __connection.close()
