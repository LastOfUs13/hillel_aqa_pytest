import allure

from HW17.utilities.api.base_api import BaseAPI


class HousesAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__houses_url = "/houses/"

    @allure.step
    def get_house(self, house_id, headers=None):
        response = self.get(url=f"{self.__houses_url}{house_id}", headers=headers)
        return response
