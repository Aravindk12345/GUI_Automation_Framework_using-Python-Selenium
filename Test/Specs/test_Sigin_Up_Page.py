from selenium import webdriver
import unittest
from Test.Actions.Signup_page_actions import *

class sign_up(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Aravind/Desktop/poc/GUI_Automation_Framework/Test/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_start(self):
        driver = self.driver
        driver.get("https://facebook.com")
        # driver.implicitly_wait(30)

        sign = signnup(driver)
        sign.enter_first_name("Aravind")
        sign.enter_last_name("Reddy")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Execution completed")

if __name__ == '__main__':
    unittest.main()
