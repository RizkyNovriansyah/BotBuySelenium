 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import os
# from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install())
link = ""
driver.get(link)

# time.sleep(delay_default)

done = input('Already Login?')

delay_default = 2

passed = False
warning_gagal = None
while not passed:
    print("Klik beli")
    try:
        button_beli = driver.find_elements_by_class_name('YtgjXY')
        button_beli[1].click()
        btn_found = True
    except:
        btn_found = False
        print("Button not found")
        driver.refresh()
    
    try:
        
        warning_gagal = driver.find_element_by_class_name('QiI0pP')
        print("Warning. Refresh")
        driver.refresh()
    except:
        print("Not found Warning")
        if btn_found:
            passed = True
        
    time.sleep(delay_default)
    
    # try:
        
        
    # except:
    #     print("Restart")
    #     time.sleep(delay_default)
    #     passed = False
    
# time.sleep(delay_default)
passed = False
warning_gagal = None
delay_default = 1
while not passed:
    print("Klik checkout")
    try:
        button_beli = driver.find_element_by_class_name('shopee-button-solid')
        button_beli.click()
        passed = True
    except:
        pass
    time.sleep(delay_default)
    
passed = False
warning_gagal = None
while not passed:
    print("Klik bank")
    try:
        button_beli = driver.find_elements_by_class_name('product-variation')
        button_beli[1].click()
        passed = True
    except:
        pass
    time.sleep(delay_default)
    
    
passed = False
warning_gagal = None
while not passed:
    print("Klik bank")
    try:
        button_beli = driver.find_elements_by_class_name('stardust-radio-button__outer-circle')
        button_beli[0].click()
        passed = True
    except:
        pass
    time.sleep(delay_default)

passed = False
while not passed:
    print("Klik ubah")
    try:
        button_beli = driver.find_element_by_class_name('_3f0IkJ')
        button_beli.click()
        passed = True
    except:
        pass
    
time.sleep(delay_default)
print("Klik same day")
button_beli = driver.find_elements_by_class_name('_3VyxJj')
button_beli[0].click()
time.sleep(delay_default)
print("Klik same day")
button_beli = driver.find_elements_by_class_name('logistics-selection-modal__content')
button_beli[0].click()
time.sleep(delay_default)
print("Klik saran waktu dirumah")
button_beli = driver.find_elements_by_class_name('_2t4H9g')
button_beli[0].click()
time.sleep(delay_default)

print("klik ok")
# stardust-button stardust-button--primary logistics-selection-modal__submit-btn
button_beli = driver.find_element_by_class_name('logistics-selection-modal__submit-btn')
button_beli.click()
time.sleep(delay_default)

passed = False
warning_gagal = None
while not passed:
    print("Klik buat pesanan")
    try:
        # stardust-button stardust-button--primary stardust-button--large _22Ktrb _1pnpSr
        button_beli = driver.find_element_by_class_name('stardust-button--primary')
        button_beli.click()
        # print("Clicked")
        passed = True
    except:
        pass
    time.sleep(delay_default)

done = input('Berhasil?')