from Test.Pages.Signup_page import signup_locators


class signnup():

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, firstname):
        self.driver.find_element_by_id(signup_locators.userfirstnametextbox_id).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element_by_id(signup_locators.userlastnametextbox_id).send_keys(lastname)
