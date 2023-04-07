from selenium.webdriver.common.by import By

from mobile_driver_config import driver


def click_burger_button():
    driver.find_element(By.XPATH, "//*[contains(@class, 'burger')]").click()


def click_menu_item_button(item):
    driver.find_element(By.XPATH, "//*[contains(@class, 'menu__item')]//*[text()='" + item + "']").click()


def click_menu_linklist_item_button(menu_linklist_item):
    menu_linklist_item_xpath = "//*[contains(@class, 'menuLinkList__item')]//*[text()='" + menu_linklist_item + "' and contains(@class, 'menuSortBtn')"
    driver.find_element(By.XPATH, menu_linklist_item_xpath + " and not(contains(@class, 'mbOnly'))]").click()