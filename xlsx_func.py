#This function will write the reagent list into an excel file.
import pandas as pd

#data = {'Reagent':['CLV', 'RTN', 'EXA', 'EXB', 'IMG', 'QCB', 'NSB', 'CSR', 'BLK', 'SIP', 'RXB', 'RIP', 'RXP'],
        #'Quantity':[34, 34, 13, 8, 17, 17, 34, 18, 18, 17, 18, 18, 18]}


def read_xlsx(excel_file):
    excel_file = 'reagents.xlsx'
    try:
        df = pd.read_excel(excel_file)
        print(df)   
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        exit(1)

def write_xlsx(excel_file, reagent, quantity):
    #load the excel file
    excel_file = 'reagents.xlsx'
    try:
        df = pd.read_excel(excel_file)
        #Modify the Dataframe as needed
        #Define the reagent you want to change and the amount you want to change
        quantity = int(quantity)
        #Change the quantity of a specific reagent
        df.loc[df['Reagent'] == reagent, 'Quantity'] = quantity
        #Save the modified DataFrame back to the Excel file
        df.to_excel(excel_file, index=False)
        print(df)
    except FileNotFoundError:
        print('Error: The file "reagents.xlsx" was not found.')
        exit(1)
