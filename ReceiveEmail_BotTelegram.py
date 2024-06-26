import imaplib
import email
from email.header import decode_header
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parsedate_to_datetime

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder, MessageHandler, filters
from bs4 import BeautifulSoup
load_dotenv()

username = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_PASSWORD')
TOKEN = "7457380542:AAHFBLtRqNJ_FLkZGjUFC2baxiCvh7H73rQ"


def receive_email():
    result = ""

    # Kết nối đến máy chủ IMAP
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    from_emails = ['do-not-reply@ses.binance.com', 'do-not-reply@post.binance.com']
    email_data = []

    for from_email in from_emails:
        status, messages = mail.search(None, f'(FROM "{from_email}")')
        if status != "OK":
            result += f"Không thể tìm thấy email từ địa chỉ: {from_email}\n"
            continue

        email_ids = messages[0].split()
        print(f"Found {len(email_ids)} emails from {from_email}")
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_date = parsedate_to_datetime(msg['Date'])
                    print(email_date)
                    email_data.append((email_date, msg))

    # Sắp xếp email theo thời gian từ mới nhất đến cũ nhất
    email_data.sort(key=lambda x: x[0], reverse=True)

    # Lấy email gần nhất
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
                    result += decode_subtitle + ' - Mã Binance: ' + extract_binance_code(body)
        else:
            payload = last_email.get_payload(decode=True)
            body = payload.decode() if isinstance(payload, bytes) else payload
            result += decode_subtitle + ' - Mã Binance: ' + extract_binance_code(body)

    mail.close()
    mail.logout()
    return result

def extract_binance_code(html_body):
    soup = BeautifulSoup(html_body, "html.parser")
    binance_code_div = soup.find("div", style="font-family:BinancePlex,Arial,PingFangSC-Regular,'Microsoft YaHei',sans-serif;font-size:20px;font-weight:900;line-height:30px;text-align:left;color:#f0b90b;")
    if binance_code_div:
        return binance_code_div.get_text().strip()
    return ""

# Hàm xử lý lệnh /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Chào! Gửi tin nhắn cho tôi và tôi sẽ chuyển tiếp nó đến email.')

async def canlong878(update: Update, context: CallbackContext) -> None:
    email_data = receive_email()
    await update.message.reply_text(email_data)

# Hàm main
def main() -> None:
    # Khởi tạo bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Đăng ký các handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("canlong878", canlong878))

    # Gửi email thông báo khởi động bot
    #notify_startup()

    # Bắt đầu bot
    app.run_polling()

if __name__ == '__main__':

    main()
