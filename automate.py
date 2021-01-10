from time import sleep
from selenium import webdriver

class HomePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')
        sleep(2)

    def start_login(self):
        return LoginPage(self.browser)

class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(8)

def test_login_page(browser):
    home_pg = HomePage(browser)
    login_pg = home_pg.start_login()
    login_pg.login("-----", "-----")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

browser = webdriver.Chrome()
browser.implicitly_wait(5)

test_login_page(browser)

browser.close()
