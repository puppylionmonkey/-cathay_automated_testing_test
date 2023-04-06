from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from path_config import project_path

chromedriver_path = project_path + 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 執行完不要關閉
emulation = {"deviceName": "iPhone 6"}
options.add_experimental_option("mobileEmulation", emulation)
driver = webdriver.Chrome(chromedriver_path, options=options)
wait = WebDriverWait(driver, 3)
driver.implicitly_wait(5)
actions = ActionChains(driver)