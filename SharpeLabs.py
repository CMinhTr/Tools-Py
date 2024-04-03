import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_GoogleChome import *
oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua ="C"
Check_Register = 0
if __name__=="__main__":
    for For1 in range(1, 999):

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


        FullName = oExcel._ExcelReadCell(f"H{For1}")
        if FullName == None:sys.exit("Doc xong het FullName")
        print(f"!!! STT {For1}:FullName :  {FullName}")

        Chrome_Driver  = Google_Chrome()
        driver = Chrome_Driver.ChromeDriver_Setup(
            user_data_dir=DD_ProfileChrome,
            undetect_chrome=True,load_extension=['CAPTCHA-Solver'])

        try:
            id_message = Chrome_Driver.ReadIDMail_Gmail('Verify your email for Sharpe App',15)
            oExcel._ExcelWriteCell(id_message, f"D{For1}")
            code_verify = Chrome_Driver.ReadMail_Gmail(id_message,'apiKey=(.*?)lang=en')
            link_veryfiy = f"https://sharpe-d41c2.firebaseapp.com/__/auth/action?apiKey={code_verify}lang=en".replace("&amp;","&").replace("<wbr>","")
            driver.get(link_veryfiy)
        except Exception as e:
            pass
 


        if Check_Register == 0 : 
            driver.get("https://terminal.sharpe.ai/signup/")
            Timeint = time.time(); TimeOut= 30;Error = 0
            while time.time() < Timeint + TimeOut:
                try:    
                    e_email = driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(Email)
                    break
                except: time.sleep(0.5)
            else:
                driver.quit()
                oExcel._ExcelWriteCell("Error Không Thấy Email", f"{CotKetQua}{For1}")
                continue

            driver.find_element(By.XPATH,'//*[@id="firstname"]').send_keys(FullName.split(" ",1)[0])
            driver.find_element(By.XPATH,'//*[@id="lastname"]').send_keys(FullName.split(" ",1)[1])
            driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(Password)
            driver.find_element(By.XPATH,'//*[@placeholder="Confirm Password"]').send_keys(Password)
            driver.find_element(By.XPATH,'//*[text()="I agree to privacy policy & terms"]').click()

            Timeint = time.time();TimeOut = 120; Error = 0
            while time.time() < Timeint + TimeOut:
                try:
                    driver.find_element(By.XPATH,'//button[text()="Agree"]').click()
                except: time.sleep(0.5)

                try:
                    if check_recaptcha(driver):
                        driver.find_element(By.XPATH,'//button[text()="sign up"]').click()
                except: time.sleep(0.5)
                
                if 'Account activation link sent to your email' in driver.page_source : break
                # if 'This email is already in use' in driver.page_source : 
                #     break
            else:
                driver.quit()
                oExcel._ExcelWriteCell("Error Giải Được Captcha", f"{CotKetQua}{For1}")
                continue

            try:
                id_message = Chrome_Driver.ReadIDMail_Gmail('Verify your email for Sharpe App')
                oExcel._ExcelWriteCell(id_message, f"D{For1}")
                code_verify = Chrome_Driver.ReadMail_Gmail(id_message,'apiKey=(.*?)lang=en')
                link_veryfiy = f"https://sharpe-d41c2.firebaseapp.com/__/auth/action?apiKey={code_verify}lang=en".replace("&amp;","&").replace("<wbr>","")
            except Exception as e:
                driver.quit()
                oExcel._ExcelWriteCell(f"Error {str(e)}", f"{CotKetQua}{For1}")
                continue
            driver.get(link_veryfiy)
        else:
            driver.get("https://terminal.sharpe.ai/login/")

        Timeint = time.time();TimeOut = 120; Error = 0
        while time.time() < Timeint + TimeOut:
            try:
                code = driver.find_element(By.XPATH, '//button[text()="Continue"]').click()
            except: time.sleep(0.5)

            try:
                code = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(Email)
                break
            except: time.sleep(0.5)
        else:
            driver.quit()
            oExcel._ExcelWriteCell("Error Continue Verify", f"{CotKetQua}{For1}")
            continue
        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(Password)        
        driver.find_element(By.XPATH,'//*[text()="remember me"]').click()

        Timeint = time.time();TimeOut = 120; Error = 2
        while time.time() < Timeint + TimeOut:
            if check_recaptcha(driver) : 
                try:
                    driver.find_element(By.XPATH,'//button[text()="log in"]').click()
                except : time.sleep(0.5)

            if "you've earned 100 sharpe points" in driver.page_source : break

        else:
            driver.quit()
            oExcel._ExcelWriteCell("Error Login", f"{CotKetQua}{For1}")
            continue


        oExcel._ExcelWriteCell(f"Đăng Ký Thành Công Rồi Đó Nha", f"{CotKetQua}{For1}")
        driver.quit()

        
