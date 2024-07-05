import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup


username = "NogglerZebley992@gmail.com"
password = "wxluiehdpdfqvaih"
def binance_code(userName, passWord):

    result = ''  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    if mail.login(username,password):

        #print('Email Login Succesful')
        mail.select('INBOX')

        from_emails = ['do-not-reply@directmail2.binance.com']

        status, messages = mail.search(None, f'(FROM "{from_emails}")')
        #print('Messages: ', messages)

        email_ids = messages[0].split()
        #print('Email IDs: ', email_ids)

        last_email = email_ids[-1]
        #print('Last Email: ', last_email)

        status, msg_data = mail.fetch(last_email,'(RFC822)')
        #print('Messages Data: ', msg_data[0])

        for reponse_data in msg_data:
            if isinstance(reponse_data,tuple):
                msg = email.message_from_bytes(reponse_data[1])

                #print('Decode Message Data: ',msg)
                
        subject = msg['Subject']
        decode_subject = decode_header(subject)
        subject_title = ''
        for part, endcoding in decode_subject:
            if isinstance(part, bytes):
                subject_title += part.decode(endcoding, 'utf-8')
            else:
                subject_title += part

        # print('Subject: ',subject)
        # print('decode_subtitle: ', decode_subject)
        # print('subject_title: ', subject_title)

        payload = msg.get_payload(decode=True)
        #print('Payload: ', payload)

        body = payload.decode()
        #print('Body: ',body)

        soup = BeautifulSoup(body,'html.parser')
        get_binance_code = soup.find('div', style="font-family: BinancePlex,Arial,PingFangSC-Regular,'Microsoft YaHei',sans-serif; font-size: 18px; line-height: 30px; text-align: left; color: #f0b90b;")
        binance_code = get_binance_code.get_text()
        result = subject_title + ' - Code: ' + binance_code
        #print(result)
    else:
        print('Email Login Failed')
    return result

bnb_code = binance_code(username,password)
print(bnb_code)










