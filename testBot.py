from selenium import webdriver,common
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time, re
from app.models import User
from app import app, db


class myTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://127.0.0.1:5000/"
        self.u = ["Arran", "Bob", "Sam", "Tim", "Tom", "Hacker", "Lam", "Zikkel"]
        self.p = ["123456", "000000", "122222", "121212", "242424242", "353553535", "993993", "jijiefe"]
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        db.create_all()

    def test01(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)
        except common.exceptions.NoSuchElementException as e:
            raise Exception(e, "\nDue to non-running server.")

        try:
            time.sleep(2)
            self.driver.find_element_by_class_name("loginbutton").click()
            time.sleep(1)
            self.driver.find_element_by_class_name("inarticleline button").click()
        except common.exceptions.ElementClickInterceptedException as e:
            raise Exception(e, "\nPlease change the webpage or window size.")
            return
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
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)
        except common.exceptions.NoSuchElementException as e:
            raise Exception(e, "\nDue to non-running server.")
            return

        time.sleep(1)
        self.driver.find_element_by_xpath("//ul[@class = 'ul_mainstyle']//li[2]").click()
        time.sleep(1)
        items = self.driver.find_elements_by_xpath("//ul[@class = 'sideul']//li[not(@class)]")
        for _ in items[1:len(items) - 1]:
            self.driver.find_element_by_class_name("next").click()
            time.sleep(0.8)
        text2 = self.driver.find_element_by_class_name("congrats").text
        print(text2, "\nTest2 finished!")


    def testUser(self):

        for i in range(len(self.u)):
            user = User(username=self.u[i])
            user.set_password(password=self.p[i])
            self.assertFalse(user.check_password("111111"))
            self.assertTrue(user.check_password(self.p[i]))

        print("User password test is done!")

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
