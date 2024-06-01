# -- coding: utf-8 --
from demo import Demo


class TestDemo:
    def setup(self):
        self.demo = Demo()

    # 测试 sales 列是否按照 sold 数量降序排序，断言 sales_volume()返回True则表示降序排序，否则断言失败，测试报错
    def test_sales_volume(self):
        assert self.demo.sales_volume() is True

    # 测试 price 列是否按照 avg price 数量升序排序，断言 price_volume()返回True则表示升序排序，否则断言失败，测试报错
    def test_price_volume(self):
        assert self.demo.price_volume() is True

    # 测试 sales 列是否按照 order 数量降序排序，断言 order_volume()返回True则表示降序排序，否则断言失败，测试报错
    def test_order_volume(self):
        assert self.demo.order_volume() is True

    def teardown(self):
        self.demo.quit()
