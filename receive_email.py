import imaplib
import email
from email.utils import parsedate_to_datetime
from email.header import decode_header
from bs4 import BeautifulSoup

import re

username = "NogglerZebley992@gmail.com"
password = "wxluiehdpdfqvaih"

def binance_code(username, password):
    result = ''  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        mail.login(username, password)
    except imaplib.IMAP4.error:
        print('Email Login Failed')
        return result

    mail.select('INBOX')

    from_emails = [
        'do-not-reply@binance.com',
        'donotreply@directmail.binance.com',
        'do-not-reply@post.binance.com',
        'do-not-reply@ses.binance.com',
        'do_not_reply@mailer.binance.com',
        'do_not_reply@mailer1.binance.com',
        'do_not_reply@mailer2.binance.com',
        'do_not_reply@mailer3.binance.com',
        'do_not_reply@mailer4.binance.com',
        'do_not_reply@mailer5.binance.com',
        'do_not_reply@mailer6.binance.com',
        'notifications@post.binance.com',
        'do-not-reply@notice.binance.com',
        'do_not_reply@mgmailer.binance.com',
        'do-not-reply@directmail2.binance.com',
        'do_not_reply@mgmailer2.binance.com',
        'do_not_reply@mgdirectmail.binance.com'
    ]

    email_data = []

    for from_email in from_emails:
        status, messages = mail.search(None, f'(FROM "{from_email}")')
        if status != "OK":
            result += f'Không thể tìm thấy email từ địa chỉ: {from_email}\n'
            continue

        email_ids = messages[0].split()
        print(f"Found {len(email_ids)} emails from {from_email}")
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, '(RFC822)')

            for response_data in msg_data:
                if isinstance(response_data, tuple):
                    msg = email.message_from_bytes(response_data[1])
                    email_date = parsedate_to_datetime(msg['Date'])
                    email_data.append((email_date, msg))
    email_data.sort(key=lambda x: x[0], reverse=True)

    if email_data:
        last_email = email_data[0][1]
        subject = last_email['Subject']
        decoded_subject = decode_header(subject)
        subject_title = ''

        for part, encoding in decoded_subject:
            if isinstance(part, bytes):
                subject_title += part.decode(encoding if encoding else 'utf-8')
            else:
                subject_title += part

        payload = last_email.get_payload(decode=True)
        body = payload.decode('utf-8', errors='ignore')
        soup = BeautifulSoup(body, 'html.parser')
        get_binance_code = soup.find('div', style="font-family: BinancePlex,Arial,PingFangSC-Regular,'Microsoft YaHei',sans-serif; font-size: 18px; line-height: 30px; text-align: left; color: #f0b90b;")
        
        if get_binance_code:
            binance_code = get_binance_code.get_text()
            result = subject_title + ' - Code: ' + binance_code
        else:
            result = subject_title + ' - Không tìm thấy mã Binance'
    else:
        result = 'Không tìm thấy email nào từ các địa chỉ Binance'

    return result


