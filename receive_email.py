import email.utils
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup

# Thông tin đăng nhập email
username = "canlong878@gmail.com"
password = "apsajwmcxaymesvq"

def receive_email():
    result = ""

    # Kết nối đến máy chủ IMAP
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    from_email = 'do-not-reply@ses.binance.com'
    status, messages = mail.search(None, f'(FROM "{from_email}")')

    email_ids = messages[0].split()
    email_data = []
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_date = email.utils.parsedate_to_datetime(msg['Date'])
                email_data.append((email_data,msg))
    email_data.sort(key=lambda x: x[0], reverse=True)
    if email_data:
        last_email = email_data[0][1]

        encode_subtitle = last_email['Subject']
        decode_subtitle_part = decode_header(encode_subtitle)
        decode_subtitle = ''
        for part, encoding in decode_subtitle_part:
            if isinstance(part, bytes):
                decode_subtitle += part.decode(encoding or 'utf-8')
            else:
                decode_subtitle += part

        if last_email.is_multipart():
            for part in last_email.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    body = payload.decode() if isinstance(payload, bytes) else payload
                    result += decode_subtitle + extract_binance_code(body)
        else:
            payload = last_email.get_payload(decode=True)
            body = payload.decode() if isinstance(payload, bytes) else payload
            result += decode_subtitle + '- Mã Binance: ' + extract_binance_code(body)

    mail.close()
    mail.logout()
    return result

def extract_binance_code(html_body):
    soup = BeautifulSoup(html_body, "html.parser")
    binance_code_div = soup.find("div", style="font-family:BinancePlex,Arial,PingFangSC-Regular,'Microsoft YaHei',sans-serif;font-size:20px;font-weight:900;line-height:30px;text-align:left;color:#f0b90b;")
    if binance_code_div:
        return binance_code_div.get_text().strip()
    return ""

# Gọi hàm receive_email để nhận và xử lý email
email_content = receive_email()
print("Email Content: ", email_content)
