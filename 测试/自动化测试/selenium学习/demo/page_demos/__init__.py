import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """一个简单展示页面对象如何工作的类"""

    def setUp(self):
       # self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox(executable_path='/homes/selenium/geckodriver')
        self.driver.get("https://www.baidu.com/")

    def test_search_in_python_org(self):
        """
        测试 python.org网站的搜索功能。搜索一个单词“pycon”然后验证某些结果会展示出来。
        注意这个测试不会在搜索结果页里寻找任何细节文本，它只会验证结果为非空
        """

        #载入主页面，这个例子里是 Python.org的首页
        main_page = page.MainPage(self.driver)
        #检查页面的标题是否包含"python"单词
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #将搜索框的文本设置为"pycon"
        main_page.search_text_element = "百度"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #验证结果页非空
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

