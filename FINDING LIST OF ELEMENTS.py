from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class demolinktext():
    def locate_by_link(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")

        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(3)
        lista = driver.find_elements(By.TAG_NAME,"a")
        print(len(lista))
        for i in lista:
            print(i.text)
        attr = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr)

        time.sleep(5)

demo = demolinktext()
demo.locate_by_link()
