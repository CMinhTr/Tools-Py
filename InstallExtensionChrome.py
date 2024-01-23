from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui

for i in range(1,6):
    user_data_dir = f'C:\\Users\\Admin\\Desktop\\HCVIP - 3\\ChromeProfile\\ChromeProfile\\ChromeProfile - {i}'
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    start_time = time.time()
    time_wait = 10
    print(start_time)
    # while time.time() < start_time + time:

    #try:
    driver.get("https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn")
    add_click = driver.find_element(By.XPATH,'//span[text()="Add to Chrome"]')
    add_click.click()
    #except Exception as e:
    #print(f'Error: {e}')
    time.sleep(5)
    pyautogui.click(996, 288)
    time.sleep(5)
    driver.quit()
