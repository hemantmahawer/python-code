import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class selection():
    def value_select(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=7010M000002IWwj&internal=true")
        dropdown = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdown)
        dd.select_by_index(3)
        time.sleep(5)
        dd.select_by_value("Sales_Manager_AP")
        time.sleep(5)
        dd.select_by_visible_text("CxO / General Manager")
        time.sleep(5)


test_obj = selection()
test_obj.value_select()