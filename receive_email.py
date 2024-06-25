import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
username = "canlong878@gmail.com"
password = "apsajwmcxaymesvq"


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
mail.select("inbox")

from_email = 'do-not-reply@ses.binance.com'
status, messages = mail.search(None,f'(FROM "{from_email}")')

email_ids = messages[0].split()

for email_id in email_ids:
    # Lấy dữ liệu của từng email
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
       
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            # In ra thông tin cơ bản của email
            print(f"From: {msg['From']}")
            print(f"Subject: {msg['Subject']}")
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                            payload = part.get_payload(decode=True)
                            body = payload.decode() if isinstance(payload, bytes) else payload
                            print("Body:", body)
            else:
                payload = msg.get_payload(decode=True)
                body = payload.decode() if isinstance(payload, bytes) else payload
                soup = BeautifulSoup(body,"html.parser")
                print("Soup: ", soup)
                binance_code = soup.find("div", style="font-family:BinancePlex,Arial,PingFangSC-Regular,'Microsoft YaHei',sans-serif;font-size:20px;font-weight:900;line-height:30px;text-align:left;color:#f0b90b")
                print("Mã kích hoạt Binance: ",binance_code.get_text())
                print("Body:", body)
                print("Payload: ", payload)
# Biến lưu trữ mã kích hoạt

                input('----')
mail.close()
mail.logout()

