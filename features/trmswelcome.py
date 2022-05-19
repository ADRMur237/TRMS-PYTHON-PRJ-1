from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

ser = Service(
    "C:/Users/17146/Documents/Work Files/Revature/2203-python-java-with-automation-reston/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=ser)


class WelcomePage:
    # Dependency Injection (for the constructor)
    def __init__(self, driver: WebDriver):  # <- very important vocabulary term,
        self.driver = driver                # <- allows us to create and manage a driver elsewhere

    def username(self):
        return self.driver.find_element(by=By.ID, value="Name")

    def password(self):
        return self.driver.find_element(by=By.ID, value="Pass")

    def login(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/button")

    def email(self):
        return self.driver.find_element(by=By.ID, value="Email")

    def create_username(self):
        return self.driver.find_element(by=By.ID, value="CreateName")

    def create_password(self):
        return self.driver.find_element(by=By.ID, value="CreatePass")

    def create_login(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/button")
