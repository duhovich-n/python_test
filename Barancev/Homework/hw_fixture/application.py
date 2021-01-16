from selenium import webdriver
from hw_fixture.session import SessionHelper
from hw_fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_homepage(self):
        driver = self.driver
        if not driver.current_url.endswith("index.php"):
            driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
