from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

try:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeIkfK23eZSEq2hnmxRZOmawCQ16m9KC_hqDsP7OztKCUaTyQ/viewform')
    sleep(3)

    elements = {
        'send_mail': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input',
        'send_address': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        'click_polygon': '//*[@id="i16"]',
        'send_website': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
        'send_idGithub': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
        'send_project': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea',
        'send_contact': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea',
        'btn_send': '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    }

    for key, value in elements.items():
        element = driver.find_element(By.XPATH, value)
        if key == 'click_polygon':
            element = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, value)))
        if 'send_mail' in key:
            element.send_keys('abc@gmail.com')
        elif 'send_address' in key:
            element.send_keys('0xd5ca946ac1c1f24eb26dae9e1a53ba6a02bd97fe') 
        elif 'send_website' in key:
            element.send_keys('Twitter')
        elif 'send_idGithub' in key:
            element.send_keys('idGithub')
        elif 'send_project' in key:
            element.send_keys('Your project description and progress')
        elif 'send_contact' in key:
            element.send_keys("What's the best way to contact you?")
        else:
             element.click()

    print("Điền Form OK")

except Exception as e:
    print("Error")

sleep(5)
