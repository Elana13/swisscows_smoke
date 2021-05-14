from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_FIELD = By.CSS_SELECTOR, 'form .input-search'
    REGION_BUTTON = By.CSS_SELECTOR, '.regions .button-toggle'
    REGION_SELECTION = By.CSS_SELECTOR, '.region-selection'
    REGION_LIST = By.CSS_SELECTOR, '.region-popup > ul > li'
    REGION_WITH_NEWS = By.CSS_SELECTOR, '.region-popup > ul li:nth-child(14)'
    SUGGEST_SECOND_ITEM = By.CSS_SELECTOR, 'ul.suggestions :nth-child(2)' #'ul.suggestions > li'
    NEWS_WIDGET = By.CLASS_NAME, 'news--startpage'

    SERVICES_BUTTON = By.CLASS_NAME, 'button-services'
    SERVICES_LIST = By.CSS_SELECTOR, '.list-services > li > a' #[href^="/news"]

    EXTENSION_LINK = By.CSS_SELECTOR, 'a[href^="https://chrome.google.com/webstore"]'
    MOREINFO_LINK = By.CSS_SELECTOR, 'a[href^="/en/about"]'

