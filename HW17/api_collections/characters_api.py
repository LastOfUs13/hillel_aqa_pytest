from HW17.utilities.api.base_api import BaseAPI
import allure

class CharactersAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__characters_url = "/characters/"

    @allure.step
    def get_character(self, character_id, headers=None):
        response = self.get(url=f"{self.__characters_url}{character_id}", headers=headers)
        return response
