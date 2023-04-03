import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def test_add_to_cart(self):
        item = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
        item.click()
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"

    def test_remove_from_cart(self):
        item = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
        item.click()
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        remove_from_cart_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_from_cart_button.click()
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert cart_badge.text == ""

    def tearDown(self):
        self.driver.close()
