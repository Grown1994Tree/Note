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

