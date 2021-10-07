from selenium import webdriver

brower = webdriver.Chrome('/homes/selenium/chromedriver')
brower.get('http://www.baidu.com')

search_text = brower.find_element_by_id("m")

print(search_text.text)


