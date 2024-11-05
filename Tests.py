from Client import PetstoreClient


def assign_test_id(test_id):  # Декоратор для назначения айдишки тестам
    def decorator(func):
        func.test_id = test_id
        test_cases[test_id] = func
        return func
    return decorator


test_cases = {}  # Хранение тестов по их Id


@assign_test_id("1")  # Post/pet
def test_create_pet(client, pet_data):
    print("Create a pet. Verify response.")
    create_response = client.create_pet(pet_data)
    print("Create response:", create_response)
    assert create_response["id"] == pet_data["id"]
    assert create_response["category"]["name"] == pet_data["category"]["name"]
    assert create_response["name"] == pet_data["name"]
    assert create_response["status"] == pet_data["status"]
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


@assign_test_id("2")  # Put/pet
def test_update_pet(client, pet_data):
    pet_data["status"] = "sold"
    print("Update pet. Verify response.")
    update_response = client.update_pet(pet_data)
    print("Update response:", update_response)
    assert update_response["id"] == pet_data["id"]
    assert update_response["status"] == "sold"
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


@assign_test_id("3")  # GET /pet/findByStatus
def test_get_pet_by_status(client, pet_data):
    print("GET pet by status and verify response.")
    pets = client.get_pet_by_status("sold")
    print("Get by status response:", pets)
    assert any(pet["id"] == pet_data["id"] for pet in pets)
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


@assign_test_id("4")  # GET /pet/{id}
def test_get_pet_by_id(client, pet_data):
    print("GET pet by id and verify response.")
    pet_by_id = client.get_pet_by_id(pet_data["id"])
    print("Get by ID response:", pet_by_id)
    assert pet_by_id is not None
    assert pet_by_id["id"] == pet_data["id"]
    assert pet_by_id["status"] == "sold"
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


@assign_test_id("5")  # DELETE /pet/{petId}
def test_delete_pet(client, pet_data):
    print("Delete pet.")
    delete_response = client.delete_pet(pet_data["id"])
    print("Delete response:", delete_response)
    assert delete_response["message"] == str(pet_data["id"])
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


@assign_test_id("6")  # Verify pet deletion
def test_verify_pet_deletion(client, pet_data):
    print("Verify the pet was deleted.")
    deleted_pet = client.get_pet_by_id(pet_data["id"])
    print("Get by ID after delete response:", deleted_pet)
    assert deleted_pet is None
    print("Test passed")
    print("\n" + "=" * 50 + "\n")


def run_tests_by_ids(*test_ids):  # Функция для запуска конкретного теста по его test_id
    client = PetstoreClient()
    pet_data = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Doggie",
        "photoUrls": [],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }
    for test_id in test_ids:
        test_func = test_cases.get(test_id)
        if test_func:
            print(f"Running test ID {test_id}")
            test_func(client, pet_data)
        else:
            print(f"No test found with ID {test_id}")


if __name__ == "__main__":
    run_tests_by_ids("1", "5", "6")
