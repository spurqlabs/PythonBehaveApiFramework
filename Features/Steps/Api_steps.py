from behave import *

# use_step_matcher("parse")
from Utility.API_Utility import API_Utility

api_util = API_Utility()


@when('User sends "{method}" call to endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_util.Method_Call(context.table, method, endpoint)


@then('User verifies the status code is "{status_code}"')
def step_impl(context, status_code):
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)


@step("User verifies GET response contains following information")
def step_impl(context):
    api_util.Verify_GET(context.table)
    response_body = response.json()
    assert response_body['data']['first_name'] == context.table[0][0]
    assert response_body['data']['last_name'] == context.table[0][1]
    assert response_body['data']['email'] == context.table[0][2]


@step("User verifies POST response body contains following information")
def step_impl(context):
    api_util.Verify_POST(context.table)
    response_body = response.json()
    assert response_body['name'] == context.table[0][0]
    assert response_body['job'] == context.table[0][1]


@step("User verifies PUT response body contains following information")
def step_impl(context):
    api_util.Verify_PUT(context.table)
    response_body = response.json()
    assert response_body['Name'] == context.table[0][0]
    assert response_body['Job'] == context.table[0][1]


@when('User sends DELETE call to the endpoint "{endpoint}"')
def step_impl(context, endpoint):
    api_util.Delete_Call(endpoint)
