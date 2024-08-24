import sys,os
import pyperclip

if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Gmail import *

def OKX_Connect_Button():
    target_title = "OKX Wallet"
    new_window_found = False
    main_window = driver.current_window_handle
    original_windows = driver.window_handles
    while not new_window_found:
        all_windows = driver.window_handles
        if len(all_windows) > len(original_windows):
            for window in all_windows:
                if window not in original_windows:
                    driver.switch_to.window(window)
                    if driver.title == target_title:
                        new_window_found = True
                        print(f"Tìm thấy cửa sổ với tiêu đề: {driver.title}")
                        break
            original_windows = all_windows  
        time.sleep(1)
    TimeInt = time.time(); TimeOut = 60
    while time.time() < TimeInt+TimeOut:
        try:
            driver.find_element(By.XPATH, '//div[text()="Connect"]').click()
            print('Connect')
            break
        except:
            time.sleep(0.5)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(main_window)
def OKX_Sign_Button():
    target_title = "OKX Wallet"
    main_window = driver.current_window_handle
    original_windows = driver.window_handles

    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        all_windows = driver.window_handles
        if len(all_windows) > len(original_windows):
            for window in all_windows:
                if window not in original_windows:
                    driver.switch_to.window(window)
                    if driver.title == target_title:
                        print(f"Tìm thấy cửa sổ với tiêu đề: {driver.title}")
                        break
            original_windows = all_windows  
        time.sleep(1)
    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            driver.find_element(By.XPATH, '//div[text()="Confirm"]').click()
            print('Confirm')
            break
        except:
            time.sleep(0.5)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(main_window)
def OKX_Login(driver, mnemonic):
    target_title = "OKX Wallet"
    new_window_found = False
    main_window = driver.current_window_handle
    original_windows = driver.window_handles
    while not new_window_found:
        all_windows = driver.window_handles
        if len(all_windows) > len(original_windows):
            for window in all_windows:
                if window not in original_windows:
                    driver.switch_to.window(window)
                    if driver.title == target_title:
                        new_window_found = True
                        print(f"Tìm thấy cửa sổ với tiêu đề: {driver.title}")
                        break
            original_windows = all_windows  
        time.sleep(1)
    TimeInt = time.time(); TimeOut = 60
    while time.time() < TimeInt+TimeOut:
        try:
            print('Import Wallet')
            driver.find_element(By.XPATH, '(//span[@class="btn-content"])[2]').click()
        except:
            time.sleep(0.5)
        try:
            print('Import Wallet')
            driver.find_element(By.XPATH, '(//div[@class="_wallet-space-item_1px67_9"])[1]').click()
            break
        except:
            time.sleep(0.5)
    TimeInt = time.time(); TimeOut = 30
    while time.time() < TimeInt+TimeOut:
        try:
            print('My seed phrase has 12 words')
            mnemonic_words = mnemonic.split()
            print(mnemonic_words)
            input_elements = driver.find_elements(By.XPATH, '//input[@class="mnemonic-words-inputs__container__input"]')
            for i, word in enumerate(mnemonic_words):
                input_elements[i].send_keys(word)
                time.sleep(0.1)
            time.sleep(3)
            break
        except:
            time.sleep(0.3)

    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            print('Confirm')
            driver.find_element(By.XPATH, '(//span[@class="btn-content"])[1]').click()
            break
        except:
            time.sleep(0.5)

    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            print('Password')
            driver.find_element(By.XPATH, '(//input[@type="password"])[1]').send_keys('Hungcuong@6789')
            break
        except:
            time.sleep(0.5)
    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            print('Confirm Password')
            driver.find_element(By.XPATH, '(//input[@type="password"])[2]').send_keys('Hungcuong@6789')
            break
        except:
            time.sleep(0.5)
    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            print('Confirm')
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            break
        except:
            time.sleep(0.5)
    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            driver.find_element(By.XPATH, '//span[@class="btn-content"]').click()
            print('Login OK')
            time.sleep(3)
            break
        except:
            time.sleep(0.5)
    
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(main_window)

def X_Click():
    TimeInt = time.time(); TimeOut = 10
    while time.time() < TimeInt+TimeOut:
        try:
            X = driver.find_element(By.XPATH, '(//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1tcrrgd"])[2]')
            X.click()
            time.sleep(3)
            break
        except:
            time.sleep(0.5)
oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua = "C"

