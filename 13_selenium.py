from selenium import webdriver

browser = webdriver.Chrome()

#네이버로 이동
browser.get('https://www.naver.com/')

# 로그인버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

#id와 pw 입력
elem = browser.find_element_by_id('id').send_keys('xxx')
elem = browser.find_element_by_id('pw').send_keys('xxx')

#로그인버튼 클릭
browser.find_element_by_id('log.login').click()

#기입력된 id 지우기
elem = browser.find_element_by_id('pw').clear()

#html 정보 출력
print(browser.page_source)

