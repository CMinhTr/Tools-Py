from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Library import Excel_App

Excel_App =Excel_App()


def find_and_send_keys(xpath, text):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.send_keys(text)

def find_and_click(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

url = 'https://docs.google.com/forms/d/e/1FAIpQLSfVLqcsxTizccpNRgCxGIT8r7M6BZdTN9FYopiNJLpiOXcDFg/viewform'
for i in range(1, 6):
    Excel_App.Excel_Save()
    TwitterHandle = Excel_App.Excel_Read(f'D{i}')
    TelegramUsername = Excel_App.Excel_Read(f'E{i}')
    EmailID = Excel_App.Excel_Read(f'C{i}')
    

    user_data_dir = Excel_App.Excel_Read(fr'A{i}')
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(3)

        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', TwitterHandle)
        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', TelegramUsername)
        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', '0x7496401674nCyNR28HT235RWERohwe3')
        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', EmailID)
        find_and_click('//div[@id="i21"]')
        find_and_click('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        time.sleep(5)
        Excel_App.Excel_Write(f'F{i}','Điền Form OK')
        print("Điền Form OK")

    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()