if __name__=="__main__":
    for For1 in range(1, 999):

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

        _12KyTu = oExcel._ExcelReadCell(f"Z{For1}")
        if _12KyTu == None:sys.exit("Doc xong het _12KyTu")
        print(f"!!! STT {For1}:_12KyTu :  {_12KyTu}")

        Chrome_Driver = Google_Chrome()
        #Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)
        driver = Chrome_Driver.ChromeDriver_Setup(undetect_chrome=False ,add_extension=['Minh - OKX.crx'])
        
        OKX_Login(driver, _12KyTu)
        driver.get(LinkRef)

        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt+TimeOut:
            try:
                driver.find_element(By.XPATH, '//button[text()="Sign In"]').click()
                print('Sign In')
            except:
                time.sleep(0.5)
            try:
                driver.find_element(By.XPATH, '//p[text()="Wallet Connect"]').click()
            except:
                time.sleep(0.5)
            try:
                element = driver.execute_script('''
                    return document
                        .querySelector("body > w3m-modal")
                        .shadowRoot.querySelector("wui-flex > wui-card > w3m-router")
                        .shadowRoot.querySelector("div > w3m-connect-view")
                        .shadowRoot.querySelector("wui-flex > wui-list-wallet:nth-child(3)")
                        .shadowRoot.querySelector("button > wui-text");
                ''')
                element.click()
                OKX_Connect_Button()
                OKX_Sign_Button()
                time.sleep(3)
            except:
                time.sleep(0.5)

            try:
                welcome = driver.find_element(By.XPATH, '//h5[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom css-8gloed"]')
                print(welcome.text)
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell('Error Login',f'{CotKetQua}{For1}')
            driver.quit()
            continue


        driver.get('https://app.okapi.xyz/game/dapp_rating')

        while True:
            
            print('\nRate dApps')
            TimeInt = time.time(); TimeOut = 10
            while time.time() < TimeInt+TimeOut:
                try:
                    get_name = driver.find_element(By.XPATH,'(//p[@class="MuiTypography-root MuiTypography-body1 css-1012ct0"])[1]')
                    name = get_name.text
                    print(name)
                    break
                except:
                    time.sleep(0.5)

            TimeInt = time.time(); TimeOut = 10
            while time.time() < TimeInt+TimeOut:
                try:
                    print('Bullish')
                    bullish = driver.find_element('(//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-fullWidth MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedContained MuiButtonGroup-groupedContainedHorizontal MuiButtonGroup-groupedContainedPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-fullWidth MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedContained MuiButtonGroup-groupedContainedHorizontal MuiButtonGroup-groupedContainedPrimary MuiButtonGroup-firstButton css-1kdxslk"])[1]')
                    bullish.click()
                    break
                except:
                    time.sleep(0.5)

            TimeInt = time.time(); TimeOut = 10
            while time.time() < TimeInt+TimeOut:
                try:
                    input_name = driver.find_element(By.XPATH,'//input[@aria-invalid="true"]')
                    input_name.send_keys(name)
                    submit = driver.find_element(By.XPATH,'//button[@type="submit"]')
                    submit.click()
                    break
                except:
                    time.sleep(0.5)
            else: 
                print('Hết lượt đánh giá')
                break
            

        driver.get('https://app.okapi.xyz/game/dapp_arena')
        X_Click()

        ticket = driver.find_element(By.XPATH,'//div[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-1elrklf"]')
        number_ticket = int(ticket.text)
        all_ticket = 820 - number_ticket
        print('All ticket', all_ticket)
        for i in range(all_ticket):

            print(f'\nYour Eligible Ticket {number_ticket  + i}')

            parent_elements = driver.find_elements(By.XPATH, '//div[@class="MuiStack-root css-1c1vt4s" and .//p[@aria-label="Twitter Followers"] and .//p[contains(text(), "k")]]')

            followers_A = parent_elements[0].find_element(By.XPATH,'.//p[contains(text(), "k")]')
            sum_A = float(followers_A.text.replace('k','').strip())
            followers_B = parent_elements[1].find_element(By.XPATH,'.//p[contains(text(), "k")]')
            sum_B = float(followers_B.text.replace('k','').strip())
            print('Follower A: ',sum_A)
            print('Follower B: ',sum_B)

            if sum_A > sum_B:
                TimeInt = time.time(); TimeOut = 10
                while time.time() < TimeInt+TimeOut:
                    try:
                        followers_A.click()
                        time.sleep(1)
                        driver.find_element(By.XPATH,'//button[@class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation css-obh2wj"]').click()
                        print('Chọn A: ',sum_A)
                        break
                    except:
                        time.sleep(0.5)
            else:
                TimeInt = time.time(); TimeOut = 10
                while time.time() < TimeInt+TimeOut:
                    try:
                        followers_B.click()
                        time.sleep(1)
                        driver.find_element(By.XPATH,'//button[@class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation css-obh2wj"]').click()
                        print('Chọn B: ',sum_B)
                        break
                    except:
                        time.sleep(0.5)
            time.sleep(3)
        else:
            print('Hết lượt chơi')
            pass

        







        # for _ in range(number_turn):
        #     try:
               
        #         break
        #     except Exception as e:
        #         print(f"Lỗi: {e}")
        #         time.sleep(0.5)
        #     time.sleep(3)

        main_window = driver.current_window_handle
        for _ in range(5):
            try:
                print('--- Đang Verify')
                element = driver.find_element(By.XPATH, '(//div[@class="css-okxgzo"])[2]')
                element.click()
                print('2')
                driver.switch_to.window(main_window)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[text()="verify"]')))
                driver.find_element(By.XPATH, '//div[text()="verify"]').click()
            except NoSuchElementException:
                print("Thoát vòng lặp")
                break
            except Exception as e:
                print(f"Lỗi: {e}")
                time.sleep(0.5)
            time.sleep(3)

        TimeInt = time.time(); TimeOut = 15
        while time.time() < TimeInt+TimeOut:
            try:
                driver.refresh()
                get_point = driver.find_element(By.XPATH,'//p[@class="chakra-text css-1erw2ku"]')
                point = get_point.text
                print(point)
                oExcel._ExcelWriteCell(point,f'{CotKetQua}{For1}')
                break
            except: time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell('Error Get Point',f'{CotKetQua}{For1}')
            driver.quit()
        TimeInt = time.time(); TimeOut = 15
        while time.time() < TimeInt+TimeOut:
            try:
                pyperclip.copy('')
                ref = driver.find_element(By.XPATH,'//img[@class="chakra-image css-4g6ai3"]')
                ref.click()
                linkref = pyperclip.paste()
                print('Link Ref: ',linkref)
                oExcel._ExcelWriteCell(linkref,f'E{For1}')
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell('Error Get Link Ref',f'E{For1}')
            driver.quit()
            continue
        driver.quit()
