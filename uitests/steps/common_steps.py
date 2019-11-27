# -*- coding: utf-8 -*-
"""
    ui-tests.common_steps
    ~~~~~~~~~~~~~~~~~~~~~

    This module holds common behave steps for navigation
"""

from behave import when, then, given
#import subprocess
from time import sleep
#from multiprocessing import process
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from uitests.lib.selenium import click_on, test_value_presence, test_element_visibility

HOME_MENU_ID = 'sidebar.home'



@when('I click dialog button "{item}"')
@then('I click dialog button "{item}"')
def click_dialog_button(context, item):
    """
    Clicks on dialog button
    """

    click_on(context, By.XPATH, '//button[contains(., "{}")]'.format(item))
    
@when('I click button by xpath "{item}"')
@then('I click button by xpath "{item}"')
def click_button(context, item):
    """
    Clicks on dialog button
    """

    click_on(context, By.XPATH, item)
    
    
@when('I click radio button id "{item}"')
@then('I click radio button id "{item}"')
def click_radio_button(context, item):
    """
    Clicks on radio button
    """
    click_on(context, By.XPATH, '//input[contains(., "{}")]'.format(item))

#alert = world.browser.switch_to.alert
#alert.accept()

@when('I click "{item}" menu option')
@then('I click "{item}" menu option')
def go_home(context,item):
    """
    Navigates to home page
    """

    click_on(context, By.XPATH, '//span[contains(., "{}")]'.format(item))


@when('I enter "{value}" for select "{field}"')
@then('I enter "{value}" for select "{field}"')

def enter_value_for_select(context, value, field):
    """
    Sets value to a select field identified by field name.
    """

#     Select(context.browser.find_element_by_id(field)).select_by_value(value)

    mySelectElement = context.browser.find_element_by_id(field)
    dropDownMenu = Select(mySelectElement)
    WebDriverWait(context.browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, field)))
    dropDownMenu.select_by_value(value)


@when('I enter "{value}" text for select "{field}"')
@then('I enter "{value}" text for select "{field}"')

def enter_text_value_for_select(context, value, field):
    """
    Sets value to a select field identified by field name.
    """
    
    Select(context.browser.find_element_by_id(field)).select_by_visible_text(value)

@when('I enter "{value}" text for select name "{field}"')
@then('I enter "{value}" text for select name "{field}"')

def enter_text_value_for_select(context, value, field):
    """
    Sets value to a select field identified by field name.
    """

    Select(context.browser.find_element_by_name(field)).select_by_visible_text(value)
    
@when('I enter "{value}" text for select xpath "{field}"')
@then('I enter "{value}" text for select xpath "{field}"')

def enter_text_value_for_select(context, value, field):
    """
    Sets value to a select field identified by field xpath.
    """

    Select(context.browser.find_element_by_xpath(field)).select_by_visible_text(value)
    

@when('I wait for visibility {seconds} seconds')
@then('I wait for visibility {seconds} seconds')

def wait_for_seconds(context, seconds):
    """
    Wait for `seconds` seconds
    """

    try:
        test_element_visibility(context, By.ID, "dummy_id", seconds)
    except TimeoutException:
        pass


@when('I click "{item}"')
def click_on_href(context, item):
    """
    Clicks on the href item
    """

    click_on(context, By.XPATH, '//a[.//text()="{}"]'.format(item))

@when('I click id named "{item}"')
@then('I click id named "{item}"')
def click_on_id_name(context, item):
    """
    Clicks on the id name
    """

    myElement = context.browser.find_element_by_id(item)
    WebDriverWait(context.browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, item)))
    click_on(context, By.ID, item)
    
@when('I click button named "{item}"')
@then('I click button named "{item}"')
def click_on_button_name(context, item):
    """
    Clicks on button
    """

    click_on(context, By.NAME, item)
    
@when('I do logout')
@then('I do logout')
def click_on_logout(context, item):
    """
    Clicks on logout
    """

    click_on(context, By.XPATH, '/html/body/app-root/div/main/app-gheader/header/div/div[2]/span[2]/a')

@when('the field "{field}" should have the value "{value}"')
@then('the field "{field}" should have the value "{value}"')
def check_field_value(context, value, field):
    
    """
    Checks field value.
    """

    test_value_presence(context, By.ID, field, value)

@when('The badge field "{field}" should have the value "{value}"')
@then('The badge field "{field}" should have the value "{value}"')
def check_field_value(context, value, field):
    
    """
    Checks badge value.
    """
    myBadgeElement = context.browser.find_element_by_id(field);
    assert myBadgeElement.text == value;

@when('The status of "{field}" should be "{value}"')
@then('The status of "{field}" should be "{value}"')
def check_status(context,field,value):
    """
    checks the nimo status
    """
    data = context.browser.find_element_by_id(field);
    assert data.text == value;

@when('the name field "{field}" should have the value "{value}"')
@then('the name field "{field}" should have the value "{value}"')
def check_field_value(context, value, field):
    
    """
    Checks field value.
    """

    test_value_presence(context, By.NAME, field, value)
    
    
@then('I should get the error message saying "{message}"')
def check_field_value(context, message):
    """
    Checks alert error message.
    """

    msg = context.browser.switch_to.alert.text
    assert msg == message

@when('I wait for {secs} seconds')
@then('I wait for {secs} seconds')
def step_impl(context, secs):
     """
     sleep wait for secs
     :param context:
     :param secs:
     :return:
     """
     sleep(int(secs))

     