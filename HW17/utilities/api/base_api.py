import requests


class BaseAPI:

    def __init__(self, env):
        self.__request = requests
        self.__base_url = env.api_url
        self.__headers = {"Connection": "keep-alive"}

    def get(self, url, headers=None, params=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f"{self.__base_url}{url}", headers=headers, params=params)
        return response

