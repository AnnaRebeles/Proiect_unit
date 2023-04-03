import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestPlaceOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        sleep(2)

    def test_quantity(self):

        add_to_cart_item1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_item1.click()
        add_to_cart_item2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart_item2.click()
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        assert cart_badge.text == "2"

    def test_place_order(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        self.driver.find_element(By.ID, "checkout").click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys(input('Introduceti numele '))
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys(input('Introduceti prenumele '))
        cod_postal = self.driver.find_element(By.ID, "postal-code")
        cod_postal.send_keys(input('Introduceti codul postal '))
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        self.driver.find_element(By.ID, "finish").click()

        succes = self.driver.find_element(By.CLASS_NAME, "complete-header")

        assert succes.text == "Thank you for your order!"

    def tearDown(self):
        self.driver.close()
