from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


for i in range(1, 6):
    user_data_dir = f'D:\\Chrome\\Chrome\\NguoiDung-00{i}'
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ&fbzx=-5264965397473189805')
        time.sleep(3)

        def find_and_send_keys(xpath, text):
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.send_keys(text)

        def find_and_click(xpath):
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()

        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 'TranCongMinh')
        find_and_send_keys('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea', 'TranCongMinhTranCongMinhTranCongMinhTranCongMinhTranCongMinhTranCongMinh')
        find_and_click('//*[@id="i13"]/div[3]/div')
        find_and_click('//*[@id="i27"]')
        find_and_click('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(2)
        find_and_click('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]')
        time.sleep(3)
        find_and_click(f'(//div[@class="AB7Lab Id5V1"])[4]')
        find_and_click(f'(//div[@class="AB7Lab Id5V1"])[9]')
        find_and_click(f'(//div[@class="AB7Lab Id5V1"])[15]')
        find_and_click(f'(//div[@class="AB7Lab Id5V1"])[21]')
        find_and_click(f'(//div[@class="AB7Lab Id5V1"])[27]')
        find_and_click('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        time.sleep(5)
        print("Điền Form OK")
    
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()
