import sys

from behave import *
from test.smoke.page_models.home_page import HomePage
from test.smoke.page_models.web_page import WebPage

use_step_matcher('re')


@then("Cursor is on the Search field")
def step_impl(context):
    page = HomePage(context.driver)
    active_element = context.driver.switch_to.active_element
    #print(active_element.get_attribute("class"))
    assert page.search_field == active_element

@then('Suggest appears')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.suggest_second_item.is_enabled()

@then("Region is selected")
def step_impl(context):
    page = HomePage(context.driver)
    assert page.region_selection.text == "Argentina"

@then("News widget is present")
def step_impl(context):
    page = HomePage(context.driver)
    assert page.news_widget.is_enabled()


@then('Link "(.*)" in Services')
def step_impl(context, link_text):
    page = HomePage(context.driver)
    page.services_button.click()
    services = page.services_list
    matching = []
    for s in services:
        print(s.text)
        if link_text in s.text:
            matching.append(s)
    if len(matching) > 0:
        assert matching[0].is_enabled()
    else:
        raise RuntimeError()

@then('Initial query was not changed')
def step_impl(context):
    page = WebPage(context.driver)
    print(page.search_field.get_attribute('value'))
    assert page.search_field.get_attribute('value') == '"Apple iPhone" grün'

@then('Results exist')
def step_impl(context):
    page = WebPage(context.driver)
    page.web_results.is_enabled()

@then('Did you mean appears')
def step_impl(context):
    page = WebPage(context.driver)
    page.did_you_mean.is_enabled()












