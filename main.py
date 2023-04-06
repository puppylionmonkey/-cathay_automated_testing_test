from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from mobile_driver_config import driver, wait


def test_for_cathay():
    # 進到網頁
    driver.get('https://www.cathaybk.com.tw/cathaybk/')
    popup_xpath = "//img[contains(@src, 'popup') and contains(@src, 'close')]"
    # 關閉彈出視窗
    if len(driver.find_elements(By.XPATH, popup_xpath)) > 0:
        driver.find_element(By.XPATH, popup_xpath).click()
    # 確認進到首頁(出現快速連結)
    locator = (By.XPATH, "//*[contains(@class, 'quickLink')]")
    wait.until(expected_conditions.visibility_of_element_located(locator))
    # 截圖
    driver.save_screenshot('homepage.jpg')

    # 點選左上角選單
    driver.find_element(By.XPATH, "//*[contains(@class, 'burger')]").click()
    # 點擊個人金融
    # driver.find_element(By.XPATH, "//*[contains(@class, 'channel')]//a[contains(text(), '個人金融')]").click()
    # 點擊產品介紹
    driver.find_element(By.XPATH, "//*[contains(@class, 'menu__item')]//*[text()='產品介紹']").click()
    # 點擊信用卡
    credit_card_menu_xpath = "//*[contains(@class, 'menuLinkList__item')]//*[text()='信用卡' and contains(@class, 'menuSortBtn')"
    driver.find_element(By.XPATH, credit_card_menu_xpath + " and not(contains(@class, 'mbOnly'))]").click()
    # 計算信用卡下面的項目數量
    credit_card_item_count = len(driver.find_elements(By.XPATH, credit_card_menu_xpath + " and contains(@class, 'mbOnly')]/parent::*//a"))
    print(credit_card_item_count)

    # 點擊卡片介紹
    driver.find_element(By.XPATH, credit_card_menu_xpath + " and contains(@class, 'mbOnly')]/parent::*//a[text()='卡片介紹']").click()
