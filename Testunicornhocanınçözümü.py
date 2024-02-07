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

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))

        # Yanlış kullanıcı adı giriliyor
        username_input = driver.find_element(By.NAME, "username")

        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys("wrong_username")
        password_input.send_keys("wrong_password")

        login_button = driver.find_element(By.NAME, "login")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "login")))
        login_button.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))

        # /html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul

        alert_message = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")

        assert "ERROR: INCORRECT USERNAME OR PASSWORD" in alert_message.text

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
