import asyncio
import requests
import pyuseragents
from eth_account.messages import encode_defunct
from web3 import Web3, Account

Account.enable_unaudited_hdwallet_features()

mnemonic = "garlic develop visit stay celery model erase stadium snack elevator increase thunder"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://protocol.carv.io",
    "referer": "https://protocol.carv.io/",
    "user-agent": pyuseragents.random(),
    "x-app-id": "carv",
}

# Lấy text từ API để ký
url = f"https://interface.carv.io/protocol/wallet/get_signature_text"
response = requests.request('GET', url, json=None, headers=headers).json()

rp = response["data"]["text"]
print('Response: ', rp)

# Kết nối với mạng OP BNB
op_rpc = "https://opbnb-mainnet-rpc.bnbchain.org"
op_bnb = Web3(Web3.HTTPProvider(op_rpc))
print('op_bnb: ', op_bnb)

# Tạo ví từ mnemonic
op_bnb_wallet = op_bnb.eth.account.from_mnemonic(mnemonic)
print('op_bnb_wallet: ', op_bnb_wallet)

private_key_a = op_bnb_wallet._private_key
print('private_key_a: ', private_key_a)

# Ký tin nhắn
encoded_msg = encode_defunct(text=rp)
print('encoded_msg: ', encoded_msg)

signed_msg = Web3().eth.account.sign_message(encoded_msg, private_key=private_key_a)
a = signed_msg.signature.hex()
print('Signed_msg: ', a)

# Đăng nhập và lấy token
json_data = {
    "wallet_addr": "0x50d7f0fbe86ef1e0f065d648998bf8567018b4c5",
    "text": rp,
    "signature": a,
}

login_url = f"https://interface.carv.io/protocol/login"

response_login = requests.request('POST', login_url, json=json_data).json()
rp_login = response_login['data']['token']
print('rp_login: ', rp_login)
print('response_login: ', response_login)

# Hàm process_mint()
async def process_mint():
    try:
        # Kiểm tra số dư
        balance = op_bnb.eth.get_balance(op_bnb_wallet.address)
        if balance == 0:
            print(f"Insufficient balance for mint | Network: OP")
            return
        
        # Thực hiện mint
        # Bạn cần thay đổi đoạn này theo yêu cầu thực tế của quá trình mint
        mint_url = f"https://interface.carv.io/airdrop/mint/carv_soul"
        mint_data = {
            "chain_id": 2020
        }
        response_mint = requests.request('POST', mint_url, json=mint_data, headers=headers).json()
        
        if response_mint['code'] == 0:
            print(f"Minted soul successfully: {response_mint['data']} | Network: OP")
        else:
            print(f"Failed to mint soul: {response_mint['msg']} | Network: OP")
        
    except Exception as error:
        print(f"Error during minting: {error}")

# Chạy hàm process_mint
asyncio.run(process_mint())
