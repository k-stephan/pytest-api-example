import requests

base_url = 'http://127.0.0.1:5000'

# GET requests
def get_api_data(endpoint, params = {},optional_headers={}):
    headers = {
        "accept": "application/json",
    }

    if optional_headers:
        headers.update(optional_headers)
    response = requests.get(f'{base_url}{endpoint}', params=params,headers=headers)
    
    return response

# POST requests
def post_api_data(endpoint, data,optional_headers={}):
    headers = {
        "accept": "application/json"
    }
    if optional_headers:
        headers.update(optional_headers)
    response = requests.post(f'{base_url}{endpoint}', json=data,headers=headers)
    return response

# PATCH requests
def patch_api_data(endpoint, data,optional_headers={}):
    headers = {
        "accept": "application/json"
    }
    if optional_headers:
        headers.update(optional_headers)
    response = requests.patch(f'{base_url}{endpoint}', json=data, headers=headers)
    return response 