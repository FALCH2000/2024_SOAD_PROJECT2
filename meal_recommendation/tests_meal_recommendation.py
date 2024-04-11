import unittest
from unittest.mock import patch
from main import call_api


class TestGetRecommendation(unittest.TestCase):

    def test_valid_request_1_meal(self):
        request_args = {"CourseType1": "MainCourse", "MealName1": "Lasagna"}
        expected_response = {'status_code': 200, 'message': 'This is a response from local', 'data': {'RecommendedMeals': [
            {'Name': 'Gin and Tonic', 'CourseType': 'Drink'}, {'Name': 'Tiramisu', 'CourseType': 'Dessert'}]}}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])

    def test_valid_request_2_meals(self):
        request_args = {"CourseType1": "MainCourse", "MealName1": "Lasagna",
                        "CourseType2": "Drink", "MealName2": "Mojito"}
        expected_response = {"data": {"RecommendedMeals": [
            {"CourseType": "Dessert", "Name": "Chocolate Mousse"}]}, "message": "This is a response from local", "status_code": 200}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])

    def test_invalid_request_meal_not_exist(self):
        request_args = {"CourseType1": "MainCourse",
                        "MealName1": "Pizza"}
        expected_response = {'status_code': 400, 'message': 'This is a response from local', 'data': {'RecommendedMeals': [
            {'Name': 'Gin and Tonic', 'CourseType': 'Drink'}, {'Name': 'Tiramisu', 'CourseType': 'Dessert'}]}}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])

    def test_invalid_request_meal_name_typo(self):
        request_args = {"CourseType1": "MainCourse",
                        "MealName1": "Pi214/*-sa"}
        expected_response = {
            "data": None, "message": "The MealName1 argument contains invalid characters.", "status_code": 400}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])

    def test_invalid_request_course_type_typo(self):
        request_args = {"CourseType1": "MainCourse5",
                        "MealName1": "Lasagna"}
        expected_response = {
            "data": None, "message": "The CourseType1 argument contains invalid characters.", "status_code": 400}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])

    def test_invalid_request_missing_an_argument(self):
        request_args = {"MealName1": "Lasagna"}
        expected_response = {
            "data": None, "message": "Error, MealName1 and CourseType1 parameters are required", "status_code": 400}

        response = call_api(request_args)

        self.assertEqual(
            expected_response['status_code'], response['status_code'])


if __name__ == '__main__':
    unittest.main()
