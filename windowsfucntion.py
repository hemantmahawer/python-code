import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class testwindowsfunc():
    def win_func(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(2)
        driver.quit()


obj1 = testwindowsfunc()
obj1.win_func()