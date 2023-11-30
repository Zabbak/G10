from django.test import TestCase
from selenium import webdriver
from faker import Faker
from django.test import LiveServerTestCase

import string
import random
import time
# Create your tests here.

class BaseTestCase(LiveServerTestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
        
class Test_Login(LiveServerTestCase):
        def test_login(self):
            self.driver.get(self.base_url)
    
            log = self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]').click()
            time.sleep(1)
            email = self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("admin@gmail.com")
            time.sleep(1)
            password = self.driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys("1234")
            time.sleep(1)
            submit = self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
            time.sleep(1)
            

            
class Test_alun(LiveServerTestCase):
    def test_login(self):
        self.driver.get(self.base_url)
        alunos = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/a').click()
        cont1 = self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[1]').click()
        esp1 =  self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[1]/option[2]').click()
        cont2 = self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[2]').click()
        esp2 = self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[2]/option[3]').click()
        cont3 = self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[3]').click()
        esp3 = self.driver.find_element(By.XPATH, '/html/body/div/div/div/select[3]/option[4]').click()
        home = self.driver.find_element(By.XPATH, '/html/body/nav/div/a/img').click()
            

class Test_admin(LiveServerTestCase):
    def test_admini(self):
        self.driver.get(self.base_url)
        administradores = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/a').click()
        home = self.driver.find_element(By.XPATH, '/html/body/nav/div/a/img').click()
        

class Test_profe(LiveServerTestCase):
    def test_prof(self):
        self.driver.get(self.base_url) 
        prof = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/a').click()
        b1 = self.driver.find_element(By.XPATH, '//*[@id="accordionExample"]/strong/div/h2/button').click()
        b2 = self.driver.find_element(By.XPATH, '//*[@id="accordionExample"]/strong/strong/div/h2/button').click()


class Test_Cadst(LiveServerTestCase):
    def test_cadadm(self):
        cad = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/a').click()
        cad1 = self.driver.find_element(By.XPATH, '/html/body/form/div/select').click()
        cad2 = self.driver.find_element(By.XPATH, '/html/body/form/div/select').click()
        home = self.driver.find_element(By.XPATH, '/html/body/nav/div/a/img').click()
        
        
        faker = Faker()
        for _ in range(5):
            username = ''.join(random.choice(string.ascii_letters) for _ in range(5))
            email = f"{username}@email.com"
            
            
            nome = self.driver.find_element(By.XPATH, '//*[@id="nome"]')
            nome.clear() 
            nome.send_keys(username)
            
            email_field = self.driver.find_element(By.XPATH, f'//*[@id="{email}"]')
            email_field.clear()
            email_field.send_keys(email)
            
            senha = self.driver.find_element(By.XPATH, '//*[@id="senha"]')
            senha.clear()
            senha.send_keys(username)
            
            submit = self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
