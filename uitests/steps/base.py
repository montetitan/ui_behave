# -*- coding: utf-8 -*-
"""
    ui-tests.common
    ~~~~~~~~~~~~~~~

    This module holds common methods for page navigation, value submission and other common things.
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from uitests.steps.common_steps import *
from uitests.lib.selenium import open_url, enter_text, click_on, check_title, switch_to_tab , check_url
from lib2to3.pgen2 import driver

LOGIN_BUTTON_ID = 'loginbutton'
#LOGIN_BUTTON_ID = 'u_0_4'
EXPERT_MODE_LINK_ID = 'icon-popout'
HEADER_USER_NAME_ID = 'header-user'


@when('I visit GOOGLE')
def visit_google(context):
    """
    Opens GOOGLE url.
    """
    print("trying to visit",context.url )
    open_url(context, context.url )


@when('I login into GOOGLE')
def login_into_google(context):
    """
    Login using given credentials and create the session
    """
    context.browser.maximize_window();
    context.execute_steps(context.session.format_steps("""
        When I enter "{username}" for id field "email"
        And I enter "{password}" for id field "pass"
        And I submit the login form
    """))
#        And 'I click dialog button "Login"')


@when('I enter "{value}" for field "{field}"')
@then('I enter "{value}" for field "{field}"')
def enter_value_for_field(context, value, field):
    """
    Sets value to a field identified by field name.
    """

    context.browser.find_element_by_name(field).clear()
    enter_text(context, By.NAME, field, value)

@when('I enter "{value}" for partial field "{field}"')
@then('I enter "{value}" for partial field "{field}"')
def enter_value_for_field2(context, value, field):
     """
     Sets value to a field identified by field name.
     """

     context.browser.find_elements_by_partial_link_text(field).clear()
     enter_text(context, By.CSS_SELECTOR, field, value)

@when('I enter "{value}" for id field "{field}"')
@then('I enter "{value}" for id field "{field}"')
def enter_value_for_field_by_id(context, value, field):
    """
    Sets value to a field identified by field id.
    """

    context.browser.find_element_by_id(field).clear()
    enter_text(context, By.ID, field, value)

@when('I enter "{value}" for class field "{field}"')
@then('I enter "{value}" for class field "{field}"')
def enter_value_for_field_by_id(context, value, field):
    """
    Sets value to a field identified by field id.
    """

#    context.browser.find_element_by_name(field).clear()
    enter_text(context, By.CLASS_NAME, field, value)


@when('I enter "{value}" for xpath field "{field}"')
@then('I enter "{value}" for xpath field "{field}"')
def enter_value_for_field_by_id(context, value, field):
    """
    Sets value to a field identified by field id.
    """

    context.browser.find_element_by_xpath('//input[contains(./data-handle,"{}")]'.format(field)).clear()
    enter_text(context, By.XPATH, '//input[contains(./data-handle,"{}")]'.format(field), value)


@when('I submit the login form')
def submit_login_form(context):
    """
    Submits GOOGLE login form. changing to XPATH button for nso 4.7.1
    """
#    click_on(context, By.XPATH, '//label[contains(.,"u_0_4")]')

    click_on(context, By.ID, LOGIN_BUTTON_ID)

@when('page title changed to "{name}"')
@then('page should have a title "{name}"')
def page_have_title(context, name):
    """
    Method checks whether page has title identified by value of param name.
    """

    check_title(context, name)



@when('page url changed to "{name}"')
@then('page should have a url "{name}"')
def page_have_title(context, name):
    """
    Method checks whether page has title identified by value of param name.
    """

    check_url(context, name)


@given('I am logged into GOOGLE')
def logged_into_google(context):
    """
    Method will wait 20 seconds for page title to be changed to "WAN Automation Engine"
    """
#     context.window.maximize_window()
    context.execute_steps(context.session.format_steps("""
        When I visit GOOGLE
        And I login into GOOGLE
    """))


# @when('I enter expert mode')
# def enter_expert_mode(context):
#     """
#     Method will click on the expert mode link
#     """
# 
#     click_on(context, By.CLASS_NAME, EXPERT_MODE_LINK_ID)
#     switch_to_tab(context, 1, 40)
    
    
@when('I enter expert mode by id "{item}"')
def enter_expert_mode(context,item):
    """
    Method will click on the expert mode link
    """

    click_on(context, By.ID, item)
    context.browser.switch_to.window(context.browser.window_handles[1])    
