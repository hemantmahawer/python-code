from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def screenshots(self):
        driver = webdriver.Chrome()
        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
        time.sleep(2)
        demo_element = driver.execute_script("return document.getElementsByClassName('dynamic-link')[5];")
        driver.execute_script("arguments[0].click();", demo_element)


obj1 = Screenshot()
obj1.screenshots()