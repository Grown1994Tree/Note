from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


brower = webdriver.Chrome('/homes/selenium/chromedriver')
brower.get('http://www.baidu.com')

try:
  
    search_list = brower.find_elements_by_link_text("吧")
    search_list1 = brower.find_elements_by_partial_link_text("贴")
   
    for search_item in search_list1:
        print(search_item.text)


    for search_item in search_list:
        print(search_item.text)

finally:
    print("接受")



