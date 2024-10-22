import datetime as dt
import asyncio, threading
import smtp, smtpd, smtplib
from config import SOURCE_MAIL


connected = smtpd.SMTPChannel.connect(address=SOURCE_MAIL)
if connected: 
    print("CONNECTION SET!")
    # do whatever as planned
    """async_notif_mail"""
else: print("CONNECTION LOST!")
