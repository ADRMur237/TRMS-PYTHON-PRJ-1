from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common import By
from selenium.webdriver.common.by import By


class RequestReimbursementPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def name(self):
        return self.driver.find_element(by=By.ID, value="Name")

    def employee_id(self):
        return self.driver.find_element(by=By.ID, value="EmpId")

    def email_address(self):
        return self.driver.find_element(by=By.ID, value="Email")

    def location(self):
        return self.driver.find_element(by=By.ID, value="location")

    def campus(self):
        return self.driver.find_element(by=By.ID, value="Campus")

    def event_date(self):
        return self.driver.find_element(by=By.ID, value="day")

    def amount_cost(self):
        return self.driver.find_element(by=By.ID, value="amount")

    def other_amount(self):
        return self.driver.find_element(by=By.ID, value="Amount")

    def submit_employee_grade(self):
        return self.driver.find_element(by=By.ID, value="grade")

    def select_department(self):
        return self.driver.find_element(by=By.ID, value="department")

    def graduation_year(self):
        return self.driver.find_element(by=By.ID, value="graduation")

    def supervisor_name(self):
        return self.driver.find_element(by=By.ID, value="Super")

    def supervisor_approval(self):
        return self.driver.find_element(by=By.ID, value="approved")

    def submit_request(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/button")
