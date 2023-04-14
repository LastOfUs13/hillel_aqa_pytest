from HW17.tests.api_tests.conftest import character_mock, house_mock
from http import HTTPStatus
from HW17.data_for_api.house_data import HouseData
from HW17.api_collections.characters_api import CharactersAPI
from HW17.data_for_api.character_data import CharacterData
import pytest


@pytest.mark.test_get_character
def test_get_character_api(env, character_mock):
    expected_character = character_mock
    response = CharactersAPI(env).get_character(10)
    response_data = response.json()
    actual_character = CharacterData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'status code is not OK'
    assert actual_character == expected_character, 'data arent  same'


@pytest.mark.test_character_data
def test_character_data(env, character_mock, house_mock):
    sirius_black = CharacterData()
    sirius_black_faculty = sirius_black.graduate
    gryffindor = HouseData()
    is_gryffindor = gryffindor.name
    assert sirius_black_faculty == is_gryffindor, "Sirius Black studied at the Gryffindor faculty"


@pytest.mark.test_character_data
def test_character_data_(env, character_mock, house_mock):
    character_data = CharacterData()
    sirius_black = character_data.name
    gryffindor = HouseData()
    gryffindor_best_students_list = gryffindor.best_students
    assert sirius_black in gryffindor_best_students_list, "Sirius was one of the strongest Gryffindor's students"
