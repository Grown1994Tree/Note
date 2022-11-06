# selenium

# selenium安装
1. 安装pip工具: `sudo apt-get install pip`
2. 安装指令：`pip install selenium`

### 一、第一个案例

```
    from selenium import webdriver

    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    assert "百度一下，你就知道" in brower.title
```
该案例主要分为三个步骤：
1. 从 `selenium` 模块 `webdriver` 对象。
2. 使用 `webdriver` 对象初始化谷歌浏览器的驱动。*<font size=2>针对不同的浏览器传递不同的浏览器驱动，下载网址：https://www.selenium.dev/downloads/</font>*
3. 打开百度网址
![avatar](/测试/自动化测试/selenium学习/第一个实例.png)
4. 通过断言确认是否访问正确

### 二、获取节点
获取节点的具体方法可以查看 `/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote` 目录，该目录涵盖了所有常用的方法。
```
    from selenium import webdriver

    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    search_input = brower.find_element_by_name("wd")
    search_input.send_keys("测试")
```
在selenium中，获取节点的方法分为三类
1. 通过 `id`、`class`、`name` 以及标签名获取节点。
   - 标签名    find_element_by_tag_name
   - `name`  find_element_by_name
   - `id` find_element_by_id
   ```
        brower.get('http://www.baidu.com')
        search_text = brower.find_element_by_id("m")
        print(search_text.text)
   ```

   - `class` find_element_by_class_name 和 find_elements_by_class_name *<font size=2>两个的差别只是在`find_element` 和 `find_elements`。其中，`find_element` 返回的是列表的第一个值，`find_elements`返回的是整个列表</font>*

   ```
        from selenium import webdriver
        from selenium.webdriver.support.ui import WebDriverWait
        import time

        brower = webdriver.Chrome('/homes/selenium/chromedriver')
        brower.get('http://www.baidu.com')

        time.sleep(10)

        search_list = brower.find_elements_by_class_name("title-content-title")

        search_item = brower.find_element_by_class_name("title-content-title")

        for item in search_list:
            print(item.text)

        print("---------------------------")
        print(search_item.text)
        print("---------------------------")

   ```
  ![avatar](/测试/自动化测试/selenium学习/by_class_name.png) 

2. css选择器
   - `find_elements_by_css_selector` 获取元素列表
   - `find_element_by_css_selector` 获取元素列表首位

   ```
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    try:
        wait = WebDriverWait(brower,10)
        wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,".s-bottom-layer-content > p.lh"))
        )
        search_list = brower.find_elements_by_css_selector(".s-bottom-layer-content >p.lh")
        search_item = brower.find_element_by_css_selector(".s-bottom-layer-content > p.lh")

        for item in search_list:
            print(item.text)

        print("---------------------------")
        print(search_item.text)
        print("---------------------------")

    finally:
        print("接受")
   ```
   ![avatar](/测试/自动化测试/selenium学习/by_css_selector.png) 
   *<font size=2>该选择器获取的内容都跟元素选择器一致</font>*

3. 链接文本选择器

  - `find_elements_by_partial_link_text` 和 `find_elements_by_link_text` 两个方法是获取链接a标签的文本值。
  其中，`find_elements_by_link_text`是完全匹配。

```
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    try:

        search_list = brower.find_elements_by_link_text("贴吧")
        search_list1 = brower.find_elements_by_partial_link_text("贴")

        for search_item in search_list1:
            print(search_item.text)


        for search_item in search_list:
            print(search_item.text)

    finally:
        print("接受")

```
![avatar](/测试/自动化测试/selenium学习/by_href_text.png) 

### 四、通过xpath获取节点
- 核心语法：`find_element_by_xpath`
- `xpath` 核心语法
    - `//*` 获取任意一个节点
    - `/` 获取直接子节点
    - `[]` 用来进行筛选，通常为数字和属性 *<font size=2>使用属性的格式为“[@属性=属性值]”</font>*
    - `.` 在某个元素里面使用xpath需要在最前面加上`.`
 - 通常使用 `xpath` 路径时，采用相对路径方法。
 
```
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    try:
        wait = WebDriverWait(brower,10)
        wait.until(
                EC.presence_of_element_located((By.ID,"s-top-left"))
        )

        print("相对于根元素获取")

        links = brower.find_elements_by_xpath("//div[@id='s-top-left']/a")

        for link_item in links:
            print(link_item.text)

        print("相对于子元素获取")

        parent_item = brower.find_element_by_id("s-top-left")

        link_list = parent_item.find_elements_by_xpath("./a")

        for link_item in link_list:
            print(link_item.text)


    finally:
        print("接受")
```

![avatar](/测试/自动化测试/selenium学习/by_xpath.png)


### 三、事件等待
    在执行过程中，可能出现测试脚本已经运行完成，但是网页还未加载完成的情况，特别是ajax使用非常频繁的环境更加容易遇到。因此，我们需要等待到网页加载完或者所需的节点加载完才继续执行代码。
    处理该问题的方法分为两种类型，显式等待和隐式等待
