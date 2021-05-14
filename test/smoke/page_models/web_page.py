from test.smoke.locators.web_page import WebPageLocators


class WebPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://dev.swisscows.com/web'

    @property
    def search_field(self):
        return self.driver.find_element(*WebPageLocators.SEARCH_FIELD)

    @property
    def web_results(self):
        return self.driver.find_element(*WebPageLocators.WEB_RESULTS)

    @property
    def did_you_mean(self):
        return self.driver.find_element(*WebPageLocators.DID_YOU_MEAN)

    @property
    def second_page(self):
        return self.driver.find_element(*WebPageLocators.SECOND_PAGE)

    @property
    def pagination(self):
        return self.driver.find_element(*WebPageLocators.WEB_PAGINATION)

