from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Library import ExcelApp
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

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')

        try:
            print("Đồng ý điều khoản Metamask...")
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input")))
            time.sleep(3)
            driver.execute_script("arguments[0].click();", element)
        except: 
            driver.quit()
            print('Error "Check Đồng Ý Điều Khoản"')
            
        try:
            print("Import Ví Hiện Có...")
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
            time.sleep(3)
        except: 
            driver.quit()
            print('Error "Import Mnemonic"')
            

        try:
            print("Hãy giúp chúng tôi cải thiện MetaMask...")
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]')))
            element.click()
            time.sleep(3)  
        except: 
            driver.quit()
            print('Error "Chọn I agree"')
            

        try:
            print('Đang nhập MNEMONIC...')
            xpaths = [
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[3]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[4]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[5]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[6]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[7]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[8]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[9]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[10]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[11]/div[1]/div/input",
                "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[12]/div[1]/div/input"
            ]
            for xpath, char in zip(xpaths, MNEMONIC_12KEY.split()):
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
                element.send_keys(char)
                time.sleep(0.1)
            time.sleep(3)  
        except: 
            driver.quit()
            print('Error "Nhập MNEMONIC"')
            

        try:
            print('Xác nhận cụm từ khôi phục')
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button')))
            element.click()
            time.sleep(3)
        except: 
            driver.quit()
            print('Error "Xác nhận cụm từ khôi phục"')
            
        try:
            print('Nhập mật khẩu mới')
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input")))
            element.send_keys('Minhcffc@321')
            time.sleep(3)
        except: 
            driver.quit()
            print('Error "Nhập mật khẩu mới"')
            

        try:
            print('Xác nhận mật khẩu')
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input")))
            element.send_keys('Minhcffc@321')
            time.sleep(3)
        except: 
            driver.quit()
            print('Error "Xác nhận mật khẩu"')
            
        try:
            print('I understand that Metamask')
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input")))
            driver.execute_script("arguments[0].click();", element)
        except: 
            driver.quit()
            print('Error "I understand that Metamask"')
            

        try:
            print('Import my wallet')
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button')))
            element.click()
            time.sleep(3)
        except: 
            driver.quit()
            print('Error "Import my wallet"')
            


        try:
            print('Got it')
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button')))
            element.click()
            time.sleep(3)
            
        except: 
            driver.quit()
            print('Error "Got it"')
            break

        try:
            print('Next')
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button')))
            element.click()
            time.sleep(3)
            
        except: 
            driver.quit()
            print('Error "Next"')
            break
        try:
            print('Done')
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button')))
            element.click()
            ExcelApp.write_excel(f'{CoKetQua}{For1}','Import Thành Công')
            print('Import Thành Công')
            time.sleep(3)
            driver.quit()
            break
        except: 
            driver.quit()
            print('Error "Done"')
            break

        # try:
        #     print('Nhập Password...')
        #     element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div/div/input")))
        #     element.send_keys('Minhcffc@321')
        #     time.sleep(3)  
      
        # except: 
        #     driver.quit()
        #     print('Error "Nhập Password"')
        #     break
        # try:
        #     print('Unlock')
        #     element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/button')))
        #     element.click()
        #     ExcelApp.write_excel(f'{CoKetQua}{For1}','Import Thành Công')
        #     print('Import Thành Công')
        #     time.sleep(3)
         
        # except: 
        #     driver.quit()
        #     print('Error "Unlock"')
        #     break
    else:
        ExcelApp.write_excel(f'{CoKetQua}{For1}','Import Không Thành Công')
        print('Import Không Thành Công')
        driver.quit()
               

if __name__ == "__main__":

    for For1 in range(1,101):
        if ExcelApp.read_excel(f'{CoKetQua}{For1}') is not None: continue
        TEN_PROFILE = ExcelApp.read_excel(f'B{For1}'); print(f'- STT{For1} NGƯỜI DÙNG: ',TEN_PROFILE)
        PATH_PROFILE = ExcelApp.read_excel(f'A{For1}'); print(f'- STT{For1} PATH_PROFILE: ',PATH_PROFILE)
        # EMAIL = ExcelApp.read_excel(f'F{For1}'); print(EMAIL)
        # PASSWORD_EMAIL = ExcelApp.read_excel(f'G{For1}'); print(PASSWORD_EMAIL)
        # EMAIL_RECOVERY = ExcelApp.read_excel(f'H{For1}'); print(EMAIL_RECOVERY)
        MNEMONIC_12KEY = ExcelApp.read_excel(f'J{For1}'); print(f'- STT{For1} MNEMONIC_12KEY: ',MNEMONIC_12KEY)
        options = ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        #options.add_argument('--start-maximized')
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-features=PrivacySandboxSettings4')
        options.add_argument(f"--user-data-dir={PATH_PROFILE}")
        
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1366, 768)
        driver.set_window_position(0, 0)
        time.sleep(2)
        extension_link = dict()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.title != '':
                extension_link[f'{driver.title}'] = driver.current_url
        createWallet(driver,For1,MNEMONIC_12KEY)
