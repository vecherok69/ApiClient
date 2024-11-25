import softest
import unittest
from PetStoreAPIClient import PetstoreClient
from PetStoreTestData import pet_data
from PetParser import Pet
from PetStatus import PetStatus


def assign_test_id(test_id):
    def decorator(func):
        func.test_id = test_id
        test_cases[test_id] = func
        return func
    return decorator


test_cases = {}


class BaseTest(softest.TestCase):
    shared_data = {}

    def setUp(self):
        self.client = PetstoreClient()
        self.pet_data = pet_data

    def get_test_id(self):
        return self._testMethodName.split('_')[-1]

    def get_assigned_test_id(self):
        return getattr(self, self._testMethodName).test_id


class TestCreatePet(BaseTest):
    @assign_test_id("1")
    def test_create_pet(self):
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestCreatePet")
        pet_data_filtered = {
            'id': self.pet_data['id'],
            'name': self.pet_data['name'],
            'status': PetStatus.AVAILABLE.value
        }
        pet = Pet(**pet_data_filtered)
        create_response = self.client.create_pet(pet.to_json())
        created_pet = Pet.from_json(create_response)
        print(f"[ID {test_id}] Created pet response:", created_pet.to_json())
        self.soft_assert(self.assertEqual, created_pet.id, pet.id)
        self.soft_assert(self.assertEqual, created_pet.name, pet.name)
        self.soft_assert(self.assertEqual, created_pet.status, pet.status)
        self.assert_all()
        BaseTest.shared_data['created_pet_id'] = created_pet.id
        print("Test passed\n")


class TestUpdatePet(BaseTest):
    @assign_test_id("2")
    def test_update_pet(self):
        self.pet_data["status"] = PetStatus.SOLD.value
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestUpdatePet")
        update_response = self.client.update_pet(self.pet_data)
        print(f"[ID {test_id}] Update response:", update_response)
        self.soft_assert(self.assertEqual, update_response["id"], self.pet_data["id"])
        self.soft_assert(self.assertEqual, update_response["status"], PetStatus.AVAILABLE.value)
        self.assert_all()
        print("Test passed\n")


class TestGetPetByStatus(BaseTest):
    @assign_test_id("3")
    def test_get_pet_by_status(self):
        created_pet_id = BaseTest.shared_data.get('created_pet_id')
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestGetPetByStatus")
        if created_pet_id:
            pet_response = self.client.get_pet_by_id(created_pet_id)
            pet = Pet.from_json(pet_response)
            print(f"[ID {test_id}] Get pet by status response:", pet.to_json())
            self.soft_assert(self.assertEqual, pet.id, created_pet_id)
            self.soft_assert(self.assertEqual, pet.status, self.pet_data["status"])
            self.assert_all()
            print("Test passed\n")
        else:
            self.fail(f"[ID {test_id}] No pet ID found from test_create_pet")


class TestGetPetById(BaseTest):
    @assign_test_id("4")
    def test_get_pet_by_id(self):
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestGetPetById")
        pet_by_id = self.client.get_pet_by_id(self.pet_data["id"])
        print(f"[ID {test_id}] Get by ID response:", pet_by_id)
        self.soft_assert(self.assertIsNotNone, pet_by_id)
        self.soft_assert(self.assertEqual, pet_by_id["id"], self.pet_data["id"])
        self.soft_assert(self.assertEqual, pet_by_id["status"], PetStatus.SOLD.value)
        self.assert_all()
        print("Test passed\n")


class TestDeletePet(BaseTest):
    @assign_test_id("5")
    def test_delete_pet(self):
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestDeletePet")
        delete_response = self.client.delete_pet(self.pet_data["id"])
        print(f"[ID {test_id}] Delete response:", delete_response)
        self.soft_assert(self.assertEqual, delete_response["message"], str(self.pet_data["id"]))
        self.assert_all()
        print("Test passed\n")


class TestVerifyPetDeletion(BaseTest):
    @assign_test_id("6")
    def test_verify_pet_deletion(self):
        test_id = self.get_assigned_test_id()
        print(f"[ID {test_id}] TestVerifyPetDeletion")
        deleted_pet = self.client.get_pet_by_id(self.pet_data["id"])
        print(f"[ID {test_id}] Get by ID after delete response:", deleted_pet)
        self.soft_assert(self.assertIsNone, deleted_pet)
        self.assert_all()
        print("Test passed\n")
