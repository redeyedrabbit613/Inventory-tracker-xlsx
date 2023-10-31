#This function will write the reagent list into an excel file.
import pandas as pd
import openpyxl
import sys

#data = {'Reagent':['CLV', 'RTN', 'EXA', 'EXB', 'IMG', 'QCB', 'NSB', 'CSR', 'BLK', 'SIP', 'RXB', 'RIP', 'RXP'],
        #'Quantity':[34, 34, 13, 8, 17, 17, 34, 18, 18, 17, 18, 18, 18]}


def read_xlsx(excel_file):
    try:
        df = pd.read_excel(excel_file)
        print(df)
        sys.exit(0)   
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        sys.exit(0)

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
        sys.exit(0)
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        sys.exit(1)

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
        sys.exit(0)
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        sys.exit(1)

def add_reag(excel_file, reagent, quantity):
    try:
        df = pd.read_excel(excel_file)
        new_row = pd.DataFrame({'Reagent': [reagent], 'Quantity': [quantity]})
        df = pd.concat([df, new_row], ignore_index=True)
        # Save the DataFrame back to the Excel file
        df.to_excel(excel_file, index=False)
        print(df)
        print(f'Reagent "{reagent}" added successfully.')
        sys.exit(0)
    except FileNotFoundError:
        print('Error: The file was not found.')
        sys.exit(1)
        
def subpack(excel_file, quantity):
    try:
       quantity= int(quantity) 
       df = pd.read_excel(excel_file)
       # Convert the 'Quantity' column to int64 if it's not already
       df['Quantity'] = df['Quantity'].astype('int64')
       df.loc[0, 'Quantity'] = (df.loc[0, 'Quantity'] - quantity * (2))
       df.loc[1, 'Quantity'] = (df.loc[1, 'Quantity'] - quantity * (2))
       df.loc[2, 'Quantity'] = (df.loc[2, 'Quantity'] - quantity * (1))
       df.loc[3, 'Quantity'] = (df.loc[3, 'Quantity'] - quantity * (1))
       df.loc[4, 'Quantity'] = (df.loc[4, 'Quantity'] - quantity * (1))
       df.loc[5, 'Quantity'] = (df.loc[5, 'Quantity'] - quantity * (1))
       df.loc[6, 'Quantity'] = (df.loc[6, 'Quantity'] - quantity * (2))
       df.loc[7, 'Quantity'] = (df.loc[7, 'Quantity'] - quantity * (1))
       df.loc[8, 'Quantity'] = (df.loc[8, 'Quantity'] - quantity * (1))
       df.loc[9, 'Quantity'] = (df.loc[9, 'Quantity'] - quantity * (1))
       df.loc[10, 'Quantity'] = (df.loc[10, 'Quantity'] - quantity * (1))
       df.loc[11, 'Quantity'] = (df.loc[11, 'Quantity'] - quantity * (1))
       df.loc[12, 'Quantity'] = (df.loc[12, 'Quantity'] - quantity * (1))
       df.to_excel(excel_file, index=False)
       print(str(quantity) + " pack(s) successfully removed.")
       sys.exit(0) 
    except FileNotFoundError:
       print('Error: The file was not found.')
       sys.exit(1)