import pytest
from human import Human

@pytest.fixture()
def create_dude():
    yield Human('Endy', 27, 'male')
    # print('\n some kind tear down')


@pytest.fixture()
def create_female(create_dude):
    dude = create_dude
    dude.change_gender('female')
    yield dude


@pytest.fixture()
def create_old_dude():
    yield Human('Peter', 99, 'male')


@pytest.fixture()
def create_dead(create_old_dude):
    dude = create_old_dude
    dude.grow()
    dude.grow()
    yield dude


@pytest.fixture()
def create_human_with_params():
    def __create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    yield __create_human


@pytest.fixture
def create_wrong_gender():
    yield Human('Kelly', 17, 'new gender')
