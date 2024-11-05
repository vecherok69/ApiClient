import requests


class PetstoreClient:
    def __init__(self, base_url="https://petstore.swagger.io/v2"):
        self.base_url = base_url

    def create_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.post(url, json=pet_data)
        response.raise_for_status()
        return response.json()

    def update_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.put(url, json=pet_data)
        response.raise_for_status()
        return response.json()

    def get_pet_by_status(self, status):
        url = f"{self.base_url}/pet/findByStatus"
        response = requests.get(url, params={"status": status})
        response.raise_for_status()
        return response.json()

    def get_pet_by_id(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    def delete_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.delete(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
