from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

try:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ&fbzx=-5264965397473189805')
    time.sleep(3)
    questionOneOption  = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    questionOneOption.send_keys('TranCongMinh')

    questionTwoOption = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    questionTwoOption.send_keys('TranCongMinhTranCongMinhTranCongMinhTranCongMinhTranCongMinhTranCongMinh')

    questionThreeSelect = driver.find_element(By.XPATH,'//*[@id="i13"]/div[3]/div')
    questionThreeSelect.click()

    questionFourSelect = driver.find_element(By.XPATH,'//*[@id="i27"]')
    questionFourSelect.click()

    Choose = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    Choose.click()
    time.sleep(2)
    Choice_1 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]')
    Choice_1.click()
    time.sleep(3)

    questionTenSelect = driver.find_element(By.XPATH,'(//div[@class="AB7Lab Id5V1"])[4]')
    questionTenSelect.click()

    questionSixSelect = driver.find_element(By.XPATH,'(//div[@class="AB7Lab Id5V1"])[9]')
    questionSixSelect.click()

    questionSevenSelect = driver.find_element(By.XPATH,'(//div[@class="AB7Lab Id5V1"])[15]')
    questionSevenSelect.click()

    questionEightSelect = driver.find_element(By.XPATH,'(//div[@class="AB7Lab Id5V1"])[21]')
    questionEightSelect.click()

    questionNineSelect = driver.find_element(By.XPATH,'(//div[@class="AB7Lab Id5V1"])[27]')
    questionNineSelect.click()


    Submit = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    Submit.click()
    
    print("Điền Form OK")
    input('sssss')
except Exception as e:
    print("Error ",e)

