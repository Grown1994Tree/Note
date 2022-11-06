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
#    brower.quit()


