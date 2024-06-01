# -- coding: utf-8 --
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as Ac

"""
1）在Sales volume这一页，所有的数据应该按 xxxx sold in the past month，从高到低的排序。
测试方法：将 xxxx 的数据取出来依次添加到一个列表 A，然后将A列表进行降序排序得到列表B，如果列表A == 列表B，那么就说明列表A是从高到底排序
2) 在Price 这一页，所有数据应该按average price $xxxx，从低到高的排序
测试方法：将 $xxxx 的数据取出来去掉$后依次添加到一个列表 A，然后将A列表进行升序排序得到列表B，如果列表A == 列表B，那么就说明列表A是从底到高排序
3）在Order 这一页，所有数据应该按 x orders, 从高到低排序。
测试方法：将 x 的数据取出来依次添加到一个列表 A，然后将A列表进行降序排序得到列表B，如果列表A == 列表B，那么就说明列表A是从高到底排序

右上角的Join Ranking, 是通过square登录，如果要求你测试登录的话，你会怎么做？
测试方法：通过UI自动化的手段进行测试的话依次进行以下操作：
1.点击 Join Ranking 按钮
2.点击后会有页面跳转，使用 self.driver.current_url 可以得到跳转后页面的url，可以根据这个url判断是否跳转成功
3.点击后会有页面跳转，如果跳转成功应该会有和 square 登录相关的用户名和密码输入框，可以定位用户名和密码输入框的页面元素，然后通过
element.is_enabled或者element.is_displayed来判断跳转后的页面上是否存在 square 的用户名和密码输入框，这样也可以判断是否跳转到square的登录页面
我看给定的demo网址现在跳转后是一个error页面，所以具体的代码没有写，这里只写出一个测试的思路
"""


class Demo(object):
    def __init__(self):
        """
        初始化chrome driver
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        if sys.platform.startswith("Linux".lower()):
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://dev-squarelocal.codeless-universe.com")
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10, 2)

    def sales_volume(self):
        """
        判断 Sales volume这一列是否按照 xxxx sold数量降序排列
        :return: 如果是降序排列返回 True,否则返回 False
        """
        sales_locator = (By.CSS_SELECTOR, "[data-key=totalQuantity]")
        self.wait.until(ec.element_to_be_clickable(sales_locator))
        sales_element = self.driver.find_element(*sales_locator)
        sales_element.is_enabled()
        Ac(self.driver).move_to_element(sales_element).click().perform()
        sleep(2)
        sale_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        sold_count_list = []
        # 依次将取到的 xxxx sold数量添加到一个列表中
        for element in sale_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[1]").text
            sold_count_list.append(int(span_text))
        print(f"降序排列前的sold数量列表：{sold_count_list}")
        if sold_count_list == sorted(sold_count_list, reverse=True):
            print(f"sold数量的列表和降序排列后的列表一致，所以sold的数量是由高到底排序")
            return True
        else:
            print(f"sold数量的列表和降序排列后的列表不一致，所以sold的数量不是由高到底排序")
            return False

    def price_volume(self):
        """
        判断 price 这一列是否按照 average price $xxxx数量升序排列
        :return: 如果是升序排列返回 True,否则返回 False
        """
        price_locator = (By.CSS_SELECTOR, "[data-key=avgPrice]")
        self.wait.until(ec.element_to_be_clickable(price_locator))
        price_element = self.driver.find_element(*price_locator)
        Ac(self.driver).move_to_element(price_element).click().perform()
        sleep(2)
        price_ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        price_list = []
        # 依次将取到的 average price $xxxx 数量去掉$后添加到一个列表中
        for element in price_ele_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[2]").text.lstrip("$")
            price_list.append(round(float(span_text), 2))
        print(f"升序排列前的price列表：{price_list}")
        if price_list == sorted(price_list, reverse=False):
            print(f"price的列表和升序排列后的列表一致，所以price是由底到高排序")
            return True
        else:
            print(f"price的列表和升序排列后的列表不一致，所以price不是由底到高排序")
            return False

    def order_volume(self):
        """
        判断 order 这一列是否按照 x orders 数量降序排列
        :return: 如果是降序排列返回 True,否则返回 False
        """
        order_locator = (By.CSS_SELECTOR, "[data-key=orderCount]")
        self.wait.until(ec.element_to_be_clickable(order_locator))
        order_element = self.driver.find_element(*order_locator)
        Ac(self.driver).move_to_element(order_element).click().perform()
        sleep(2)
        order_ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".mt-2>div")
        order_list = []
        # 依次将取到的 x orders 数量添加到一个列表中
        for element in order_ele_list:
            span_text = element.find_element(By.TAG_NAME, "h5").find_element(By.XPATH, "./*[3]").text
            order_list.append(int(span_text))
        print(f"降序排列前的order数量列表：{order_list}")
        if order_list == sorted(order_list, reverse=True):
            print(f"order数量的列表和降序排列后的列表一致，所以order的数量是由高到底排序")
            return True
        else:
            print(f"order数量的列表和降序排列后的列表不一致，所以order的数量不是由高到底排序")
            return False

    def quit(self):
        self.driver.quit()
