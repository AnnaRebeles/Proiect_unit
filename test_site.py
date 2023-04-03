import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def test_logo(self):
        logo = self.driver.find_element(By.CLASS_NAME, "app_logo")

        assert logo.text == "Swag Labs"

    def test_check_price(self):
        onsie = self.driver.find_element(By.CSS_SELECTOR, "a[id='item_2_title_link'] div[class='inventory_item_name']")
        onsie.click()
        onsie_price = self.driver.find_element(By.CLASS_NAME, "inventory_details_price")

        assert onsie_price.text == "$7.99"

    def test_check_product_name(self):
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        backpack = self.driver.find_element(By.CLASS_NAME, "inventory_details_name.large_size")

        assert backpack.text == "Sauce Labs Backpack"

    def tearDown(self):
        self.driver.close()
