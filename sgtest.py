from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://sogang.ac.kr/bachelor/students/notice/notice08.html')
time.sleep(1)
pop_up = browser.find_elements_by_tag_name('iframe')
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrm"]'))
time.sleep(1)
a = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[5]')
print(a)
#접근까진 성공 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ


# //*[@id="mainFrm"]
# a = browser.find_elements_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[2]')
# soup = BeautifulSoup(pop_up, 'html.parser')




# # iframe 안으로 이동하기
# ## 몇 번째 iframe인지 확인 후, 그에 맞게 넣어주셔야해요. 저는 첫 번째 iframe에 들어가고 싶어 0을 넣어줬습니다!
# pop_up = driver.find_elements_by_tag_name('iframe')[0]
# driver.switch_to.frame(pop_up)