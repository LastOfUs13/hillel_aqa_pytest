import pytest
from pytest import mark


def test_grow(create_dude):
    dude = create_dude
    current_age = dude.age
    dude.grow()
    expected_age = current_age + 1
    assert expected_age == current_age + 1, 'something wrong with age,it should be 28'


def test_change_gender(create_dude):
    dude = create_dude
    dude.change_gender('female')
    assert dude.gender == 'female', 'Endy should be a female'


def test_alive_status(create_female):
    dude = create_female
    assert dude._Human__status == 'alive', 'your dude should be alive'


def test_dead_status(create_dead):
    dude = create_dead
    assert dude._Human__status == 'dead', 'your dude should be dead'


@mark.parametrize('gender', ["male", "female"])
def test_human_gender(create_human_with_params, gender):
    some_human = create_human_with_params('Lucy', 25, gender)
    assert some_human.gender == gender


def test_alive_exception(create_dead):
    dude = create_dead
    with pytest.raises(Exception) as expected:
        dude._Human__is_alive()
    assert f"{dude._Human__name} is already dead..." in str(expected.value)


def test_wrong_gender(create_wrong_gender):
    something = create_wrong_gender
    with pytest.raises(Exception) as expected:
        something._Human__validate_gender(something.gender)
    assert "Not correct name of gender" in str(expected.value)


def test_change_gender_to_same(create_female):
    girl = create_female
    with pytest.raises(Exception) as expected:
        girl.change_gender('female')
    assert f"{girl._Human__name} already has gender '{girl.gender}'" in str(expected.value)

