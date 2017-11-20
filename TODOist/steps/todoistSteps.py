from compare import *

@given(u'I ask for the list of projects')
def step_impl(context, host):
    context.host = host
    print(context.host)

@when(u'I enter the token')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter the token')

@then(u'I get the list of projects')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get the list of projects')
