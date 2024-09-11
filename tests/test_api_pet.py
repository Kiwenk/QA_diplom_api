from methods.api_metods import pet_api_responses
from methods.utils_for_tests import make_checking_greate_again
from jsonschema import validate


def test_post_pet(setup_base_url):
    res = pet_api_responses.post_pet(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    assert res[0].status_code == 200, 'Код ответа не равен 200'
    validate(data_load, data_validate)
    make_checking_greate_again.check_data_load_pet_name_get_by_id(data_load)


def test_pet_find_by_status(setup_base_url):
    pet_api_responses.post_pet(setup_base_url)
    res = pet_api_responses.pet_find_by_status_get(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    assert res[0].status_code == 200, 'Код ответа не равен 200'
    validate(data_load, data_validate)
    make_checking_greate_again.check_data_load_pet_name_get_by_status(data_load)


def test_pet_find_by_id(setup_base_url):
    pet_api_responses.post_pet(setup_base_url)
    res = pet_api_responses.pet_id_get(setup_base_url, 16)
    data_load = res[1]
    data_validate = res[2]
    assert res[0].status_code == 200, 'Код ответа не равен 200'
    validate(data_load, data_validate)
    make_checking_greate_again.check_data_load_pet_name_get_by_id(data_load)
