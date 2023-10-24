import ast
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

def send_noti(min_value, max_value):
    sender_email = 'mailertesta1@gmail.com'  
    sender_password = 'eipfbfmothdbhexo'         
    recipient_email = 'bobbot33@outlook.com' 
    smtp_server = 'smtp.gmail.com'          
    smtp_port = 587                              
    
        
    try:
        excel_file = 'reagents.xlsx'
        df = pd.read_excel(excel_file)
        excel_dict = df.to_dict(orient='list')
        inv_val = excel_dict['Quantity']
        min_value = min(inv_val)
        max_value = max(inv_val)    
    except (ValueError, SyntaxError):
        print('Error: Unable to convert the file content to a dictionary.')
        exit(1) 
    if min_value < (max_value / 2):
        subject = "Alert: It's Time to Order More Reagents"
        body = f'Please order more reagents. Inventory has dropped below halfway point.'
    else:
        subject = 'No Alert'
        body = f'Plenty of Inventory.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print('Email notification sent successfully.')
    except Exception as e:
        print('Email notification could not be sent. Error:', str(e))
try:
    excel_file = 'reagents.xlsx'
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    print('Error: The file was not found.')
    exit(1)
try:
    excel_dict = df.to_dict(orient='list')
    inv_val = excel_dict['Quantity']
    min_value = min(inv_val)
    max_value = max(inv_val)
    if not isinstance(excel_dict, dict):
        raise ValueError('The file does not contain a valid dictionary.')
except (ValueError, SyntaxError):
    print('Error: Unable to convert the file content to a dictionary.')
    exit(1)

send_noti(min_value, max_value)