1. 显示等待（推进）
   - 定义：在测试脚本要满足一定的条件才进行深一步执行，通常是等待一定的时间。
   - 第二节的 `time.sleep(10)` 就是显示等待的方式之一
   - 需要通过 `WebDriverWait` 配合预期条件 `EC` 模块来判断条件是否达到，如果条件达到则继续执行下一步 *<font size=2>需要引入`from selenium.webdriver.support.ui import WebDriverWait ` 和 `from selenium.webdriver.support import expected_conditions as EC`</font>*

   ```
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        brower = webdriver.Chrome('/homes/selenium/chromedriver')
        brower.get('http://www.baidu.com')

        try:

            WebDriverWait(brower,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"title-content-title"))
            )
            search_list = brower.find_elements_by_class_name("title-content-title")

            search_item = brower.find_element_by_class_name("title-content-title")

            for item in search_list:
                print(item.text)

            print("---------------------------")
            print(search_item.text)
            print("---------------------------")

        finally:
            brower.quit()
   ```
     - 通过引入by模块来对元素进行定位 `from selenium.webdriver.common.by import By`
     对元素定位的方法：
     ```
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
     ```
     - `WebDriverWait(brower,10).until()` 等待10秒后，判断条件是否达成，如果达成才执行下一步。
     - 预期条件类型
     ```
        title_is
        title_contains
        presence_of_element_located
        visibility_of_element_located
        visibility_of
        presence_of_all_elements_located
        text_to_be_present_in_element
        text_to_be_present_in_element_value
        frame_to_be_available_and_switch_to_it
        invisibility_of_element_located
        element_to_be_clickable - 元素展示并且可用
        staleness_of
        element_to_be_selected
        element_located_to_be_selected
        element_selection_state_to_be
        element_located_selection_state_to_be
        alert_is_present
     ```

2. 隐式等待
   - 定义：程序每经过一定的时间就对DOM节点进行定位
   - 使用方法：使用`implicitly_wait`方法
   ```
    from selenium import webdriver
    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.implicitly_wait(10)
    brower.get('http://www.baidu.com')

    try:

        search_list = brower.find_elements_by_class_name("title-content-title")

        search_item = brower.find_element_by_class_name("title-content-title")

        for item in search_list:
            print(item.text)

        print("---------------------------")
        print(search_item.text)
        print("---------------------------")

    finally:
        brower.quit()

   ```

### 四、元素操作
1. 元素事件。元素所拥有的方法见`usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webelement.py` 文件。
```
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    brower = webdriver.Chrome('/homes/selenium/chromedriver')
    brower.get('http://www.baidu.com')

    try:
        wait = WebDriverWait(brower,10)
        wait.until(
                EC.presence_of_element_located((By.ID,"s-top-left"))
        )

        parent_item = brower.find_element_by_id("s-top-left")

        link_list = parent_item.find_elements_by_xpath("./a")

        for link_item in link_list:
            link_item.click()

    finally:
        print("接受")

```

![avatar](/测试/自动化测试/selenium学习/click_events.png)
*<font size=2>该案例只展示点击事件</font>*

2. 行为链
- 需要引入行为链模块。
    - `from selenium.webdriver.common.action_chains import ActionChains`
    - 该模块支持的方法可以在 `usr/local/lib/python3.8/dist-packages/selenium/webdriver/common/action_chains.py` 文件下查看。
    - 在行为链的操作中，会出现加载延迟，所以需要暂停程序的运行。

    ```
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.action_chains import ActionChains
        from time import sleep

        brower = webdriver.Chrome('/homes/selenium/chromedriver')
        brower.get('http://www.baidu.com')

        try:ll
            wait = WebDriverWait(brower,10)
            wait.until(
                    EC.presence_of_element_located((By.ID,"s_side_wrapper"))
            )
            brower.maximize_window()
            # //*[@id="video-meeting"]/div/div/div[2]/button[2]
            video_meet = brower.find_element_by_class_name("video-meet-entry")
            sleep(4)
            actions = ActionChains(brower)
            actions.move_to_element(video_meet)
            actions.click(video_meet)
            actions.perform()
            sleep(4)
            sleep(4)
            actions1 = ActionChains(brower)
            enter_meet = brower.find_element_by_xpath('//*[@id="video-meeting"]/div/div/div[2]/button[2]')

            actions1.click(enter_meet)
            actions1.perform()
            sleep(4)

        finally:
            print("接受")
      
    ```


### 五、页面对象
1. 目的：
    - 提高测试代码的可重用性
    - 提高测试框架的稳定性
    - 提高测试代码的可读性

2. 方式：把测试页面和测试元素封装成对象从业务中区分出来，更加专注于业务上的测试。

3. 实例：测试打开百度首页面并进行查询
- 创建初始化入口`__init__.py`
    - 该模块为运行入口模块，可以直接使用 `python3 __init__.py` 运行;如果该模块被其他模块引用，则无法调用 `unittest.main() ` 方法
    - `PythonOrgSearch` 类主要包含基本的操作，包括加载驱动`setUp`、测试任务`test_search_in_python_org` 以及关闭测试任务 `tearDown`
    - 方法`test_search_in_python_org` 为测试的主要部分，在加载驱动`setUp` 和关闭闭测试任务 `tearDown` 之间可以添加任意测试任务
```
    # __init__.py

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

```

- 创建页面对象的基本页类
    - 该类包含各种方法来对元素进行技术上的定位，实现对元素的监控、获取属性、获取值以及基本操作*<font size=2>业务部分直接继承该部分，并进行操作</font>*
    - 在对元素的操作之前，先通过`lambda`匿名函数来判断对应的元素是否加载完毕 
```
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
                                           
```

- 创建业务模块类
   - 在 `page.py` 模块中，包含该测试任务中的各个子任务；包含对元素进行业务上的定位，从而进行操作。
   - 在 `MainPage` 和 `SearchResultsPage` 方法里面实现测试任务的具体操作,通过这两个方法可以实现对页面的测试。

```
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

```