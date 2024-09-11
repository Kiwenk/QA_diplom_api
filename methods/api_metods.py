import requests
import json

from path import path_resources, path_schemas


class Pet_api:
    def __init__(self):
        pass

    def pet_find_by_status_get(self, base_url):
        response = requests.get(url=f'{base_url}pet/findByStatus/', params={'status': 'available'})
        with open(f'{path_schemas('get_by_status.json')}') as file:
            data_validate = json.load(file)
        data_load = response.json()
        return response, data_load, data_validate

    def pet_id_get(self, base_url, pet_id):
        response = requests.get(url=f'{base_url}pet/{pet_id}')
        with open(f'{path_schemas('get_by_id.json')}') as file:
            data_validate = json.load(file)
        data_load = response.json()
        return response, data_load, data_validate

    def post_pet(self, base_url):
        with open(f'{path_resources('post_pet.json')}') as file:
            data_upload = json.load(file)
        response = requests.post(url=f'{base_url}pet/', json=data_upload)
        with open(f'{path_schemas('post_pet.json')}') as file:
            data_validate = json.load(file)
        data_load = response.json()
        return response, data_load, data_validate


class Store_api:
    def __init__(self):
        pass

    def post_store(self, base_url):
        with open(f'{path_resources('post_store.json')}') as file:
            data_upload = json.load(file)
        response = requests.post(url=f'{base_url}store/order', json=data_upload)
        data_load = response.json()
        id_order = data_load["id"]
        with open(f'{path_schemas('post_store.json')}') as file:
            data_validate = json.load(file)
        return response, data_load, data_validate, id_order

    def delete_store(self, base_url, id_order):
        response = requests.delete(url=f'{base_url}store/order/{id_order}')
        data_load = response.json()
        with open(f'{path_schemas('delete_store.json')}') as file:
            data_validate = json.load(file)
        return response, data_load, data_validate


pet_api_responses = Pet_api()
store_api_responses = Store_api()
