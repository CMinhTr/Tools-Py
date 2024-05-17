from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
import undetected_chromedriver as uc
import sys,os
sys.path.insert(0,r'C:\Users\Admin\Desktop\HCVIP - 3\Tools Py')
from thuvien.thuvien import *

ExcelApp = ExcelApp()
import time
CoKetQua ='C'

def createWallet(driver,For1,MNEMONIC_12KEY):

    Timeint = time.time(); TimeOut= 90;Error = 0
    while time.time() < Timeint + TimeOut:
            
        current = driver.current_window_handle
        driver.switch_to.window(current)

        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if handle != current:
                driver.close()

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock')
        try:
            print('Nhập mật khẩu')
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div/div/input")))
            element.send_keys('Hungcuong@6789')
            element.send_keys(Keys.ENTER)
            time.sleep(3)
            driver.find_element(By.XPATH,'//*[@class="app-header__metafox-logo--horizontal"]')
            print("Đăng nhập thành công")
            break
        except: 
            print('Error Nhập mật khẩu')
            
    else:
        ExcelApp.write_excel(f'{CoKetQua}{For1}','Import Không Thành Công')
        print('Import Không Thành Công')
        driver.quit()
               

if __name__ == "__main__":

    for For1 in range(1,101):
        if ExcelApp.read_excel(f'{CoKetQua}{For1}') is not None: continue
        TEN_PROFILE = ExcelApp.read_excel(f'B{For1}'); print(f'- STT{For1} NGƯỜI DÙNG: ',TEN_PROFILE)
        PATH_PROFILE = r'C:\Users\Admin\AppData\Local\Google\Chrome\User Data'
        #PATH_PROFILE = ExcelApp.read_excel(f'A{For1}'); print(f'- STT{For1} PATH_PROFILE: ',PATH_PROFILE)
        # EMAIL = ExcelApp.read_excel(f'F{For1}'); print(EMAIL)
        # PASSWORD_EMAIL = ExcelApp.read_excel(f'G{For1}'); print(PASSWORD_EMAIL)
        # EMAIL_RECOVERY = ExcelApp.read_excel(f'H{For1}'); print(EMAIL_RECOVERY)
        MNEMONIC_12KEY = ExcelApp.read_excel(f'J{For1}'); print(f'- STT{For1} MNEMONIC_12KEY: ',MNEMONIC_12KEY)

        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        #options.add_argument('--start-maximized')
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-features=PrivacySandboxSettings4')
        options.add_argument(f"--user-data-dir={PATH_PROFILE}")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1000,1047)
        driver.set_window_position(-7,0)
        time.sleep(2)
        extension_link = dict()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.title != '':
                extension_link[f'{driver.title}'] = driver.current_url
        createWallet(driver,For1,MNEMONIC_12KEY)
        driver.get('https://pioneer.particle.network/en/point')

        Timeint = time.time(); TimeOut= 30
        while time.time() < Timeint + TimeOut:
            try:
                driver.find_element(By.XPATH,'//*[text()="Check-in"]').click()
                print('CHECK-IN OK')
            except:
                time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//*[text()="Confirm"]').click()
                print('Confirm OK')
            except:
                time.sleep(0.5)
        else:
            print('Erro CHECK-IN')
        
        input('---')
