import requests

BASE_URL = "https://petstore.swagger.io/v2"

class PetstoreClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def create_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        try:
            response = requests.post(url, json=pet_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating pet: {e}")
            return None

    def update_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        try:
            response = requests.put(url, json=pet_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error updating pet: {e}")
            return None

    def get_pet_by_status(self, status):
        url = f"{self.base_url}/pet/findByStatus"
        try:
            response = requests.get(url, params={"status": status})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting pets by status: {e}")
            return []

    def get_pet_by_id(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        try:
            response = requests.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting pet by id: {e}")
            return None

    def delete_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error deleting pet: {e}")
            return None
