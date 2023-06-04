from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class demolinktext():
    def locate_by_link(self):
        driver = webdriver.Chrome()
        # driver.get("https://www.yatra.com/")

        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(3)
        # driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
        # driver.find_element(By.CLASS_NAME, "dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack").click()


        driver.find_element(By.TAG_NAME, 'login-input').send_keys("test@gmail.com")


        time.sleep(5)

demo = demolinktext()
demo.locate_by_link()
