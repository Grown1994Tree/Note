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



