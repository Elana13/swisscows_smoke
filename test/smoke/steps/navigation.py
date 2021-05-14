from behave import *
from selenium import webdriver

from test.smoke.page_models.digest_page import DigestPage
from test.smoke.page_models.home_page import HomePage
from test.smoke.page_models.plus_page import PlusPage
from test.smoke.page_models.web_page import WebPage

use_step_matcher('re')

@given("User is on Homepage")
def step_impl(context):
    context.driver = webdriver.Chrome('d:\\ChromeDriver\\chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('User is on Web page with "(.*)" query')
def step_impl(context, query):
    context.driver = webdriver.Chrome('d:\\ChromeDriver\\chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url + f"?query={query}")
    context.driver.implicitly_wait(15)

@then("User is on Web page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expected_url = WebPage(context.driver).url
    assert expected_url in context.driver.current_url

@then('Region "(.*)" is added to url')
def step_impl(context, region):
    assert f"?region={region}" in context.driver.current_url

@then("User is on Digest page")
def step_impl(context):
    expected_url = DigestPage(context.driver).url
    assert expected_url in context.driver.current_url

@then("User is on Plus page")
def step_impl(context):
    expected_url = PlusPage(context.driver).url
    assert expected_url == context.driver.current_url

@when("Move to the next tab")
def step_impl(context):
    original_window = context.driver.current_window_handle
    print(original_window)
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break

@then('User is on site "(.*)"')
def step_impl(context, site_name):
    expected_url = f"https://{site_name}.com/en"
    print(context.driver.current_url)
    print(expected_url)
    assert expected_url.startswith(context.driver.current_url)

@then("User is on Google store page")
def step_impl(context):
    expected_url = "https://chrome.google.com/webstore/detail/swisscows"
    assert expected_url in context.driver.current_url

@then("Next 10 results are displayed")
def step_impl(context):
    expected_url = "https://dev.swisscows.com/web?query=appple&offset=10"
    assert expected_url == context.driver.current_url








