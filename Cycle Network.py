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
        time.sleep(3)
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
verify = '''
var divs = document.querySelectorAll('div.css-1ykwh6m');
var found = false;
divs.forEach(function(div) {
    if (div.textContent.trim() === "verify") {
        div.click();
        found = true;
        console.log("Đã click vào phần tử với text 'verify'.");
    }
});
if (!found) {
    console.log("Không tìm thấy phần tử <div> với text 'verify'.");
}
'''
if __name__=="__main__":
    for For1 in range(1,999):

        if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue
        #Reset_Modem()
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
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt+TimeOut:
            try:
                driver.get('https://x.com/intent/follow?screen_name=iotex_io')
                element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Following @iotex_io"]')))
                print('Fowllow iotex_io OK')
                break
            except: 
                try:
                    element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Follow @iotex_io"]')))
                    element.click()
                    print('Fowllow iotex_io OK')
                except: 
                    driver.find_element(By.XPATH,'//button[@data-testid="confirmationSheetConfirm"]').click()
                    
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt+TimeOut:
            try:
                driver.get('https://x.com/tapup_tg')
                element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Following @tapup_tg"]')))
                print('Fowllow tapup_tg OK')
                break
            except: 
                try:
                    element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Follow @tapup_tg"]')))
                    element.click()
                    print('Fowllow tapup_tg OK')
                except: 
                    driver.find_element(By.XPATH,'//button[@data-testid="confirmationSheetConfirm"]').click()
                    
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt+TimeOut:
            try:
                driver.get('https://x.com/intent/follow?screen_name=cyclenetwork_GO')
                element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Following @cyclenetwork_GO"]')))
                print('Fowllow cyclenetwork_GO OK')
                break
            except: 
                try:
                    element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@aria-label="Follow @cyclenetwork_GO"]')))
                    element.click()
                    print('Fowllow cyclenetwork_GO OK')
                except:
                    driver.find_element(By.XPATH,'//button[@data-testid="confirmationSheetConfirm"]').click()
                    

        driver.get(LinkRef)
    
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[@aria-label="Close"]')))
            close = driver.find_element(By.XPATH,'//button[@aria-label="Close"]')
            close.click()
        except: time.sleep(0.5)
        try:

            signNature = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[text()="Sign signature"]')))
            if signNature:
                driver.find_element(By.XPATH,'//div[text()="Sign signature"]').click()
                time.sleep(3)
                main_window = driver.current_window_handle
                all_windows = driver.window_handles
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        print('Đang ở cửa sổ: ',driver.title)
                        if driver.title == "MetaMask":
                            scrSign = '''
                            var buttons = document.querySelectorAll('button');
                            var found = false;
                            buttons.forEach(function(button) {
                                if (button.textContent.trim() === "Sign") {
                                    button.click();
                                    found = true;
                                }
                            });
                            if (!found) {
                                console.log("Không tìm thấy phần tử <button> với text 'Sign'.");
                            }
                        '''
                            driver.execute_script(scrSign)
                        
                            
        except: 
            TimeInt = time.time(); TimeOut = 60
            while time.time() < TimeInt + TimeOut:
                try:
                    print("Connect Wallet")
                    driver.find_element(By.XPATH,'(//p[text()="Connect Wallet"])[2]').click()
                    print("MetaMask")
                    driver.find_element(By.XPATH,'//span[text()="MetaMask"]').click()
                    time.sleep(3)
                    break
                except: time.sleep(0.5)
            
            found = False
            TimeInt = time.time(); TimeOut = 60
            while time.time() < TimeInt + TimeOut and not found:
                try:
                    main_window = driver.current_window_handle
                    all_windows = driver.window_handles
                    for window in all_windows:
                        if window != main_window:
                            driver.switch_to.window(window)
                            print('Đang ở cửa sổ: ', driver.title)
                            if driver.title == "MetaMask":

                                scrNext = '''
                                var buttons = document.querySelectorAll('button');
                                var found = false;
                                buttons.forEach(function(button) {
                                    if (button.textContent.trim() === "Next") {
                                        button.click();
                                        found = true;
                                    }
                                });
                                if (!found) {
                                    console.log("Không tìm thấy phần tử <button> với text 'Next'.");
                                }
                            '''
                                driver.execute_script(scrNext)
                                print("Next")
                                time.sleep(3)
                                scrConfirm = '''
                                var buttons = document.querySelectorAll('button');
                                var found = false;
                                buttons.forEach(function(button) {
                                    if (button.textContent.trim() === "Confirm") {
                                        button.click();
                                        found = true;
                                    }
                                });
                                if (!found) {
                                    console.log("Không tìm thấy phần tử <button> với text 'Confirm'.");
                                }
                            '''
                                driver.execute_script(scrConfirm)
                                print("Confirm")
                                time.sleep(3)

                                scrApprove = '''
                                var buttons = document.querySelectorAll('button');
                                var found = false;
                                buttons.forEach(function(button) {
                                    if (button.textContent.trim() === "Approve") {
                                        button.click();
                                        found = true;
                                    }
                                });
                                if (!found) {
                                    console.log("Không tìm thấy phần tử <button> với text 'Approve'.");
                                }
                            '''
                                driver.execute_script(scrApprove)
                                print("Approve")
                                time.sleep(3)

                                scrSwitchNetwork = '''
                                var buttons = document.querySelectorAll('button');
                                var found = false;
                                buttons.forEach(function(button) {
                                    if (button.textContent.trim() === "Switch network") {
                                        button.click();
                                        found = true;
                                    }
                                });
                                if (!found) {
                                    console.log("Không tìm thấy phần tử <button> với text 'Switch network'.");
                                }
                            '''
                                driver.execute_script(scrSwitchNetwork)
                                print("Switch Network")
                                found = True
                                break  # Thoát vòng lặp for nếu tìm thấy và xử lý cửa sổ MetaMask
                        
                except Exception as e:
                    print(f"Lỗi: {e}")
                    time.sleep(0.5)

            windows = driver.window_handles
            driver.switch_to.window(windows[0])
            TimeInt = time.time(); TimeOut = 60
            while time.time() < TimeInt + TimeOut:    
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[text()="Sign signature"]')))    
                driver.find_element(By.XPATH,'//div[text()="Sign signature"]').click()
                print("Sign Signature")
                break

            TimeInt = time.time(); TimeOut = 60
            while time.time() < TimeInt + TimeOut:
                signNature = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[text()="Sign signature"]')))
                if signNature:
                    driver.find_element(By.XPATH,'//div[text()="Sign signature"]').click()
                    time.sleep(3)
                    main_window = driver.current_window_handle
                    all_windows = driver.window_handles
                    for window in all_windows:
                        if window != main_window:
                            driver.switch_to.window(window)
                            print('Đang ở cửa sổ: ',driver.title)
                            if driver.title == "MetaMask":
                                scrSign = '''
                                var buttons = document.querySelectorAll('button');
                                var found = false;
                                buttons.forEach(function(button) {
                                    if (button.textContent.trim() === "Sign") {
                                        button.click();
                                        found = true;
                                    }
                                });
                                if (!found) {
                                    console.log("Không tìm thấy phần tử <button> với text 'Sign'.");
                                }
                            '''
                                driver.execute_script(scrSign)
                                break
                
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt + TimeOut:
            try:
                driver.find_element(By.XPATH,'//div[text()="Claimed"]')
                print("Verify OK")
                print('Claimed')
                break
            except: time.sleep(0.5)
            try:
                driver.execute_script("document.querySelector('.css-okxgzo').scrollIntoView({ behavior: 'smooth' });")
                print("Cuộn đến cuối trang")
            except: time.sleep(0.5)
            try:
                driver.execute_script(verify)
            except: time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//div[text()="connect"]').click()
                print('Click Connect Twitter')
            except: time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//*[@class="submit button selected"]').click()
            except: time.sleep(0.5)
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt + TimeOut:
            windows = driver.window_handles
            driver.switch_to.window(windows[0])
            try:
                driver.find_element(By.XPATH,'//div[text()="Claimed"]')
                print("Verify OK")
                print('Claimed')
                break
            except: time.sleep(0.5)

            try:
                driver.execute_script("document.querySelector('.css-okxgzo').scrollIntoView({ behavior: 'smooth' });")
                print("Cuộn đến cuối trang")
            except: time.sleep(0.5)
            try:
                driver.execute_script(verify)
            except: time.sleep(0.5)
            try:
                element = driver.find_element(By.XPATH,'(//div[text()="follow"])[1]')
                element.click()
                print("Click Follow")
            except: time.sleep(0.5)

            
        input('----')

    





