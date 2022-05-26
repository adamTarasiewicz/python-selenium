from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """This class is the parent of all pages"""
    """It contains all the generic methods and utilities for all the pages we want to test"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_current_url(self):
        url = self.driver.current_url
        return str(url)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element_attribute(self, by_attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_attribute))
        return element.get_attribute()

    def hover(self, by_attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_attribute))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()


'''    
    # define more methods of BasePage class
    def get_something(self, by_attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located())
        return something (or not)
'''
