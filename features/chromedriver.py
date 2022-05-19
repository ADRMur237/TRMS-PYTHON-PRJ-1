from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

ser = Service(
    "C:/Users/17146/Documents/Work Files/Revature/2203-python-java-with-automation-reston/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=ser)
