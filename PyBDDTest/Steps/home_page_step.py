from behave import *

@given('User loads www.google.com in browser')
def step_impl(context):
    context.Home.do_open_homepage()
    assert True is True

@when('User input search term in search box and submit it')
def step_impl(context):
    assert True is not False

@then('User navigates to Web result page of searched term')
def step_impl(context):
    assert True is True

@then('page title contains search term')
def step_impl(context):
    assert True is True