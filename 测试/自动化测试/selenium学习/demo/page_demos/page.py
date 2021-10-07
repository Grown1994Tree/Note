# page.py

from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """这个类从指定的定位器里获取到搜索文本"""

    #已经输入搜索字符串的搜索框的定位器
    locator = '//*[@id="kw"]'


class BasePage(object):
    """初始化所有页面都会调用的基本页类"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """主页操作方法放这里"""

    #定义一个变量存放检索文本
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """验证硬编码字符"python"出现在页面标题里"""
        return "百度" in self.driver.title

    def click_go_button(self):
        """触发搜索功能"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """搜索结果页操作方法放这里"""

    def is_results_found(self):
        # 或许应该在具体的页面元素里搜索文本，不过目前为止这样运行没什么问题
        return "No results found." not in self.driver.page_source
