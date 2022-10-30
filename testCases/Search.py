import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class Practice(unittest.TestCase):
    @classmethod
    def setUpClass(self):   # This function will run everytime when we run the test
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://practice.automationbro.com")

    def test_homePage(self):    # Shows page title and total number of links with their titles
        self.driver.get("https://practice.automationbro.com")
        print(self.driver.title)
        link = self.driver.find_elements("tag name", "a")
        for i in link:
            print(i.text)
        print (len(link), "total links on the page")

    def test_shopItemSearch(self):  # It will test if search command is working
        self.driver.get("https://practice.automationbro.com")
        self.driver.find_element("id", "menu-item-567").click()
        self.driver.find_element("id", "woocommerce-product-search-field-0").send_keys("watch")
        self.driver.find_element("xpath", "//button[@value='Search']").click()

    @classmethod
    def tearDownClass(self):    # This function will run after completing all the test
        self.driver.quit()
        print ("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Ammar/PycharmProjects/seleniumTest/Reports"))
