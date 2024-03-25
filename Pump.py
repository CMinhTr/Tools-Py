from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,pyperclip

from Library import ExcelApp,reset_modem
ExcelApp = ExcelApp()
For1 ='3'
CoKetQua = 'C'

TEN_PROFILE = ExcelApp.read_excel(f'B{For1}'); print(f'- STT {For1}: TEN_PROFILE:',TEN_PROFILE)
PATH_PROFILE = ExcelApp.read_excel(f'A{For1}'); print(f'- STT {For1}: PATH_PROFILE:',PATH_PROFILE)
# EMAIL = ExcelApp.read_excel(f'F{For1}'); print(f'- STT {For1}: EMAIL:',EMAIL)
# PASSWORD_EMAIL = ExcelApp.read_excel(f'G{For1}'); print(f'- STT {For1}: PASSWORD_EMAIL:',PASSWORD_EMAIL)
# EMAIL_RECOVERY = ExcelApp.read_excel(f'H{For1}'); print(f'- STT {For1}: EMAIL_RECOVERY:',EMAIL_RECOVERY)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument('--disable-features=PrivacySandboxSettings4')
options.add_argument(f"--user-data-dir={PATH_PROFILE}")
driver = webdriver.Chrome(options=options)

driver.get('https://pump.markets/')
curent_tab = driver.current_window_handle

enter_ref = WebDriverWait(driver,timeout=30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/main/div/section[1]/div/div/div[2]/div/input')))
enter_ref.send_keys('91563912')

btn_connnect_twitter = WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/main/div/section[2]/div/div/button[1]')))
btn_connnect_twitter.click()

time.sleep(3)
all_tabs = driver.window_handles

# Kiểm tra xem có tab thứ hai không
if len(all_tabs) > 1:
    tab_to_switch = all_tabs[1]
    driver.switch_to.window(tab_to_switch)

    # Thực hiện thao tác chỉ khi tab thứ hai được mở
    btn_aAuthorize_app = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/span/span')))
    btn_aAuthorize_app.click()

    # Sau khi thao tác hoàn tất, chuyển lại tab đầu tiên để tiếp tục thao tác
    time.sleep(10)
    driver.switch_to.window(curent_tab)

    btn_like_rt = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/main/div/section[2]/div/div/button[2]')))
    btn_like_rt.click()
    
    time.sleep(3)
else:
    print("Tab thứ hai không tồn tại hoặc đã đóng.")

try:
    #all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[0])
    time.sleep(3)
    btn_tweet_intive_code = WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/main/div/section[2]/div/div/button[3]')))
    btn_tweet_intive_code.click()
except: time.sleep(0.5)

try:
    #all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[2])
    time.sleep(3)
    btn_post = WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span')))
    btn_post.click()
except: time.sleep(0.5)

driver.switch_to.window(curent_tab)
btn_join = WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div[1]/div[2]/a')))
btn_join.click()

driver.switch_to.window(curent_tab)
btn_copy_invitecode = WebDriverWait(driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/button')))
btn_copy_invitecode.click()

clipboard_content = pyperclip.paste()
print("Nội dung từ clipboard:", clipboard_content)
driver.quit()
input('----')




