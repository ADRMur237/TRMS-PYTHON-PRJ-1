import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from features.trmswelcome import WelcomePage
from features.trmsrequest import RequestReimbursementPage
from features.trmsdepartment import ReviewRequestsPage

ser = Service(
    "C:/Users/17146/Documents/Work Files/Revature/2203-python-java-with-automation-reston/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=ser)

welcome_page = WelcomePage(driver)
request_page = RequestReimbursementPage(driver)
review_page = ReviewRequestsPage(driver)


def _test():
    try:
        driver.get(
            "C:/Users/17146/Documents/Work Files/Revature/2203-python-java-with-automation-reston/chromedriver.exe")
        welcome_page.username().send_keys("Name")
        welcome_page.password().send_keys("Pass")
        welcome_page.login().click()
        welcome_page.email().send_keys("Email")
        welcome_page.create_username().send_keys("CreateName")
        welcome_page.create_password().send_keys("CreatePass")
        welcome_page.create_login().click()
        time.sleep(3)
        review_page.locate_request().send_keys("employee")
        review_page.approve_requests().send_keys("approve")
        review_page.submit_approval().click()
        time.sleep(3)
        request_page.name().send_keys("Name")
        request_page.employee_id().send_keys("EmpId")
        request_page.email_address().send_keys("Email")
        request_page.location().click()
        request_page.campus().send_keys("Campus")
        request_page.event_date().send_keys("day")
        request_page.amount_cost().is_selected("amount")
        request_page.other_amount().send_keys("Amount")
        request_page.submit_employee_grade().click()
        request_page.select_department().is_selected()
        request_page.graduation_year().is_selected()
        request_page.supervisor_name().send_keys("Super")
        request_page.supervisor_approval().click()
        request_page.submit_request().click()
        time.sleep(3)

        assert "Request Successfully Added!" == driver.switch_to.alert.text
    except AssertionError:
        print(f"Test: Submit Request - Failed\n Actual text: {driver.switch_to.alert.text}")
    else:
        print("Test: Submit Request - Passed")
    finally:
        driver.quit()


if __name__ == '__main__':
    _test()
