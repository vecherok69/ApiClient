import unittest
from PetStoreTests import test_cases, TestCreatePet, TestUpdatePet, TestGetPetByStatus, TestGetPetById, TestDeletePet, TestVerifyPetDeletion


class TestRunner:
    @staticmethod
    def run_all_tests():
        unittest.main()

    @staticmethod
    def run_tests_by_ids(*test_ids):
        test_suite = unittest.TestSuite()
        for test_id in test_ids:
            if test_id in test_cases:
                test_func = test_cases[test_id]
                test_class = globals()[test_func.__qualname__.split('.')[0]]
                test_suite.addTest(test_class(test_func.__name__))
            else:
                print(f"Test ID {test_id} not found.")
        runner = unittest.TextTestRunner()
        runner.run(test_suite)


if __name__ == "__main__":
    TestRunner.run_tests_by_ids("1", "2", "3", "4", "5", "6")
    #TestRunner.run_all_tests()
