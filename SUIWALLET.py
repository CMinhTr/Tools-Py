import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Gmail import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua ="C"

def send_tui_token(WalletAddress):
    driver.get('chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html?type=popup#/send?type=0x2%3A%3Asui%3A%3ASUI')

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Select Coin Amout To Send')
            amout_sui = '0.000000001'
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="coin-amount-input"]')))
            element.send_keys(amout_sui)
            oExcel._ExcelWriteCell('_Send: ' + amout_sui, f"AJ{For1}")
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Select Coin Amout To Send", f"{CotKetQua}{For1}")
        driver.quit()

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Enter Recipient Address')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="address-input"]')))
            element.send_keys(WalletAddress)
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Enter Recipient Address", f"{CotKetQua}{For1}")
        driver.quit()

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Review')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
            element.click()
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Review", f"{CotKetQua}{For1}")
        driver.quit()

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Send Now')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Send Now"]')))
            element.click()
            break
        except:
            try:
                print('>>> Review')
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
                element.click()
                
            except:
                time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Send Now", f"{CotKetQua}{For1}")
        driver.quit()

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Gas Fees')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="font-medium text-body text-gray-90"]')))
            gasfee = element.text
            print(gasfee)
            oExcel._ExcelWriteCell(gasfee, f"AK{For1}")
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Gas Fees", f"{CotKetQua}{For1}")
        driver.quit()

    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Get Href')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@class="text-hero-dark no-underline"])[1]')))
            href = driver.find_element(By.XPATH, '(//*[@class="text-hero-dark no-underline"])[1]').get_attribute('href')
            #href = get_href.get_attribute("href")
            print(href)
            transaction = re.findall(r'0x[0-9a-fA-F]+',href)
            if transaction:
                link_transaction = 'https://suiscan.xyz/mainnet/object/' + transaction[0]
                oExcel._ExcelWriteCell(link_transaction, f"AN{For1}")
            else:
                oExcel._ExcelWriteCell('Error Link Transaction', f"AN{For1}")
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell('Error Link Transaction', f"AN{For1}")
        time.sleep(0.5)
        
    Timeint = time.time(); TimeOut= 30
    while time.time() < Timeint + TimeOut:
        try:
            print('>>> Transaction')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="overlay-title"]')))
            oExcel._ExcelWriteCell("Send Token SUI OK " + get_time(), f"{CotKetQua}{For1}")
            break
        except:
            time.sleep(0.5)
    else:
        oExcel._ExcelWriteCell("Error Send Token SUI", f"{CotKetQua}{For1}")
        driver.quit()

    
def import_sui_wallet(_12KyTu):
            try:
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[0])
                driver.get('chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/accounts/import-passphrase')
            except:
                time.sleep(0.5)

        
            try:
                print('>>> Import _12KyTu')
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@type="password"]')))
                driver.find_element(By.XPATH,'//*[@id="recoveryPhrase.0"]').send_keys(_12KyTu)
                driver.find_element(By.XPATH,'//*[@type="submit"]').click()
            except:
                time.sleep(0.5)
    
            try:
                print('>>> Nhập Password')
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@type="password"]')))
                driver.find_element(By.XPATH,'//*[@name="password.input"]').send_keys('Hungcuong@6789')
                driver.find_element(By.XPATH,'//*[@name="password.confirmation"]').send_keys('Hungcuong@6789')
                driver.find_element(By.XPATH,'//*[@id="acceptedTos"]').click()
                driver.find_element(By.XPATH,'//*[@type="submit"]').click()
                time.sleep(3)
            except:
                time.sleep(0.5)

            try:
                driver.find_element(By.XPATH,'//*[@data-testid="bullshark-dismiss"]').click()
                driver.find_element(By.XPATH,'//*[text()="Home"]').click()
            except:
                time.sleep(0.5)
        
def get_sui_txHash(WalletAddress):
    url = f'https://suiscan.xyz/api/sui-backend/mainnet/api/accounts/{WalletAddress}/transactions?transactionsParticipationType=SENDER&orderBy=DESC'
    response = requests.get(url)
    data = response.json()
    tx_count = sum(1 for tx in data['content'] if tx['type'] == 'Programmable Tx')
    return tx_count

def get_sui_token(WalletAddress):
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Content-Type": "application/json" 
        }
    response = requests.request(method='POST',
                                url = 'https://suiscan.xyz/api/sui/mainnet/', 
                                data=json.dumps({
                                        "jsonrpc": "2.0",
                                        "id": 1,
                                        "method": "suix_getBalance",
                                        "params": {
                                            "owner": f"{WalletAddress}"
                                        }
                                    }), headers=headersList)
    if response.status_code == 200:
        response_data = response.json()
        total_balance = response_data.get("result", {}).get("totalBalance", "Not Found")
        balance = int(total_balance) / 1000000000
        print(f"Total Balance: {balance}")
        return balance
    else:
        print(f"Request failed with status code {response.status_code}")
                  
if __name__ == "__main__":  

    for For1 in range(1,999):

        if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue

        _12KyTu = oExcel._ExcelReadCell(f"X{For1}")
        if _12KyTu == None:sys.exit("Doc xong het _12KyTu")
        print(f"!!! STT {For1}:_12KyTu :  {_12KyTu}")

        WalletAddress = oExcel._ExcelReadCell(f"AG{For1}")
        if WalletAddress == None:sys.exit("Doc xong het WalletAddress")
        print(f"!!! STT {For1}:WalletAddress :  {WalletAddress}")

        # op = Options()
        # op.add_extension(r'C:\Users\Admin\Desktop\SUIWALLET.crx')
        # driver = webdriver.Chrome(options=op)
        Chrome_Driver  = Google_Chrome()
        Chrome_Driver.ChromeDriver_Kill(BROWER_DEFAUT)
        driver = Chrome_Driver.ChromeDriver_Setup(add_extension=['Minh - SUIWALLET.crx'])
        oExcel._ExcelWriteCell(get_sui_token(WalletAddress), f"AH{For1}")
        oExcel._ExcelWriteCell('TxHash: ' + str(get_sui_txHash(WalletAddress)), f"AI{For1}")
        import_sui_wallet(_12KyTu)
        send_tui_token(WalletAddress)
        oExcel._ExcelWriteCell(get_sui_token(WalletAddress), f"AL{For1}")
        oExcel._ExcelWriteCell('TxHash: ' + str(get_sui_txHash(WalletAddress)), f"AM{For1}")
        driver.quit()
