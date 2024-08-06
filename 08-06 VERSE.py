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

        LinkRef = oExcel._ExcelReadCell(f"X{For1}")
        if LinkRef == None:sys.exit("Doc xong het LinkRef")
        print(f"!!! STT {For1}:LinkRef :  {LinkRef}")
        

        Chrome_Driver = Google_Chrome()
        driver = Chrome_Driver.ChromeDriver_Setup(undetect_chrome=True,user_data_dir=DD_ProfileChrome)
        driver.maximize_window()
        gmail_client = Gmail_Client(email=Email,password=Password,driver=driver)
        try:
            gmail_client.CheckLogin_Gmail()

        except Exception as e:
            driver.quit()
            oExcel._ExcelWriteCell(str(e),f"{CotKetQua}{For1}")
            continue
        
        driver.get(LinkRef)
       

        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                element = driver.find_element(By.XPATH,'//*[@id="kol-embed-page-frame-384904-0"]')
                src = element.get_attribute('src')
                print('src: ',src)
                driver.get(src)
                break
            except:
                time.sleep(0.5)
                print('--- Đang tìm "src"')
        else:
            oExcel._ExcelWriteCell('Error mở src',f'{CotKetQua}{For1}')
            driver.quit()
            continue


        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                element = driver.find_element(By.XPATH,'//*[@id="privacy_consent_label"]')
                driver.execute_script("arguments[0].click();", element)
                element.click()
            except:
                print('Error Click')
                time.sleep(0.5)
            try:
                full_name = driver.find_element(By.XPATH,'//input[@name="first_name"]')
                full_name.clear()
                full_name.send_keys(FullName)
            except:
                time.sleep(0.5)
            try:
                email = driver.find_element(By.XPATH,'//input[@name="email"]')
                email.clear()
                email.send_keys(Email)
            except:
                time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//input[@type="submit"]').click()
                print("Đã gửi code đăng ký")
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[text()="View Leaderboard"]')))
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell("Error gữi code đăng ký")

        try:    
            id_messagae = gmail_client.ReadIDMail_Gmail('Please click the following verification link to be added to the V-Card waitlist.',60)
            url_message = gmail_client.ReadMail_Gmail(id_messagae,'get_code\?id=(.*?)<')
            print(url_message)
        except Exception as e:
            oExcel._ExcelWriteCell(str(e), f"{CotKetQua}{For1}")
            continue
        input('---')
        driver.quit()












      

        
