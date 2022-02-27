from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/'
browser.get(url) # url로 이동

#가는날 선택 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)

#가는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button').click() #tr이 형, td가 열
#오는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button').click()

#목적지 입력창 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
#목적지입력
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys('cju')
time.sleep(1)
#리스트에서 제주행선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a').click()
#검색버튼 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 검색 완료 후 가장 상단에 있는 요소가 뜰때까지 기다리기
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]')))
#

print(elem.text)


# b = browser.find_elements_by_class_name('sc-dIsUp jEEywD num')
# print(b)
# 2.25 : //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button
# 2.26 : //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button
# 2.02 : //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/button