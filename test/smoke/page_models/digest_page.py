class DigestPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://dev.swisscows.com/digest'

