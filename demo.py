# -- coding: utf-8 --
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as Ac

from ui.common.logger import log

"""

"""


class Demo(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://dev-squarelocal.codeless-universe.com")
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10, 2)

    def sales_volume(self):
        sales_locator = (By.CSS_SELECTOR, "[data-key=totalQuantity]")
        self.wait.until(ec.element_to_be_clickable(sales_locator))
        sales_element = self.driver.find_element(*sales_locator)
        Ac(self.driver).move_to_element(sales_element).click().perform()
        sleep(2)
        sale_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        sold_count_list = []
        for element in sale_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[1]").text
            sold_count_list.append(int(span_text))
        log.info(f"降序排列前的sold数量列表：{sold_count_list}")
        if sold_count_list == sorted(sold_count_list, reverse=True):
            log.info(f"sold数量的列表和降序排列后的列表一致，所以sold的数量是由高到底排序")
            return True
        else:
            log.info(f"sold数量的列表和降序排列后的列表不一致，所以sold的数量不是由高到底排序")
            return False

    def price_volume(self):
        price_locator = (By.CSS_SELECTOR, "[data-key=avgPrice]")
        self.wait.until(ec.element_to_be_clickable(price_locator))
        price_element = self.driver.find_element(*price_locator)
        Ac(self.driver).move_to_element(price_element).click().perform()
        sleep(2)
        price_ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        print(f"price element list: 长度 {len(price_ele_list)}")
        price_list = []
        for element in price_ele_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[2]").text.lstrip("$")
            price_list.append(int(float(span_text)))
        log.info(f"升序排列前的price列表：{price_list}")
        if price_list == sorted(price_list, reverse=False):
            log.info(f"price的列表和升序排列后的列表一致，所以price是由底到高排序")
            return True
        else:
            log.info(f"price的列表和升序排列后的列表不一致，所以price不是由底到高排序")
            return False

    def order_volume(self):
        order_locator = (By.CSS_SELECTOR, "[data-key=orderCount]")
        self.wait.until(ec.element_to_be_clickable(order_locator))
        order_element = self.driver.find_element(*order_locator)
        Ac(self.driver).move_to_element(order_element).click().perform()
        sleep(2)
        order_ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        order_list = []
        for element in order_ele_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[3]").text
            order_list.append(int(span_text))
        log.info(f"降序排列前的order数量列表：{order_list}")
        if order_list == sorted(order_list, reverse=True):
            log.info(f"order数量的列表和降序排列后的列表一致，所以order的数量是由高到底排序")
            return True
        else:
            log.info(f"order数量的列表和降序排列后的列表不一致，所以order的数量不是由高到底排序")
            return False

    def quit(self):
        self.driver.quit()
