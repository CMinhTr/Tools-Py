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
def disable_extensions(driver):

    driver.get('chrome://extensions/')

    extensionIds = ['jiidiaalihmmhddjgbnbgdfflelocpak','mcohilncbfahbmgdjkbpemcciiolgcge','pdliaogehgdbhbnmkklieghmmjkpigpa']
    script = '''
    let extensionIds = arguments[0];
    extensionIds.forEach(extensionId => {
        let manager = document.querySelector("body > extensions-manager").shadowRoot;
        let itemsList = manager.querySelector("#items-list").shadowRoot;
        let extension = itemsList.querySelector(`#${extensionId}`);
        if (extension) {
            let toggle = extension.shadowRoot.querySelector('cr-toggle');
            if (toggle && toggle.hasAttribute('checked')) {
                toggle.click();
            }
        }
    });
    '''
    driver.execute_script(script, extensionIds)
                    
if __name__=="__main__":

    for For1 in range(1,999):

        if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue
        #Reset_Modem()
        oExcel._ExcelBookSave()
        extension_link = dict()
        

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



        Chrome_Driver = Google_Chrome()
        Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)

        driver = Chrome_Driver.ChromeDriver_Setup(user_data_dir=DD_ProfileChrome, undetect_chrome=False)

        driver.maximize_window()
        disable_extensions(driver)
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.title != '':
                extension_link[f'{driver.title}'] = driver.current_url

        
        loginWallet()
        
        driver.get('https://protocol.carv.io/airdrop')
        TimeInt = time.time(); TimeOut = 60
        while time.time() < TimeInt+TimeOut:
            
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Login"]')))
                login = driver.find_element(By.XPATH,'//button[text()="Login"]')
                login.click()
                print('Choose Login')
            except:
                time.sleep(0.5)
            try:
                    
                MetaMask = driver.find_element(By.XPATH,'(//div[@class="iekbcc0 ju367v4 ju367va ju367v14 ju367v1s"])[1]')
                MetaMask.click()
                print('Choose MetaMask')
            except:
                time.sleep(0.5)
            try:
                print('Sign')
                main_window = driver.current_window_handle
                all_windows = driver.window_handles

                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        print("Đã chuyển sang cửa sổ:", driver.title)
                        # Thực hiện các thao tác trên cửa sổ popup ở đây

                # Sau khi hoàn thành, chuyển lại cửa sổ chính (nếu cần)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
                
                driver.switch_to.window(main_window)
                break
            except: 
                time.sleep(0.5)
        
        input('---')

            
