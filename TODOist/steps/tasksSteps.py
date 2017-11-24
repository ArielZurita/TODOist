from compare import *
from utils.apiLib import *
from jsondiff import diff

@when(u'I perform "{method}" request to "{endpoint}" endpoint')
def step_impl(context, method, endpoint):
    context.result = perform_request(method, endpoint)

@given(u'I use "{endpoint}" endpoint')
def step_impl(context, endpoint):
    context.endpoint = endpoint

@given(u'I perform "{method}" method')
def step_impl(context, method):
    context.method = method

@when(u'I send the request')
def step_impl(context):
    context.result = perform_request(context.method, context.endpoint, context.id, context.data)

@then(u'I get status code "{code}"')
def step_impl(context, code):
    expect(str(context.result.status_code)).to_equal(code)
    print(context.result.status_code)

@given(u'I sent the proper id: "{id}"')
def step_impl(context, id):
    print(context.id)
    print(id)
    if id not in ("task_id", "label_id", "project_id"):
        context.id = id

@given(u'I will send the following data')
def step_impl(context):
    context.data = json.loads(context.text)

@then(u'I compare data')
def step_impl(context):
    # compare = diff(context.data, context.result.json(), syntax='explicit')
    # print(compare)
    dict = {**context.result.json(),**context.data }
    # compare = diff(dict, context.result.json(), syntax='explicit')
    # print(compare)
    # expect(bool(compare)).to_be_falsy()
    print(dict)
    print(context.result.json())
    expect(dict).to_equal(context.result.json())
