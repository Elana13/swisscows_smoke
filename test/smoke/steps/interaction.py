from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test.smoke.page_models.home_page import HomePage
from test.smoke.page_models.web_page import WebPage
import globals

use_step_matcher('re')

@when('User type text "(.*)" into search field')
def step_impl(context, text):
    page = HomePage(context.driver)
    page.search_field.send_keys(text)
    context.driver.implicitly_wait(10)

@when("User select item from Suggest")
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, 'ul.suggestions :nth-child(2)')
    globals.initialize.suggest_item_text = element.text
    element.click()
    context.driver.implicitly_wait(10)

@when("User switch checkbox")
def step_impl(context):
    page = HomePage(context.driver)
    page.region_button.click()

@when("User open list with regions")
def step_impl(context):
    page = HomePage(context.driver)
    page.region_selection.click()
    context.driver.implicitly_wait(10)

@when("User select random region")
def step_impl(context):
    page = HomePage(context.driver)
    page.region_list.click()

@when("User select region with news")
def step_impl(context):
    page = HomePage(context.driver)
    page.region_with_news.click()

@when("User press Services button")
def step_impl(context):
    page = HomePage(context.driver)
    page.services_button.click()

@when('User press "(.*)" in services')
def step_impl(context, link_text):
    page = HomePage(context.driver)
    services = page.services_list
    for s in services:
        if link_text in s.text:
            matching = s

    if matching != 0:
        matching.click()
    else:
        raise RuntimeError()

@when("User press extension link")
def step_impl(context):
    page = HomePage(context.driver)
    page.extension_link.click()

@when('User type "Apple iPhone" grün query')
def step_impl(context):
    page = HomePage(context.driver)
    page.search_field.send_keys('"Apple iPhone" grün' + Keys.ENTER)

@when("User press second page")
def step_impl(context):
    page = WebPage(context.driver)
    page.second_page.click()



























