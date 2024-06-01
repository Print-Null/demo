# -- coding: utf-8 --
from demo import Demo


class TestDemo:
    def setup(self):
        self.demo = Demo()

    def test_sales_volume(self):
        assert self.demo.sales_volume() is True

    def test_price_volume(self):
        assert self.demo.price_volume() is True

    def test_order_volume(self):
        assert self.demo.order_volume() is True

    def teardown(self):
        self.demo.quit()
