import os
import sys
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.join(os.path.join(sys.path[0], os.pardir), os.pardir)))
from behave import *
from POM.LoginLogoutPage import LoginLogoutPage

login_link_text = ''
user_name = ''


@given('The user is at the Home Page')
def step_impl(context):
    context.browser.get('http://10.1.22.67/Jamaica/membre.php')

@when('The user Logs In with Valid Credentials')
def step_impl(context):
    for row in context.table:
        context.browser.find_element(*LoginLogoutPage.login_link).click()
        context.browser.find_element(*LoginLogoutPage.username).clear()
        context.browser.find_element(*LoginLogoutPage.username).send_keys(row['UserName'])
        context.browser.find_element(*LoginLogoutPage.password).clear()
        context.browser.find_element(*LoginLogoutPage.password).send_keys(row['Password'])
        context.browser.find_element(*LoginLogoutPage.login_button).click()
        global login_link_text
        global user_name
        login_link_text = context.browser.find_element(*LoginLogoutPage.login_link).text
        user_name = row['UserName']

@then('The user is logged in successfully')
def step_impl(context):
    assert (login_link_text == user_name) is True
