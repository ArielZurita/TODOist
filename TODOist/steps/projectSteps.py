from json import *
from compare import *
from utils.apiLib import *

@given(u'I do not send a {id}')
def step_impl(context, id):
    context.id = None

@then(u'I get all projects')
def step_impl(context, data):
    context.data = data
    context.result = perform_request(context.method, context.endpoint)
    expect(context.result.json()).to_equal(data)