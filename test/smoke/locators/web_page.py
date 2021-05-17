from selenium.webdriver.common.by import By


class WebPageLocators:
    SEARCH_FIELD = By.CSS_SELECTOR, 'form .input-search'
    SUGGEST_SECOND_ITEM = By.CSS_SELECTOR, 'ul.suggestions :nth-child(2)'
    WEB_RESULTS = By.CLASS_NAME, 'web-results'
    DID_YOU_MEAN = By.CLASS_NAME, 'message.warning.compact'
    SECOND_PAGE = By.CSS_SELECTOR, '.web-pagination li.number a' #'.web-pagination > li.active + li > a'
    WEB_PAGINATION = By.CSS_SELECTOR, '.web-pagination'

