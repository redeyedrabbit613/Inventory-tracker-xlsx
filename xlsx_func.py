#This function will write the reagent list into an excel file.
import pandas as pd
import openpyxl

#data = {'Reagent':['CLV', 'RTN', 'EXA', 'EXB', 'IMG', 'QCB', 'NSB', 'CSR', 'BLK', 'SIP', 'RXB', 'RIP', 'RXP'],
        #'Quantity':[34, 34, 13, 8, 17, 17, 34, 18, 18, 17, 18, 18, 18]}


def read_xlsx(excel_file):
    try:
        df = pd.read_excel(excel_file)
        print(df)
        exit()   
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        exit()

def add_xlsx(excel_file, reagent, quantity):
    reagent_dic= {'CLV': 0, 'RTN': 1, 'EXA': 2, 'EXB': 3, 'IMG': 4, 'QCB': 5, 'NSB': 6, 'CSR': 7, 'BLK': 8, 'SIP': 9, 'RXB': 10, 'RIP': 11, 'RXP': 12}
    try:
        #convert the reagent input as a value in the reagent_dic
        reagent = reagent_dic[reagent] 
        #load .xlsx file
        df = pd.read_excel(excel_file)
        #look up reagent inventory value and assign it as row_val
        row_val = df.loc[reagent, 'Quantity']
        #subtract the row_val from the quantity input and assign it as row_val
        row_val = row_val + quantity 
        #update the new inventory value for the inventory input as the new row_val value
        df.loc[reagent, 'Quantity'] = row_val
        #write to excel file
        df.to_excel(excel_file, index=False)
        print(df)
        exit()
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        exit()

def sub_xlsx(excel_file, reagent, quantity):
    reagent_dic= {'CLV': 0, 'RTN': 1, 'EXA': 2, 'EXB': 3, 'IMG': 4, 'QCB': 5,'NSB': 6, 'CSR': 7, 'BLK': 8, 'SIP': 9, 'RXB': 10, 'RIP': 11, 'RXP': 12}
    try:
        #convert the reagent input as a value in the reagent_dic
        reagent = reagent_dic[reagent] 
        #load .xlsx file
        df = pd.read_excel(excel_file)
        #look up reagent inventory value and assign it as row_val
        row_val = df.loc[reagent, 'Quantity']
        #subtract the row_val from the quantity input and assign it as row_val
        row_val = row_val - quantity 
        #update the new inventory value for the inventory input as the new row_val value
        df.loc[reagent, 'Quantity'] = row_val
        #write to excel file
        df.to_excel(excel_file, index=False)
        print(df)
        exit()
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        exit()

def add_reag(excel_file, reagent, quantity):
    try:
        df = pd.read_excel(excel_file)
        new_row = pd.DataFrame({'Reagent': [reagent], 'Quantity': [quantity]})
        df = pd.concat([df, new_row], ignore_index=True)
        # Save the DataFrame back to the Excel file
        df.to_excel(excel_file, index=False)
        print(df)
        print(f'Reagent "{reagent}" added successfully.')
        exit()
    except FileNotFoundError:
        print('Error: The file was not found.')
        exit()