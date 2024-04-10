import functions_framework
import requests


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

    if request_args and 'MealName1' in request_args and 'CourseType1' in request_args:
        params = {
            "MealName1": request_args['MealName1'],
            "CourseType1": request_args['CourseType1']
        }
    else:
        return "Error, MealName1 and CourseType1 parameters are required"

    if 'MealName2' in request_args and 'CourseType2' in request_args:
        params = {
            "MealName1": request_args['MealName1'],
            "CourseType1": request_args['CourseType1'],
            "MealName1": request_args['MealName2'],
            "CourseType1": request_args['CourseType2']
        }

    url = "https://7d78g8kc-5082.use2.devtunnels.ms/api/Meal"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return "Error when performing the query:" + e
