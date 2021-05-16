from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time, re


class myTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.base_url = "http://127.0.0.1:5000/"

    def test01(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.find_element_by_class_name("loginbutton").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("register_button").click()
        time.sleep(1)
        name = "feijigeigege"
        email = 'egiegiengie@gmail.com'
        password = "1234567"
        self.driver.find_element_by_name('username').send_keys(name)
        time.sleep(0.5)
        self.driver.find_element_by_name('email').send_keys(email)
        time.sleep(0.5)
        self.driver.find_element_by_name('password').send_keys(password)
        time.sleep(0.5)
        self.driver.find_element_by_name('password2').send_keys(password)
        time.sleep(0.5)
        self.driver.find_element_by_name('submit').click()
        time.sleep(1)
        text1 = self.driver.find_element_by_class_name('redp').text
        print(text1, "\nTest1 finished!")

    def test02(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(1)
        self.driver.find_element_by_xpath("//ul[@class = 'ul_mainstyle']//li[2]").click()
        time.sleep(1)
        items = self.driver.find_elements_by_xpath("//ul[@class = 'sideul']//li[not(@class)]")
        for _ in items[1:len(items)-1]:
            self.driver.find_element_by_class_name("next").click()
            time.sleep(0.8)
        text2 = self.driver.find_element_by_class_name("congrats").text
        print(text2, "\nTest2 finished!")

    def tearDown(self) -> None:
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
