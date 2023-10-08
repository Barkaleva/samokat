#Баркалёва Ольга, кагорта 8а, инженер по тестированию плюс

def create_order():
    current_body = data.order_body()
    track_number = sender_test.post_new_order(current_body)
    return str(track_number.json()["track"])
def positive_assert():
    track_number = create_order()
    current_params = data.params_get.copy()
    current_params["t"] = track_number
    response = sender_test.get_order(current_params)
    assert response.status_code == 200

def test_order():
    positive_assert()