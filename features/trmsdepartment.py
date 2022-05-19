from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ReviewRequestsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def locate_request(self):
        return self.driver.find_element(by=By.ID, value="")

    def approve_requests(self):
        return self.driver.find_element(by=By.ID, value="")

    def submit_approval(self):
        return self.driver.find_element(by=By.XPATH, value="")
