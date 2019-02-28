from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'https://www.aminer.cn/profile/frederick-brooks/53f432dadabfaee0d9b416d5'
browser.get(url)
time.sleep(10)
print(browser.page_source)
print('----------华丽的分割线----------')
#coworkers = browser.find_element_by_class_name('network_node')
#print(coworkers)
time.sleep(10)
browser.close()

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# print(input_first)
# print('----------华丽的分割线----------')
# print(browser.page_source)
# time.sleep(2)
# browser.close()