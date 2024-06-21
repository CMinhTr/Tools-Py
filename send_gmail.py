import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import Updater, filters, CommandHandler, CallbackContext, ApplicationBuilder, MessageHandler
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv('sender_email')
sender_password = os.getenv('sender_password')
recipient_email = "congminh25112002@gmail.com"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Xin chào'

msg.attach(MIMEText('Xin Chào Công Minh', 'plain'))
try:
    # Sử dụng context manager để thiết lập server và kết nối
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print('Email đã được gửi thành công!')
except Exception as e:
    print(f'Lỗi: {e}')
