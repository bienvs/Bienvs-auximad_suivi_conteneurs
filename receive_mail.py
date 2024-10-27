import os, imaplib, email
import dotenv 
dotenv.load_dotenv()

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(
    os.environ["EMAIL_HOST_USER"],
    os.environ["EMAIL_HOST_PASSWORD"]
)
mail.select('inbox')
status, messages = mail.search('utf-8', 'UNSEEN')
for num in messages[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    
    print('Subject: ', msg['Subject'])
    print('From: ', msg['From'])
    
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            print(part.get_payload())

mail.close()
mail.logout()