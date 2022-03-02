import json
from pytest import fixture


data_path='tests/data-driven/test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param
    return data