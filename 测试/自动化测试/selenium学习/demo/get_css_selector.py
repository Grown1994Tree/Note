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
    search_list = brower.find_elements_by_css_selector(".s-bottom-layer-content > p.lh")
    search_item = brower.find_element_by_css_selector(".s-bottom-layer-content > p.lh")
        
    for item in search_list:
        print(item.text)

    print("---------------------------")
    print(search_item.text)
    print("---------------------------")

finally:
    print("接受")
#    brower.quit()


