from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """一个主页面定位器类，所有的页面定位器应该来自这里"""
    GO_BUTTON = (By.ID, 'su')

class SearchResultsPageLocators(object):
    """一个搜索结果定位器类，所有搜索结果定位器应该来自这里"""
    pass
