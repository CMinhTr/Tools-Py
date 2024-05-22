import requests
import json
import sys,os
if os.getenv('COMPUTERNAME') == 'HCVIP-1':
    sys.path.insert(0,r'F:\Share-MayChu\005-File Chay Tool 2022')
else:
    sys.path.insert(0,r'\\HCVIP-1\Share-MayChu\005-File Chay Tool 2022')

from vinhthoai.Utils_Gmail import *

oExcel=Excel(win32gui.GetWindowText(win32gui.FindWindow('XLMAIN',None)),'title')
CotKetQua ="C"
for For1 in range(1,999):

    if oExcel._ExcelReadCell(f'{CotKetQua}{For1}')!=None:continue
    WalletAddress = oExcel._ExcelReadCell(f"A{For1}")
    if WalletAddress == None:sys.exit("Doc xong het WalletAddress")
    print(f"!!! STT {For1}:WalletAddress :  {WalletAddress}")


    # Payload JSON

    # Headers (nếu cần)
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Content-Type": "application/json" 
        }

    # Gửi yêu cầu POST tới API
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

    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        # Chuyển đổi phản hồi JSON thành dictionary
        response_data = response.json()
        # Lấy giá trị totalBalance
        total_balance = response_data.get("result", {}).get("totalBalance", "Not Found")
        balance = int(total_balance) / 1000000000
        print(f"Total Balance: {balance}")
        oExcel._ExcelWriteCell(balance,f'{CotKetQua}{For1}')
    else:
        print(f"Request failed with status code {response.status_code}")
