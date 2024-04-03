import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Twitter import *
from vinhthoai.Utils_GoogleChome import *
# from vinhthoai.Utils_Discord import *
# from vinhthoai.Utils_Web3py import *
import time,win32gui,sys,pyautogui
from datetime import datetime
# from anticaptchaofficial.imagetocoordinates import *
from telethon import functions, sessions,sync,errors
from telethon.tl.functions.account import *
from telethon.sessions import *
from datetime import datetime
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, CreateNewSession, UseCurrentSession
from opentele.exception import TDesktopUnauthorized,TFileNotFound
import asyncio,pyperclip
import cv2, numpy as np
from urllib.parse import unquote

oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua ="C"
DD_Telegram = r'D:\002-FileDATA-TelegramMoi'
User_Group = ['@memefi_chat']
User_Bot_Telegram = '@memefi_coin_bot'

async def main():

    DD_ProfileChrome = oExcel._ExcelReadCell(f"A{For1}")
    if DD_ProfileChrome==None:sys.exit("Doc xong het DD_ProfileChrome")
    print(f"!!! STT {For1}:DD_ProfileChrome :  {DD_ProfileChrome}")

    NguoiDung =  oExcel._ExcelReadCell(f"B{For1}")
    if NguoiDung == None: sys.exit("Xong Het NguoiDung")
    print(f"!!! STT {For1}: NguoiDung: {NguoiDung}")

    Ten_Telegram =  oExcel._ExcelReadCell(f"I{For1}")
    if Ten_Telegram == None: sys.exit("Xong Het Ten_Telegram")
    print(f"!!! STT {For1}: Ten_Telegram: {Ten_Telegram}")

    SDT_Telegram =  oExcel._ExcelReadCell(f"K{For1}")
    if SDT_Telegram == None: sys.exit("Xong Het SDT_Telegram")
    print(f"!!! STT {For1}: SDT_Telegram: {SDT_Telegram}")

    # Password_Telegram =  oExcel._ExcelReadCell(f"H{For1}")
    Password_Telegram =  'Hungcuong@6789'
    if Password_Telegram == None: sys.exit("Xong Het Password_Telegram")
    print(f"!!! STT {For1}: Password_Telegram: {Password_Telegram}")

    Path_File_Session = os.path.join(DD_Telegram,Ten_Telegram,SDT_Telegram + '.session')
    print(f"!!! STT {For1}: Path_File_Session: {Path_File_Session}")

    LinkRef =  oExcel._ExcelReadCell( f"X{For1}")
    print(f"!!! STT {For1}: LinkRef: {LinkRef}")
    oExcel._ExcelWriteCell(LinkRef, f"X{For1}")

    CodeRef = re.search('start=(.*)',LinkRef).group(1)
    print(f"!!! STT {For1}: CodeRef: {CodeRef}")

    api = API.TelegramDesktop.Generate(system="windows",unique_id=SDT_Telegram) #Lấy API offical Opentele
    client = TelegramClient(Path_File_Session,api=api) # TelegramClient Opentele

    try: await client.connect() # Kết nối Telethon
    except OSError: sys.exit('Failed to connect')

    if not await client.is_user_authorized(): # Kiểm Tra Phiên Telethon
        await client.disconnect()

        try:
            tdesktop = TDesktop(os.path.join(DD_Telegram,Ten_Telegram,'tdata'))
        except TFileNotFound:
            print("!!! Ko Thay key_data")
            return oExcel._ExcelWriteCell("!!! Ko Thay key_data", f"{CotKetQua}{For1}")

        try:
            client = await tdesktop.ToTelethon(Path_File_Session,CreateNewSession, api, password=Password_Telegram)
        except TDesktopUnauthorized:
            print("!!! Telegram Desktop Out")
            oExcel._ExcelWriteCell("Telegram Desktop Out", f"D{For1}")
            oExcel._ExcelWriteCell("Telegram Desktop Out", f"E{For1}")
            return oExcel._ExcelWriteCell("Telegram Desktop Out", f"{CotKetQua}{For1}")
        except TimeoutError:
            print("!!! Xoa chay Lai")
            return oExcel._ExcelWriteCell("!!! Xoa chay Lai", f"{CotKetQua}{For1}")
        await client.connect()

    # for i in User_Group:
    #     try:
    #         result = await client(functions.channels.JoinChannelRequest(i))
    #         if str(result.chats[0].username) not in i:
    #             await client.disconnect()
    #             return oExcel._ExcelWriteCell(f"Error Join {i}", f"{CotKetQua}{For1}")
    #         else:
    #             print(result.stringify())
    #             print(f"!!! STT {For1}: Join Group: {i} OK")
    #     except Exception as e : 
    #         print(f"!!! STT {For1}: Join Group: {e} ")
    #         await client.disconnect()
    #         return oExcel._ExcelWriteCell(str(e), f"{CotKetQua}{For1}")


    Chrome_Driver  = Google_Chrome()
    # Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)
    driver = Chrome_Driver.ChromeDriver_Setup( 
        binary_location=BROWER_DEFAUT,undetect_chrome=True,
        user_data_dir=DD_ProfileChrome)

    driver.get('https://web.telegram.org/a/')
    Timeint = time.time(); TimeOut= 60; check_login = 0
    while time.time() < Timeint + TimeOut:
        try:
            driver.find_element(By.XPATH,'//*[text()="Log in by phone Number"]').click()
        except: time.sleep(1)

        try:
            country =  driver.execute_script('return document.querySelector("#sign-in-phone-code").value')
            # print(country)
            if country == 'Vietnam' :
                input_phone = driver.find_element(By.XPATH,'//*[@id="sign-in-phone-number"]')
                input_phone.send_keys(SDT_Telegram)
                input_phone.send_keys(Keys.ENTER)
            time.sleep(5)
            check_login = 1
        except: time.sleep(0.5)

        try:
            driver.find_element(By.XPATH,'//*[@id="sign-in-code"]')
            break
        except: time.sleep(1)

        try:
            driver.find_element(By.XPATH,'//*[@id="telegram-search-input"]')
            await client.disconnect()
            print(">>>> Telegram còn phiên đăng nhập")
            break
        except: time.sleep(1)

    else:
        oExcel._ExcelWriteCell("Error Log in by phone Number", f"{CotKetQua}{For1}")
        return driver.quit()

    if check_login == 1:
            Timeint = time.time(); TimeOut= 60
            while time.time() < Timeint + TimeOut:
                message=  await client.get_messages(777000,limit= 1)
                re_code_login = re.search('Login code: (.*?). Do not give this code to anyone',message[0].message)
                if re_code_login:
                    code_login = re_code_login.group(1)
                    print(f"!!! Code Login API: {code_login}")
                    await client.disconnect()
                    break
            else:
                oExcel._ExcelWriteCell("Error No Code Login", f"{CotKetQua}{For1}")
                return driver.quit()

            Timeint = time.time(); TimeOut= 60; check_login = 0
            while time.time() < Timeint + TimeOut:
                try:
                    input_code = driver.find_element(By.XPATH,'//*[@id="sign-in-code"]')
                    input_code.clear()
                    input_code.send_keys(code_login)
                except: time.sleep(1)
                try:
                    input_password = driver.find_element(By.XPATH,'//*[@id="sign-in-password"]')
                    input_password.clear()
                    input_password.send_keys(Password_Telegram)
                    input_password.send_keys(Keys.ENTER)
                except: time.sleep(1)

                try:
                    driver.find_element(By.XPATH,'//*[@id="telegram-search-input"]')
                    print(">>>> Đăng nhập thành công Telegram")
                    break
                except: time.sleep(1)

            else:
                oExcel._ExcelWriteCell("Error Login Code OR Password", f"{CotKetQua}{For1}")
                return driver.quit()

    if oExcel._ExcelReadCell( f"Z{For1}") is None :   
        driver.get(f"https://web.telegram.org/k/#?tgaddr=tg%3A%2F%2Fresolve%3Fdomain%3Dmemefi_coin_bot%26start%3D{CodeRef}")
        time.sleep(3)
        
        Timeint = time.time(); TimeOut= 60; click = 0
        while time.time() < Timeint + TimeOut:
            try:
                driver.execute_script('document.querySelector(".btn-primary.btn-transparent.text-bold.chat-input-control-button.rp").click()') #start
                time.sleep(5)
            except: time.sleep(1)

            try:
                driver.execute_script('document.querySelector(".is-web-view.reply-markup-button.rp").click()')  
                time.sleep(5)
            except: time.sleep(1)

            try:
                driver.execute_script('document.querySelector(".popup-button.btn.primary.rp").click()') 
                time.sleep(5) 
            except: time.sleep(1)

            try:
                url  = driver.find_element(By.XPATH,'//iframe[@allow="camera; microphone; geolocation;"]').get_attribute('src')
                print(f"URL: {url}")
                if 'tgWebAppData' in url :
                    oExcel._ExcelWriteCell(url.replace("tgWebAppPlatform=web","tgWebAppPlatform=android").replace("tgWebAppPlatform=weba","tgWebAppPlatform=android"), f"Z{For1}")
                    break
            except: time.sleep(0.5)

        else:
            oExcel._ExcelWriteCell("Error Get Link Account", f"{CotKetQua}{For1}")     
            return driver.quit()
        # driver.quit()
    else:
        url = oExcel._ExcelReadCell( f"Z{For1}")

    driver.get(url.replace("tgWebAppPlatform=web","tgWebAppPlatform=android").replace("tgWebAppPlatform=weba","tgWebAppPlatform=android"))
    Timeint = time.time(); TimeOut= 120
    while time.time() < Timeint + TimeOut:
        try:
            driver.find_element(By.XPATH,'//p[text()="Start Playing"]')
            driver.get("https://tg-app.memefi.club/invite")
            time.sleep(1)
        except: time.sleep(0.5)
        try:
            text= driver.find_element(By.XPATH,'//*[@id=":r0:"]').get_attribute("value")
            if 't.me/memefi_coin_bot...' in text : 
                token = driver.execute_script("return localStorage['auth-token']")
                print("token",token)
                if 'ey' in token : break
            time.sleep(1)
        except: time.sleep(0.5)

    else:
        oExcel._ExcelWriteCell("Error auth-token", f"{CotKetQua}{For1}")
        return driver.quit()



    oExcel._ExcelWriteCell(token, f"D{For1}")
    oExcel._ExcelWriteCell(text.replace("t.me/memefi_coin_bot...","https://t.me/memefi_coin_bot?start=r_"), f"{CotKetQua}{For1}")
    return driver.quit()



if __name__ == "__main__":
    for For1 in range(1,9999):
        if oExcel._ExcelReadCell( CotKetQua + str(For1)) != None : continue
        # Google_Chrome().ChromeDriver_Kill(BROWER_DEFAUT)
        Reset_Modem()
        oExcel._ExcelBookSave()
        asyncio.new_event_loop().run_until_complete(main())
        print(1)


    
