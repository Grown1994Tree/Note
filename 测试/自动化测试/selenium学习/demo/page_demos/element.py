# element.py

from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """初始化每个页面对象类的基本页类"""

    def __set__(self, obj, value):
        """用给定的值设置文本"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """从具体的对象里获取文本"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")
