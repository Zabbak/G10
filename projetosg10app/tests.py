from django.test import TestCase
from selenium import webdriver
from faker import Faker
from django.test import LiveServerTestCase

import string
import random
import time
# Create your tests here.

class test_cad(LiveServerTestCase):
    def test_setUp(self):
        self.base_url = "http://localhost:8000"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        
    def test_login(self):
        time.sleep(3)
        self.driver.get(self.base_url)
        
        time.sleep(3)
    
        log = self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]').click()
        time.sleep(1)
        email = self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("admin@gmail.com")
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys("1234")
        time.sleep(3)
        submit = self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
        time.sleep(3)
        
    def test_cadadm(self):
        cad = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/a').click()
        cad1 = self.driver.find_element(By.XPATH, '/html/body/form/div/select').click()
        cad2 = self.driver.find_element(By.XPATH, '/html/body/form/div/select').click()
        
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
            
    
            

        
        
        