from test.smoke.locators.home_page import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://dev.swisscows.com'

    @property
    def search_field(self):
        return self.driver.find_element(*HomePageLocators.SEARCH_FIELD)

    @property
    def suggest_second_item(self):
        return self.driver.find_element(*HomePageLocators.SUGGEST_SECOND_ITEM)

    @property
    def region_button(self):
        return self.driver.find_element(*HomePageLocators.REGION_BUTTON)

    @property
    def region_selection(self):
        return self.driver.find_element(*HomePageLocators.REGION_SELECTION)

    @property
    def region_list(self):
        return self.driver.find_element(*HomePageLocators.REGION_LIST)

    @property
    def region_with_news(self):
        return self.driver.find_element(*HomePageLocators.REGION_WITH_NEWS)

    @property
    def news_widget(self):
        return self.driver.find_element(*HomePageLocators.NEWS_WIDGET)

    @property
    def services_button(self):
        return self.driver.find_element(*HomePageLocators.SERVICES_BUTTON)

    @property
    def services_list(self):
        return self.driver.find_elements(*HomePageLocators.SERVICES_LIST)

    @property
    def extension_link(self):
        return self.driver.find_element(*HomePageLocators.EXTENSION_LINK)





