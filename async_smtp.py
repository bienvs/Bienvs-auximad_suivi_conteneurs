import asyncio, threading
import mailbox
import smtplib, smtpd, smtpd
import ssl
import datetime


verifier = smtplib.SMTPConnectError(code=404, msg="Error, Connection Lost!")
auth = smtplib.SMTPAuthenticationError(code=303, msg="Warning, No Authorization!")
collector = smtplib.SMTP(host="github.com", port="345", source_addres="transporteur")




"""Email Transporteur @ProtonMail_app:
    Titre Sujet{enlèvement, expédition, restitution, réception}, 
    _date_automatique
    _one_of_registered_truck_driver
    __code_anti_phishing_attack
"""