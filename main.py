import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from mobile_driver_config import driver, wait, actions
from scroll_function import scroll_down_until_element_visible_top


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

    # 截圖
    # 1. 找出所有anchor的id
    anchor_id_element_list = driver.find_elements(By.XPATH, "//*[contains(@class, 'anchor')]//*[contains(@data-anchor-btn, 'blockname')]")
    anchor_id_list = [anchor_id_element.get_attribute('data-anchor-btn') for anchor_id_element in anchor_id_element_list]
    ok_anchor_id_list = list()
    for anchor_id in anchor_id_list:
        anchor_text = driver.find_element(By.XPATH, "//*[contains(@class, 'anchor')]//*[@data-anchor-btn='" + anchor_id + "']//p").text
        if anchor_text == '推薦卡片' or anchor_text == '熱門卡片':
            continue
        else:
            ok_anchor_id_list.append(anchor_id)

    for anchor_id in ok_anchor_id_list:
        print(anchor_id)
        driver.find_element(By.XPATH, "//*[contains(@class, 'anchor')]//*[@data-anchor-btn='" + anchor_id + "']").click()
        time.sleep(2)  # todo: wait
        # locator = (By.XPATH, "//*[contains(@class, 'anchor')]//*[@data-anchor-btn='" + anchor_id + "' and contains(@class, 'active')]")
        # wait.until(expected_conditions.presence_of_element_located(locator))
        # locator = (By.XPATH, "//section[@data-anchor-block='" + anchor_id + "']")
        # wait.until(expected_conditions.visibility_of_element_located(locator))
        # 將section移到畫面上方
        section_xpath = "//section[@data-anchor-block='" + anchor_id + "']"
        scroll_down_until_element_visible_top(section_xpath)
        actions.move_to_element(driver.find_element(By.XPATH, section_xpath)).drag_and_drop_by_offset(driver.find_element(By.XPATH, section_xpath), 0, -50).perform()
        time.sleep(1)
        # 如果底下有swiper，一個一個點
        swiper_element_list = driver.find_elements(By.XPATH, "//section[@data-anchor-block='" + anchor_id + "']//span[contains(@class, 'swiper-pagination-bullet')]")
        # 到最前面
        if len(swiper_element_list) > 0:
            for swiper_element in swiper_element_list:
                swiper_element.click()
                time.sleep(0.5)
                # 一張卡一張卡點擊
                print(driver.find_element(By.XPATH, section_xpath + "//*[@class='swiper-wrapper']//*[contains(@class, 'active')]//*[@class='cubre-m-compareCard__title']").text)
        # 2. 每個tab點了後，滑到最上面.
        # 3. 點每一個slide
        # 4. 確認當前title有沒有停發，如果有截圖
