# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:21:57 2023

@author: John Wang
"""
import pandas as pd
from min_max import min_max
from email_noti_xlsx import send_noti
#This function will check the inventory and send an email notification if the inventory is below the set amount.
excel_file = 'reagents.xlsx'
def checkinv(excel_file):
    excel_file = 'reagents.xlsx'
    df= pd.read_excel(excel_file)
    lst_min = min(df['Quantity'])
    if lst_min < 10:
        min_max(excel_file)
    print(df)
    
checkinv(excel_file)