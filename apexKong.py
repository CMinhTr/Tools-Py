import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Gmail import *
oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua ="C"
Check_Register = 0
if __name__=="__main__":
    for For1 in range(1, 999):

        if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue
        #Reset_Modem()
        oExcel._ExcelBookSave()

        NguoiDung= oExcel._ExcelReadCell(f"B{For1}")
        if NguoiDung==None:sys.exit("Doc xong het Nguoi Dung")
        print(f"!!! STT {For1}:Nguoi Dung :  {NguoiDung}")

        _12KyTu = oExcel._ExcelReadCell(f"Z{For1}")
        if _12KyTu == None:sys.exit("Doc xong het _12KyTu")
        print(f"!!! STT {For1}:_12KyTu :  {_12KyTu}")
        
        Wallet = oExcel._ExcelReadCell(f"S{For1}")
        if Wallet == None:sys.exit("Doc xong het Wallet")
        print(f"!!! STT {For1}:Wallet :  {Wallet}")

        Chrome_Driver = Google_Chrome()
        #Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)
        driver = Chrome_Driver.ChromeDriver_Setup(undetect_chrome=False,add_extension=['Minh - OKX.crx'])
        driver.maximize_window()
        driver.get('https://www.apex.exchange/kong')


        
        target_title = "OKX Wallet"
        new_window_found = False
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
                mnemonic_words = _12KyTu.split()
                print(mnemonic_words)
                input_elements = driver.find_elements(By.XPATH, '//input[@class="mnemonic-words-inputs__container__input"]')
                for i, word in enumerate(mnemonic_words):
                    input_elements[i].send_keys(word)
                    time.sleep(0.5)
                break
            except:
                time.sleep(0.5)
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
            except:
                time.sleep(0.5)
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
                driver.close()
                break
            except:
                time.sleep(0.5)
        
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[0])
        driver.refresh()
        print(driver.title)
        TimeInt = time.time(); TimeOut = 10
        while time.time() < TimeInt+TimeOut:
            try:
                driver.find_element(By.XPATH,'//p[text()="Connect Wallet"]').click()
                print('Connect Wallet')
                time.sleep(0.5)
                driver.execute_script('ethereum.enable()')
                break
            except:
                time.sleep(0.5)

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
        
        driver.find_element(By.XPATH,'(//button[@data-testid="okd-button"])[2]').click()

        TimeInt = time.time(); TimeOut = 10
        while time.time() < TimeInt+TimeOut:
            try:
                driver.find_element(By.XPATH,'(//img[@class="w-[40px] h-[40px]"])[2]').click()
                print('Task')
            except:
                time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'(//div[text()="GO"])[2]').click()
                print('GO')
                time.sleep(0.5)
                break
            except:
                time.sleep(0.5)
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[1])

        TimeInt = time.time(); TimeOut = 10
        while time.time() < TimeInt+TimeOut:
            try:
                driver.find_element(By.XPATH,'(//span[@class="x-button-txt"])[3]').click()
                print('Connect Wallet')
                driver.execute_script('ethereum.enable()')
                break
            except:
                time.sleep(0.5)
            
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
        
        driver.find_element(By.XPATH,'(//button[@data-testid="okd-button"])[2]').click()










        input('---')
    
   











      

        
