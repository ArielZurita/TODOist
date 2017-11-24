from json import *
from compare import *
from utils.utilGetJson import *
from utils.apiLib import *

@given(u'I do not send a {id}')
def step_impl(context, id):
    context.id = None

@then(u'I get all projects')
def step_impl(context):
    expect(context.result.json()).to_equal(context.data)

@then(u'I get response with name entered')
def step_impl(context):
    dir = context.data
    name = dir["name"]
    allresponse = context.result.json()
    dataToCompare = "name"
    if dataToCompare in allresponse:
        expect(str(allresponse[dataToCompare])).to_equal(str(name))
