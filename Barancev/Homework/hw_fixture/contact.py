class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        # init contact creation
        driver.find_element_by_link_text(u"Добавить контакт").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_homepage()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_homepage()
        self.select_first_contact()
        # submit deletion
        driver.find_element_by_xpath(u"//input[@value='Удалить']").click()
        driver.switch_to_alert().accept()
        self.app.open_homepage()

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        self.app.open_homepage()
        # open modification form
        driver.find_element_by_xpath(u"//img[@alt='Изменить']").click()
        # fill form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.app.open_homepage()

    def count(self):
        driver = self.app.driver
        self.app.open_homepage()
        return len(driver.find_elements_by_name("selected[]"))
