"""
    info: dict = Sms.phone.puce4G
        .filter(correspondances=[transporteurs, agences])
        .transfer_api_through_USBWire()
    return async(get(info))
"""

'''
    .transfer_api_through_USBWire()
        phone must be scanned by Avast_&_361 
        phone must have malware_scanner


    if the transporteur ever crashes on way:
        send sms/mail to agency
        call phone agence
'''