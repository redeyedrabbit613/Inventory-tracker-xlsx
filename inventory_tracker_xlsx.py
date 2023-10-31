#This function will create a dictionary to sort and track the inventory of reagents. Reagent are the keys and the inventory count is the value.
import ast
import pandas as pd
from email_noti_xlsx import send_noti
from xlsx_func import add_xlsx
from xlsx_func import sub_xlsx
from xlsx_func import add_reag
from xlsx_func import subpack
from min_max import min_max
#reagents ={'CLV': '0', 'RTN': '0', 'EXA': '0', 'EXB': '0', 'IMG': '0', 'QCB': '0', 'NSB': '0', 'CSR': '0', 'BLK': '0', 'SIP': '0', 'RXB': '0', 'RIP': '0', 'RXP': '0'}


prmpt = ('To check inventory enter "1"'
        '\nTo add a new reagent to the list enter "2"'
        '\nTo add to reagent(s) to the inventory enter "3"'
        '\nTo take away from a reagent(s) from the inventory enter "4"'
        '\nTo take away a reagent pack(s) worth of reagents from the inventory eneter "5"')
print(prmpt)

prmpt_input = input('What would you like to do?')
for res in prmpt_input:
    if res == '1':
        excel_file = 'reagents.xlsx'
        min_max(excel_file)
        break
    if res == '2':
        excel_file = 'reagents.xlsx'
        reagent = input('What reagent would you like to add to the inventory list: ')
        quantity = int(input('How many would you like to add to the inventory: '))
        add_reag(excel_file, reagent, quantity)
        break
    if res == '3':
        excel_file = 'reagents.xlsx'
        reagent = input('What reagent inventory would you like to add to: ')
        quantity = input('How many would you like to add to the inventory: ')
        quantity = int(quantity)
        add_xlsx(excel_file, reagent, quantity)
        break
    if res == '4':
        excel_file = 'reagents.xlsx'
        reagent = input('What reagent inventory would you like to take away from: ')
        quantity = input('How many would you like to take away from the inventory: ')
        quantity = int(quantity)
        sub_xlsx(excel_file, reagent, quantity)
        break
    if res =='5':
        excel_file = 'reagents.xlsx'
        quantity = input('How many would you like to take away from the inventory: ')
        subpack(excel_file, quantity)
        min_max(excel_file)
        break
    