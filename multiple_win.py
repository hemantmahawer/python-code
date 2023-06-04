from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class multi_win():
    def multi_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_path = driver.window_handles
        print(parent_path)
        driver.find_element(By.XPATH, "//a[@title='Free Cancellation']//img[@class='conta iner large-banner']").click()
        time.sleep(5)

        all_win = driver.window_handles
        for handle in all_win:
            if handle != parent_path:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").send_keys('New Delhi')
                time.sleep(2)
                driver.close()
                time.sleep(2)
                break
                time.sleep(2)
        print(driver.window_handles)

        driver.switch_to.window(parent_path)
        driver.find_element(By.XPATH, "//a[@title='Offers']").click()
        time.sleep(5)




obj1 = multi_win()
obj1.multi_windows()