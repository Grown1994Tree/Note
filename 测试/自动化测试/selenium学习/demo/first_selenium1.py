from selenium import webdriver

brower = webdriver.Chrome('/homes/selenium/chromedriver')
brower.get('http://www.baidu.com')

search_input = brower.find_element_by_name("wd")

search_input.send_keys("测试")


