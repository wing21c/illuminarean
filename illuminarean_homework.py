from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 자동 업데이트
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 입력 데이터
service_data = '''{
    "companyName": "일루미나리안",
    "ceoName": "김상철",
    "businessType": "개인",
    "scale": "51-100 명",
    "name": "백창현",   
    "email": "test@gmail.com",
    "mobile": "01012345678"
}'''

# 공통 함수
def find_element_by_xpath_and_input_data(xpath, input_text):
    print("find_element_by_xpath_and_input_data")
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    element.send_keys(input_text)
    time.sleep(1)

def find_element_by_xpath_and_select_item_with_js(item_text):
    print("find_element_by_xpath_and_select_item_with_js")
    option = driver.find_element(By.XPATH, '//*[text()="{}"]'.format(item_text))
    driver.execute_script("arguments[0].scrollIntoView();", option)
    option.click()
    time.sleep(1)

def find_element_by_xpath_and_click_button(xpath):
    print("find_element_by_xpath_and_click_button")
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

######################################### Start ############################################
# 웹페이지 해당 주소 이동
driver.maximize_window()
url = "https://illuminarean.com/"
driver.get(url)


# 현재 윈도우 핸들 저장
main_window_handle = driver.window_handles[0]


# 팝업 제거
try:

    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-1lby940.e1iwydzj0 > svg > path'))).click()

except Exception as error:
    print("NoSuchElementException")
    pass
 

try:
    # WORK 이동
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/header/div/div/div/div/nav/ul/li[2]/a/span'))).click()
    
    # GOODVIBE 이동
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div/div[3]/div/a'))).click()

    # 무료체험신청 이동
    new_window_handle = driver.window_handles[1]
    driver.switch_to.window(new_window_handle)

    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/button'))).click()
    
except Exception as error:

    print("NoSuchElementException")
    driver.quit();
   
# 서비스 이용 신청  
try:  
    dict = json.loads(service_data)

    find_element_by_xpath_and_input_data("//*[@id='companyName']", dict['companyName'])
    find_element_by_xpath_and_input_data("//*[@id='ceoName']", dict['ceoName'])

    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#businessType > div > div.react-select__value-container.react-select__value-container--has-value.css-1hwfws3'))).click() 
    find_element_by_xpath_and_select_item_with_js(dict['businessType'])
    
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#scale > div > div.react-select__value-container.react-select__value-container--has-value.css-1hwfws3'))).click() 
    find_element_by_xpath_and_select_item_with_js(dict['scale'])

    find_element_by_xpath_and_input_data("//*[@id='name']", dict['name'])
    find_element_by_xpath_and_input_data("//*[@id='email']", dict['email'])
    find_element_by_xpath_and_input_data("//*[@id='mobile']", dict['mobile'])


    # 검색 1개 입력
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div'))).click() 
    find_element_by_xpath_and_select_item_with_js("매니저")
    find_element_by_xpath_and_click_button('/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[2]/button[2]')
  

    # 리스트에서 마지막 항목 1개 클릭
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div'))).click()
    time.sleep(1)
    list = driver.find_elements(By.CLASS_NAME, 'css-1irt6ri.el0tj996')
    #################### For debug ####################
    # for index, button in enumerate(list):
    #     print(f'Button Element {index+1} : {button.text}\n')

    # print(f'List Length : {len(list)}')

    # last_duty = list[len(list)-1].text
    # print(f'last_duty : {last_duty}')
    ###################################################

    find_element_by_xpath_and_select_item_with_js(list[len(list)-1].text)
    find_element_by_xpath_and_click_button('/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[2]/button[2]')

    # 신청 취소 버튼 
    find_element_by_xpath_and_click_button('/html/body/div[6]/button/span')

    # 신청 취소 확인 버튼
    find_element_by_xpath_and_click_button('/html/body/div[8]/div/div/div/div/div/div/button[2]')


    # 현재 창 종료
    driver.close()
    driver.switch_to.window(main_window_handle)

except Exception as error:

    print("NoSuchElementException")
    driver.quit();        