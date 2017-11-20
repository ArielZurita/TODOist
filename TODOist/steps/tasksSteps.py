from compare import *

@given(u'I connect to the \'task service\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I connect to the \'task service\'')

@when(u'I enter a valid \'token\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid \'token\'')

@when(u'I enter a valid \'task identifier\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid \'task identifier\'')

@then(u'I get status code \'200\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get status code \'200\'')
