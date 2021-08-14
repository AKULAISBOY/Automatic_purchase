

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time 
import random

AMAZON_URL = 'https://www.amazon.com/MAXSUN-GEFORCE-GT-1030-Graphics/dp/B08RD5VMNN'
AMAZON_TEST_URL = 'https://www.amazon.com/ZOTAC-GeForce-Graphics-IceStorm-ZT-A30600H-10M/dp/B08W8DGK3X'
WAIT_TIME = 3
PRICE_LIMIT = 550.00

class AKULA :
    def __init__(self, username, password):
        """ Initializes Bot with class-wide variables. """
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('D:/Code/BOT/chromedriver.exe') ## ВАШ ПУТЬ ДО webdriver.Chrome
    
    ## Sign into site with the product
    def signIn(self):
        """ Sign into site with the product. """
        driver = self.driver ## Navigate to URL
        
        ## Enter Username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        username_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## Enter Password
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        password_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
    ## Найдите товар в разделе X количество
    def findProduct(self):
        """ Находит продукт по глобальной ссылке. """
        driver = self.driver
        driver.get(AMAZON_TEST_URL)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## Если продукт недоступен, подождите, пока он будет доступен
        isAvailable = self.isProductAvailable()
        
        if isAvailable == 'Currently unavailable.':
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
        elif isAvailable <= PRICE_LIMIT:
            ## Buy Now
            buy_now = driver.find_element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.signIn()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
            ## Place Order
            place_order = driver.find_element_by_name('placeYourOrder1').text
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            print(f'***** РАЗМЕСТИТЬ ЗАКАЗ: {place_order}')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            ## place_order.click()
            ## time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
        else:
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
            
    def isProductAvailable(self):
        """ Проверяет, доступен ли продукт. """
        driver = self.driver
        available = driver.find_element_by_class_name('a-color-price').text
        #if available == 'Currently unavailable.':
         #   print(f'***** AVAILABLE: {available}')
         #   return available
        #else:
        #    print(f'***** PRICE: {available}')
        #    return float(available[1:])## $123.22 -> 123.22




        if available == 'Currently unavailable.':
           print(f'***** AVAILABLE: {available}')
           return available
       
        while True:
                   available != 'Currently unavailable.'
                   print(f'***** AVAILABLE: {available}') #ДОСТУПНА
                   print('карточки ZOTAC Gaming GeForce RTX 3060 нет') 
                   driver.get(AMAZON_TEST_URL)
                   time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))   
                   
        else:
           
           print(f'***** PRICE: {available}')
           return float(available[1:]) ## $123.22 -> 123.22    
        
           
            



    
    def closeBrowser(self):
        """ Closes browser """
        self.driver.close()
        

if __name__ == '__main__':
    shopBot = AKULA (username="MAIL", password="Password")
    shopBot.findProduct()
    shopBot.closeBrowser()
            


