import sys
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome import options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# ---------------------------------------------------------------------------
empId = '●●●●●●●●●'
phoneNum = '●●●●●●●●●●'
# ---------------------------------------------------------------------------
# Options設定，建立 webdriver 時呼叫使用
# stupid wits network , use headless need VPN (。___ 。 )
op = webdriver.ChromeOptions()
# op.add_argument('--headless')
op.add_argument('--disable-gpu')
op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors')
# 無視 log 輸出 (主要是windows系統usb相關控制權)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
# 視窗最大化
op.add_argument("--start-maximized")

# 開啟瀏覽器(Chrome)
browser = webdriver.Chrome("./chromedriver.exe", options=op)
# 瀏覽器顯示時的座標
# browser.set_window_position(-10000,0)
# 瀏覽器畫面大小
#browser.set_window_size(1200, 800)

browser.get('https://wits-healthy.wistronits.com/healthy-tp/login')
# 找&填 員工編號跟手機號碼
id = browser.find_element_by_name("employeeId")
id.send_keys(empId)
phone = browser.find_element_by_name("mobileNo")
phone.send_keys(phoneNum)
phone.submit()

# 找體溫 radiobutton 點過沒
if browser.find_element_by_id('temperatureType1').is_selected() is False:
    browser.find_element_by_id('temperatureType1').click()
    tmp = browser.find_element_by_name('temperature')
    tmp.clear()
    input_tmp = random.uniform(36.1 , 36.6)
    tmp.send_keys( str( round(input_tmp, 1) ) )

# 畫面以滾輪方式移到最下面
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# 給他一點時間滾
time.sleep(1)

# 找無症狀 checkbox 點過沒
nothing = browser.find_element_by_xpath('//*[@id="symptomList0"]').is_selected()
if nothing is False :
    print('I\'m fine.   <--- let\'s check !!')
    nothing_check = browser.find_element_by_xpath('//*[@id="symptomList0"]')
    nothing_check.click()

    # 送出
    submit = browser.find_element_by_xpath('//*[@id="mainForm"]/div/div[16]/div/button')
    submit.submit()

    # chrome 掰
    browser.quit()
    print('bye')
    # python 掰
    sys.exit()
else:
    print('already sent , bye')
    time.sleep(3)
    # chrome 掰
    browser.quit()
    print('bye')
    # python 掰
    sys.exit()