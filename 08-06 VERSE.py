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
                full_name = driver.find_element(By.XPATH,'//input[@name="first_name"]')
                full_name.clear()
                full_name.send_keys(FullName)
                time.sleep(3)
            except:
                time.sleep(0.5)
            try:
                email = driver.find_element(By.XPATH,'//input[@name="email"]')
                email.clear()
                email.send_keys(Email)
                time.sleep(3)
            except:
                time.sleep(0.5)
            try:
                element = driver.find_element(By.XPATH,'//*[@id="privacy_consent_label"]')
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
            except:
                print('Error Click')
                time.sleep(0.5)
            try:
                driver.find_element(By.XPATH,'//input[@type="submit"]').click()
                time.sleep(3)
                print("Đã gửi code đăng ký")
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[text()="View Leaderboard"]')))
                break
            except:
                time.sleep(0.5)
        else:
            oExcel._ExcelWriteCell("Error gữi code đăng ký")
            continue


        try:    
            id_messagae = gmail_client.ReadIDMail_Gmail('Please click the following verification link to be added to the V-Card waitlist.',60)
            url_message = gmail_client.ReadMail_Gmail(id_messagae,'(?s)verify-email\?c=(.*?)"')
            print(url_message)
        except Exception as e:
            oExcel._ExcelWriteCell(str(e), f"{CotKetQua}{For1}")
            continue



        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                url_verify = f'https://app.kickofflabs.com/verify-email?c={url_message}'
                driver.get(url_verify)
                print('--- Đã truy cập Verify Me')
                break
            except:
                time.sleep(0.5)
                print('--- Đang truy cập Verify Me')
        else:
            oExcel._ExcelWriteCell('Error Verify Me',f'{CotKetQua}{For1}')
            continue
        
        main_window = driver.current_window_handle
        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            driver.switch_to.default_content()
            try:
                follow_us_on_X = driver.find_element(By.XPATH,'//div[text()="Follow us on X!"]')
                follow_us_on_X.click()
                print('--- Đang tìm button Follow')
            except:
                time.sleep(0.5)

            try:
                iframe = driver.find_element(By.XPATH,'//*[@id="twitter-widget-0"]')
                driver.switch_to.frame(iframe)
            except: time.sleep(0.5)

            try:
                try:
                    iframe = driver.find_element(By.XPATH,'//*[@id="twitter-widget-0"]')
                    driver.switch_to.frame(iframe)
                except: time.sleep(0.5)
                driver.find_element(By.XPATH,'//b[text()="@VerseEcosystem"]').click()
                # driver.execute_script('''
                #     var buttons = document.querySelectorAll('b');
                #     var found = false;
                #     buttons.forEach(function(button) {
                #         if (button.textContent.trim() === "@VerseEcosystem") {
                #             button.click();
                #             found = true;
                #         }
                #     });
                # ''')
                print('Follow @VerseEcosystem')
                break   
            except:
                time.sleep(0.5)
                print('Error Follow @VerseEcosystem')
        
        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                
                driver.find_element(By.XPATH,'//div[text()="Join us on Telegram!"]').click()
                print('Join us on Telegram!')
                break
            except:
                time.sleep(0.5)
                print('Error Join us on Telegram!')

        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                driver.switch_to.window(main_window)
                repost_us = driver.find_element(By.XPATH,'//div[text()="Repost us!"]')
                repost_us.click()
                print('--- Đang tìm button Repost us!')
            except:
                time.sleep(0.5)

            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[@class="btn btn-twitter"]')))
                driver.find_element(By.XPATH,'//a[@class="btn btn-twitter"]').click()
                print('Retweet')
                break
            except:
                time.sleep(0.5)
                print('Error Retweet')
        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                driver.switch_to.window(main_window)
                get_ref = driver.find_element(By.XPATH,'//input[@class="kol-copy-and-paste-sharelink form-control form-control-appended has-set-radius"]')
                ref = get_ref.get_attribute('value')
                print('Ref: ',ref)
                oExcel._ExcelWriteCell(ref,f'{CotKetQua}{For1}')
                break
            except:
                time.sleep(0.5)
                print('--- Đang tìm ref')
        else:
            oExcel._ExcelWriteCell('Error lấy Ref',f'{CotKetQua}{For1}')

        Timeint = time.time(); TimeOut= 60; 
        while time.time() < Timeint + TimeOut:
            try:
                driver.refresh()
                WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'(//span[@class="kol-data-replace"])[2]')))
                get_point = driver.find_element(By.XPATH,'(//span[@class="kol-data-replace"])[2]')
                point = get_point.text
                print('Point: ',point)
                oExcel._ExcelWriteCell(point,f'D{For1}')
            except:
                print('Error get point')    
        driver.quit()












      

        