def bybit_code(username, password):
    result = ''  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        mail.login(username, password)
    except imaplib.IMAP4.error:
        print('Email Login Failed')
        return result

    mail.select('INBOX')

    from_emails = [
        'notification@bybit.com',
        'notification@noreply.bybit.com',
        'notification@notification-2.bybit.com'

    ]

    email_data = []

    for from_email in from_emails:
        status, messages = mail.search(None, f'(FROM "{from_email}")')
        if status != "OK":
            result += f'Không thể tìm thấy email từ địa chỉ: {from_email}\n'
            continue

        email_ids = messages[0].split()

        print(f"Found {len(email_ids)} emails from {from_email}")
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, '(RFC822)')

            for response_data in msg_data:
                if isinstance(response_data, tuple):
                    msg = email.message_from_bytes(response_data[1])
                    email_date = parsedate_to_datetime(msg['Date'])
                    print(email_date)
                    email_data.append((email_date, msg))

    email_data.sort(key=lambda x: x[0], reverse=True)

    if email_data:
        last_email = email_data[0][1]
        subject = last_email['Subject']
        decoded_subject = decode_header(subject)
        subject_title = ''

        for part, encoding in decoded_subject:
            if isinstance(part, bytes):
                subject_title += part.decode(encoding if encoding else 'utf-8')
            else:
                subject_title += part
        
        payload = last_email.get_payload(decode=True)
        body = payload.decode('utf-8', errors='ignore')
        soup = BeautifulSoup(body, 'html.parser')
        get_bybit_code = soup.get_text()
        match = re.search(r'(\d{6})', get_bybit_code)
        if match:
            bybit_code = match.group(1)
            result += subject_title + ' - Code: ' + bybit_code
        else:
            result += subject_title + ' - Không tìm thấy mã Bybit'
    else:
        result = 'Không tìm thấy email nào từ các địa chỉ Bybit'

    return result

def mexc_code(username, password):
    result = ''  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        mail.login(username, password)
    except imaplib.IMAP4.error:
        print('Email Login Failed')
        return result

    mail.select('INBOX')

    from_emails = [
        'mexc@email.mexc.link',
        'mexc@email.mexc.ci',
        'mexc@email.mexc.cg',
        'mexc_official@email.mexc.link',
        'do_not_reply@mailer.mexc.sg',
        'mexc@notice.mexc.link',
        'mexc@notice.mexc.cg',
        'mexc@notice.mexc.ci',
        'mexc@info.mexc.link',
        'mexc@info.mexc.cg',
        'mexc@info.mexc.ci',
        'dontreply@notification.mexc.link',
        'dontreply@notification.mexc.cg',
        'dontreply@notification.mexc.ci'

    ]

    email_data = []

    for from_email in from_emails:
        status, messages = mail.search(None, f'(FROM "{from_email}")')
        if status != "OK":
            result += f'Không thể tìm thấy email từ địa chỉ: {from_email}\n'
            continue

        email_ids = messages[0].split()

        print(f"Found {len(email_ids)} emails from {from_email}")
        for email_id in email_ids:
            print('Email ID', email_id)
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            print('Msg: ', msg_data)
            for response_data in msg_data:
                if isinstance(response_data, tuple):
                    msg = email.message_from_bytes(response_data[1])
                    email_date = parsedate_to_datetime(msg['Date'])
                    print(email_date)
                    email_data.append((email_date, msg))

    email_data.sort(key=lambda x: x[0], reverse=True)

    if email_data:
        last_email = email_data[0][1]
        print('Last Email: ', last_email)
        subject = last_email['Subject']
        decoded_subject = decode_header(subject)
        subject_title = ''
        for part, encoding in decoded_subject:
            if isinstance(part, bytes):
                subject_title += part.decode(encoding if encoding else 'utf-8')
            else:
                subject_title += part

        #payload = last_email.get_payload(decode=True)
        for part in last_email.walk():
            if part.get_content_type() == 'text/plain':
                payload = part.get_payload(decode=True)
                print('Payload: ', payload)
                break  # Stop after finding the plain text part

        
        if not payload:
            result = 'Không có nội dung email để xử lý'
            return result

        try:
            body = payload.decode('utf-8', errors='ignore')
        except AttributeError:
            result = 'Không thể giải mã nội dung email'
            return result

        print('Body: ', body)

        soup = BeautifulSoup(body, 'html.parser')
        get_bybit_code = soup.get_text()
        match = re.search(r'(\d{6})', get_bybit_code)
        if match:
            bybit_code = match.group(1)
            result += subject_title + ' - Code: ' + bybit_code
        else:
            result += subject_title + ' - Không tìm thấy mã MEXC'
    else:
        result = 'Không tìm thấy email nào từ các địa chỉ MEXC'

    return result


bnb_code = mexc_code(username, password)
print(bnb_code)
