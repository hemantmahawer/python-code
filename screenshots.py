from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def screenshots(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        demo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        demo.screenshot(".\\screenshot\\test1.pgn")
        demo.click()
        time.sleep(5)
        # demo.save_screenshot(".\\screenshot\\test2.png")
        # time.sleep(5)
        # demo.get_screenshot_as_file(".\\screenshot\\test3.jpg")
        driver.get_screenshot_as_file(".\\screenshot\\test2.png")
        driver.save_screenshot(".\\screenshot\\test3.jpg")

obj1 = Screenshot()
obj1.screenshots()
