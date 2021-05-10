from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest,time,re

class myTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.base_url="http://127.0.0.1:5000/"

    def test01(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("login_button").click()


    def test02(self):
        pass

    def tearDown(self) -> None:
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()