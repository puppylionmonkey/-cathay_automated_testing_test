import time
from selenium.webdriver.common.by import By

from mobile_driver_config import actions, driver


def focus_element_by_click(element_xpath):
    actions.move_to_element(driver.find_element(By.XPATH, element_xpath)).click().perform()
    time.sleep(1)


def scroll_down_until_element_visible(element_xpath):  # 前台
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, element_xpath))
    time.sleep(1)


def scroll_down_until_element_visible_top(element_xpath):  # 前台 true: 頂端對齊
    driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, element_xpath))
    time.sleep(1)


def scroll_down_until_element_visible_bottom(element_xpath):  # 前台 false: 底端對底端
    driver.execute_script("return arguments[0].scrollIntoView(false);", driver.find_element(By.XPATH, element_xpath))
    time.sleep(1)