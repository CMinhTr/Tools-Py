from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import openpyxl
from time import sleep
import undetected_chromedriver as uc

# Đọc thông tin từ file Excel
file_path = 'profile_info.xlsx'  # Thay đổi tên file và đường dẫn tương ứng
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Khởi tạo trình duyệt Chrome và mở từng profile
for row in sheet.iter_rows(min_row=1, values_only=True):  # Bắt đầu từ dòng thứ hai (đầu tiên chứa tiêu đề)
    path_to_profile = row[0]  # Lấy đường dẫn profile từ cột đầu tiên
    TenProfile = [1]
    email = row[2]  # Lấy thông tin email từ cột thứ hai
    password = row[3]  # Lấy thông tin mật khẩu từ cột thứ ba
    
    
    # Khởi tạo tùy chọn cho Chrome với đường dẫn profile


    options = uc.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--profile-directory={TenProfile}")
    options.add_argument(f'--user-data-dir={path_to_profile}')
    # Khởi tạo trình duyệt với các tùy chọn đã thiết lập
    driver = uc.Chrome(options=options)

    driver.get('https://accounts.google.com/')
    # add email
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    sleep(10)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    sleep(10)
    driver.quit()
workbook.save(file_path)
