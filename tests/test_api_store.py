from methods.api_metods import store_api_responses
from methods.utils_for_tests import make_checking_greate_again
from jsonschema import validate


def test_post_store(setup_base_url):
    res = store_api_responses.post_store(setup_base_url)
    data_load = res[1]
    data_validate = res[2]
    assert res[0].status_code == 200, 'Код ответа не равен 200'
    validate(data_load, data_validate)
    make_checking_greate_again.check_status_order(data_load)


def test_delete_order(setup_base_url):
    order = store_api_responses.post_store(setup_base_url)
    res = store_api_responses.delete_store(setup_base_url, order[3])
    data_load = res[1]
    data_validate = res[2]
    assert res[0].status_code == 200, 'Код ответа не равен 200'
    validate(data_load, data_validate)
    make_checking_greate_again.check_delete_status_response(data_load, order[3])
