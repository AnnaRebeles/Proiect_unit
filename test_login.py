import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_check_url(self):
        expected_url = "https://www.saucedemo.com/"
        actual_url = self.driver.current_url
        sleep(2)
        assert expected_url == actual_url, "Error: URL-ul nu este corect"

    def test_valid_login(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID,"password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        login_url = "https://www.saucedemo.com/inventory.html"
        actual_login_url = self.driver.current_url
        assert login_url == actual_login_url, "Error: username sau parola incorecta"

    def test_invalid_login(self):
        username = self.driver.find_element(By.ID,"user-name")
        password = self.driver.find_element(By.ID,"password")
        username.send_keys("invalid_user")
        password.send_keys("invalid_password")
        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()
        assert "Epic sadface: Username and password do not match any user in this service" in self.driver.page_source

    def tearDown(self):
        self.driver.close()
