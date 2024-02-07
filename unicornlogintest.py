import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait # webidriver'i bekletme
from selenium.webdriver.support import expected_conditions # beklenen durumlar
from selenium.webdriver.support import expected_conditions as EC




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()


    def test_login(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        login_button  = driver.find_element(By.NAME, "login")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "login")))
        login_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='woocommerce-error']/li"))
        )
        #error_message = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")
        self.assertEqual(error_message.text.lower(), "error: username is required.")

        #assert "Error:"  in driver.page_source

    def test_login_wrong_username(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        # Yanlış kullanıcı adı giriliyor
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys("wrong_username")

        login_button = driver.find_element(By.NAME, "login")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "login")))
        login_button.click()


            # Hata mesajının kontrolü
        error_message = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, "//ul[@class='woocommerce-error']/li"))
            )
        self.assertEqual(error_message.text.lower(), "error: the password field is empty.")

    def test_login_wrong_username_and_password(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        # Yanlış kullanıcı adı giriliyor
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys("wrong_username")

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("wrong_password")

        login_button = driver.find_element(By.NAME, "login")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "login")))
        login_button.click()

        try:
            # Hata mesajının kontrolü
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@class='woocommerce-error']/li"))
            )
            self.assertEqual(error_message.text.lower(), "error: incorrect username or password.")

        except Exception as e:
            print(f'Hata: {e}')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
