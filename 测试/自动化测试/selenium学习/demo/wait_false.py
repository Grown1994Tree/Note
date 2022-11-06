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
    



