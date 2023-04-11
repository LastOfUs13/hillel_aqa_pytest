import pytest
from HW17.data_for_api.character_data import CharacterData
from HW17.data_for_api.house_data import HouseData


@pytest.fixture()
def character_mock():
    return CharacterData(name="Sirius Black", animagus="Black dog")


@pytest.fixture()
def house_mock():
    return HouseData(name="Gryffindor", founder="Godric Gryffindor", best_students=['Hermione Hranger', 'Harry Potter',
                                                                                    'Sirius Black'])
