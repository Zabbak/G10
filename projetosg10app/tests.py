from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class app_health(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        
    def test_load_home_page(self):
        driver = self.driver

        driver.get(self.base_url)
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("Início", driver.title)
        image_element = driver.find_element_by_css_selector('img[src*="]')
        self.assertTrue(image_element.is_displayed(), "A imagem não está sendo exibida na página")
        