from HW17.tests.api_tests.conftest import character_mock, house_mock
from HW17.api_collections.houses_api import HousesAPI
from HW17.data_for_api.house_data import HouseData
from http import HTTPStatus


def test_get_house_api(env, house_mock):
    expected_house = house_mock
    response = HousesAPI(env).get_house(1)
    response_data = response.json()
    actual_house = HouseData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'status code is note OK'
    assert actual_house == expected_house, 'data arent  same'