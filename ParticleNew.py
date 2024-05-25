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
        oExcel._ExcelWriteCell('Login Không Thành Công' , f'{CotKetQua}{For1}')
        print('Login Không Thành Công')
        driver.quit()
    

if __name__ == "__main__":

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

        UserName_Twitter = oExcel._ExcelReadCell(f"M{For1}")
        if UserName_Twitter == None:sys.exit("Doc xong het UserName_Twitter")
        print(f"!!! STT {For1}:UserName_Twitter :  {UserName_Twitter}")
        
        Chrome_Driver  = Google_Chrome()
        Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)
        driver = Chrome_Driver.ChromeDriver_Setup(
            user_data_dir=DD_ProfileChrome,
            undetect_chrome=False)

        loginWallet()

        driver.get(f'https://x.com/intent/post?text=+&url=https%3A%2F%2Fx.com%2FParticleNtwrk%2Fstatus%2F1786002826788745605&via=ParticleNtwrk&hashtags=ChainAbstraction')
        time.sleep(3)

        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Post')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[text()="Post"])[1]')))
                btn_post = driver.find_element(By.XPATH,'(//*[text()="Post"])[1]')
                btn_post.click()
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell("Error Post", f"{CotKetQua}{For1}")
            driver.quit()
            continue


        driver.get(f'https://x.com/{UserName_Twitter}')
        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Get Href')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21"])[1]')))
                get_href_post = driver.find_element(By.XPATH,'(//*[@class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21"])[1]')
                href = get_href_post.get_attribute('href')
                print(href)
                oExcel._ExcelWriteCell(href, f"AE{For1}")
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell("Error Get Href", f"{CotKetQua}{For1}")
            driver.quit()
            continue

        driver.get('https://pioneer.particle.network/en/point')
        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Verify')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Verify"]')))
                Verify = driver.find_element(By.XPATH,'//*[text()="Verify"]')
                Verify.click()
                break
            except:
                time.sleep(0.5)
                
        else:
            oExcel._ExcelWriteCell("Error Verify", f"{CotKetQua}{For1}")
            driver.quit()
            continue    

        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Paste Href')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-slot="input"]')))
                Paste_Href = driver.find_element(By.XPATH,'//*[@data-slot="input"]')
                Paste_Href.send_keys(href)
                break
            except:
                time.sleep(0.5)
                
        else:
            oExcel._ExcelWriteCell("Error Paste Href", f"{CotKetQua}{For1}")
            driver.quit()
            continue  

        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Verify')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[text()="Verify"])[2]')))
                Verify = driver.find_element(By.XPATH,'(//span[text()="Verify"])[2]')
                Verify.click()
                break
            except:
                time.sleep(0.5)
                
        else:
            oExcel._ExcelWriteCell("Error Verify 2", f"{CotKetQua}{For1}")
            driver.quit()
            continue    

        Timeint = time.time(); TimeOut= 60
        while time.time() < Timeint + TimeOut:
            try:
                print('>>> Earned 1000 points')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Earned 1000 points"]')))
                Earned = driver.find_element(By.XPATH,'//*[text()="Earned 1000 points"]')
                print(Earned.text)
                time.sleep(3)
                oExcel._ExcelWriteCell("Earned 1000 points", f"{CotKetQua}{For1}")
                driver.quit()
                break
            except:
                time.sleep(0.5)
                
        else:
            oExcel._ExcelWriteCell("Error Earned 100 points", f"{CotKetQua}{For1}")
            driver.quit()
            continue    
