import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Gmail import *
oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')

CotKetQua ="C"
def loginWallet():

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
        oExcel._ExcelWriteCell(f'{CotKetQua}{For1}','Import Không Thành Công')
        print('Import Không Thành Công')
def click_button_with_text(driver, text):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//button[text()="{text}"]'))
        )
        button.click()
    except Exception as e:
        print(f"Không tìm thấy phần tử <button> với text '{text}': {e}")

if __name__=="__main__":
    for For1 in range(1,999):

        if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue
        Reset_Modem()
        oExcel._ExcelBookSave()
        
        DD_ProfileChrome = oExcel._ExcelReadCell(f"A{For1}")
        if DD_ProfileChrome==None:sys.exit("Doc xong het DD_ProfileChrome")
        print(f"!!! STT {For1}:DD_ProfileChrome :  {DD_ProfileChrome}")
                        
        NguoiDung= oExcel._ExcelReadCell(f"B{For1}")
        if NguoiDung==None:sys.exit("Doc xong het Nguoi Dung")
        print(f"!!! STT {For1}:Nguoi Dung :  {NguoiDung}")

        Email = oExcel._ExcelReadCell(f"F{For1}")
        if Email == None:sys.exit("Doc xong het Email")
        print(f"!!! STT {For1}:Email :  {Email}")

        Password = oExcel._ExcelReadCell(f"G{For1}")
        if Password == None:sys.exit("Doc xong het Password")
        print(f"!!! STT {For1}:Password :  {Password}")

      
        LinkRef = oExcel._ExcelReadCell(f"X{For1}")
        if LinkRef == None:sys.exit("Doc xong het LinkRef")
        print(f"!!! STT {For1}:LinkRef :  {LinkRef}")

        Chrome_Driver = Google_Chrome()
        #Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)

        driver = Chrome_Driver.ChromeDriver_Setup(user_data_dir=DD_ProfileChrome, undetect_chrome=False)
        
        extension_link = dict()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.title != '':
                extension_link[f'{driver.title}'] = driver.current_url
        loginWallet()

        driver.get(LinkRef)
        try:
            signNature = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//div[text()="Sign signature"]')))
            if signNature:
                signNature.click()
                WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'(//p[text()="Connect Wallet"])[2]')))
                driver.find_element(By.XPATH,'(//p[text()="Connect Wallet"])[2]').click()
                WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//span[text()="MetaMask"]')))
                driver.find_element(By.XPATH,'//span[text()="MetaMask"]').click()

        except:
            time.sleep(0.5)
       
        TimeInt = time.time(); TimeOut = 60
        found = False
        while time.time() < TimeInt + TimeOut and not found:
            try:
                main_window = driver.current_window_handle
                all_windows = driver.window_handles
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        print('Đang ở cửa sổ: ', driver.title)
                        if driver.title == "MetaMask":
                            click_button_with_text(driver, "Next")
                            click_button_with_text(driver, "Confirm")
                            click_button_with_text(driver, "Approve")
                            click_button_with_text(driver, "Switch network")
                            found = True
                            break  # Thoát vòng lặp for nếu tìm thấy và xử lý cửa sổ MetaMask
                else:
                    continue  # Nếu không có break trong for, tiếp tục vòng lặp while
                break  # Nếu có break trong for, thoát vòng lặp while
            except Exception as e:
                print(f"Lỗi: {e}")
                    

        

        input('----')

    





