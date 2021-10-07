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
    



