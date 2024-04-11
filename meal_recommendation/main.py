import functions_framework
import requests

url = "https://7d78g8kc-5082.use2.devtunnels.ms/api/Meal"


def call_api(request_args):

    if request_args and 'MealName1' in request_args and 'CourseType1' in request_args:
        params = {
            "MealName1": request_args['MealName1'],
            "CourseType1": request_args['CourseType1']
        }
    else:
        return {
            "status_code": 400,
            "message": "Error, MealName1 and CourseType1 parameters are required",
            "data": None
        }

    if 'MealName2' in request_args and 'CourseType2' in request_args:
        params = {
            "MealName1": request_args['MealName1'],
            "CourseType1": request_args['CourseType1'],
            "MealName2": request_args['MealName2'],
            "CourseType2": request_args['CourseType2']
        }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        server_response = {
            "status_code": response.status_code,
            "message": data['message'],
            "data": data['data']
        }

        return server_response

    except requests.exceptions.HTTPError as e:
        data = response.json()
        return {
            "status_code": response.status_code,
            "message": data['message'],
            "data": None
        }


@functions_framework.http
def get_recommendation(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_args = request.args

    return call_api(request_args)
