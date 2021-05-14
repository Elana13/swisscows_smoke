from selenium.webdriver.common.by import By


class WebPageLocators:
    SEARCH_FIELD = By.CSS_SELECTOR, 'form .input-search'
    WEB_RESULTS = By.CLASS_NAME, 'web-results'
    DID_YOU_MEAN = By.CLASS_NAME, 'message.warning.compact'
    SECOND_PAGE = By.CSS_SELECTOR, '.web-pagination > li.active + li > a'
    WEB_PAGINATION = By.CSS_SELECTOR, '.web-pagination'

