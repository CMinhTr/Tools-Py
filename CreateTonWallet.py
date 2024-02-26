from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re,sys


from Library import Excel_App

Excel_App = Excel_App()
Key24Wallet = "B"
WalletAddress = "C"
def find_and_send_keys(xpath, text):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.send_keys(text)

def find_and_click(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
def find_and_get_text(xpath):
    element = driver.find_element(By.XPATH, xpath).text
    return element
def webdriver_wait(xpath):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--start-maximized')

for stt in range(1,501):
    Excel_App.Excel_Save()
    if Excel_App.Excel_Read(f'A{stt}') != None:continue
    print(f"!!! STT {stt} - Đang Khởi Chạy Vị Trí: {stt}")
    
    try:
        
        driver = webdriver.Chrome(options=options)
        driver.get('https://wallet.ton.org/')
        time.sleep(3)

        find_and_click('//*[@id="start_createBtn"]')
        find_and_click('//*[@id="createdContinueButton"]')

        num_items = ''
        for i in range(1,25):
            webdriver_wait(f'//*[@id="createWords"]/div[{i}]')
            word_nums = find_and_get_text(f'//*[@id="createWords"]/div[{i}]/span[1]')
            word_items = find_and_get_text(f'//*[@id="createWords"]/div[{i}]/span[2]')
    
            num_items += word_nums + word_items + ' '
        #print(num_items)
        danh_sach_tu = num_items.split()
        #print(danh_sach_tu)
        danh_sach_tu.sort(key=lambda x: int(x.split('.')[0]))

        # Tạo chuỗi mới từ danh sách đã sắp xếp
        chuoi_sap_xep = ' '.join(danh_sach_tu)
        keywallet = re.sub(r'[0-9.]', '', chuoi_sap_xep)
        # In kết quả
        print(chuoi_sap_xep)
        print(f'!!! STT {stt} KeyWall: ',keywallet)
        
        webdriver_wait('//*[@id="backup_continueBtn"]')
        find_and_click('//*[@id="backup_continueBtn"]')
        webdriver_wait('//*[@id="alert"]/div[3]/button[1]')
        find_and_click('//*[@id="alert"]/div[3]/button[1]')
        danh_sach_phan_tu = keywallet.split()
        find_and_send_keys('//*[@id="confirmInput0"]',danh_sach_phan_tu[int(driver.find_element(By.XPATH, '//*[@id="confirmInput0"]').get_attribute('data-index'))])
        find_and_send_keys('//*[@id="confirmInput1"]',danh_sach_phan_tu[int(driver.find_element(By.XPATH, '//*[@id="confirmInput1"]').get_attribute('data-index'))])
        find_and_send_keys('//*[@id="confirmInput2"]',danh_sach_phan_tu[int(driver.find_element(By.XPATH, '//*[@id="confirmInput2"]').get_attribute('data-index'))])
        find_and_click('//*[@id="wordsConfirm_continueBtn"]')
        find_and_send_keys('//*[@id="createPassword_input"]','NguoiDung@6789')
        find_and_send_keys('//*[@id="createPassword_repeatInput"]','NguoiDung@6789')
        find_and_click('//*[@id="createPassword_continueBtn"]')
        find_and_click('//*[@id="readyToGo_continueBtn"]')
        find_and_click('//*[@id="main_receiveBtn"]')
        find_and_click('//*[@id="receive"]/div[4]')
        webdriver_wait('//*[@id="receive"]/div[4]')

        wallet = driver.find_element(By.XPATH, '//*[@id="receive"]/div[4]').text
        print(f'!!! STT {stt} WalletAddress: ',wallet)
        Excel_App.Excel_Write(f'{Key24Wallet}{stt}',keywallet)
        Excel_App.Excel_Write(f'{WalletAddress}{stt}',wallet)
        driver.quit()
    except Exception as e:
        print(f'Error: {e}')

