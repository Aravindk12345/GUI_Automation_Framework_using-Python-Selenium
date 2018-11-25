from selenium.webdriver import chrome
from selenium import webdriver


def test_Setup():
    global driver
    path = "C:\\Users\\Aravind\\Desktop\\xoxoDay_latest\\xoxoDay\\xoxoday_ui\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://facebook.com")


def test_signup_page():
    driver.find_element_by_id("u_0_j").send_keys("Aravind")
    driver.find_element_by_id("u_0_l").send_keys("Reddy")

def test_run_suite():
    print("h")
    quit();


if __name__ == '__main__':
    test_Setup()
    test_signup_page()
    test_run_suite()