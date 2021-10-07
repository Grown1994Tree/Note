from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

brower = webdriver.Chrome('/homes/selenium/chromedriver')
brower.get('http://www.baidu.com')

try:
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



