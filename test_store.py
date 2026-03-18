from jsonschema import validate
import pytest
import schemas
import random
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.fixture
def create_pets():
    value = random.randint(5, 99)
    test_endpoint = "/pets"
    payload = {
                "id": value,
                "name": "string",
                "type": "cat",
                "status": "available"
            }
    response = api_helpers.post_api_data(test_endpoint, payload,optional_headers={"Content-Type": "application/json"})
    assert response.status_code == 201
    data = response.json()
    print("Response Pets Data:", data)  
    pet_id = data["id"]
    print("Created Pets ID:", pet_id)
    return pet_id

@pytest.fixture
def create_order(create_pets):
    pet_id = create_pets
    test_endpoint = "/store/order"
    payload = {"pet_id":pet_id} 

    response = api_helpers.post_api_data(test_endpoint, payload,optional_headers={"Content-Type": "application/json"})
    assert response.status_code == 201

      # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.order)

    data = response.json()
    print("Response Store Data:", data)
    order_id = data["id"]
    print("Created Store Order ID:", order_id)
    return order_id

def test_patch_order_by_id(create_order):
    order_id = create_order
    test_endpoint = f"/store/order/{order_id}"
    payload = {"status":"available"} 
    response = api_helpers.patch_api_data(test_endpoint, payload,optional_headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    response_data = response.json()
    print("Response Patch Data:", response_data)
    Expected_message = "Order and pet status updated successfully"
    assert_that(response_data["message"], contains_string(Expected_message))
    print("PATCH Response Message validated successfully:", response_data.get("message"))


def test_patch_order_not_found():
    order_id = 11111
    test_endpoint = f"/store/order/{order_id}"
    payload = {"status":"available"} 
    response = api_helpers.patch_api_data(test_endpoint, payload,optional_headers={"Content-Type": "application/json"})
    assert response.status_code == 404
    response_data = response.json()
    expected_message = "Order not found"
    assert "message" in response_data
    assert expected_message in response_data["message"]
    
