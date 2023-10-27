import pandas as pd
import openpyxl

def add_reag(excel_file, reagent, quantity):
        excel_file = 'reagents.xlsx'
        try:
                df = pd.read_excel(excel_file)
                new_row = pd.DataFrame({'Reagent': [reagent], 'Quantity': [quantity]})
                df = pd.concat([df, new_row], ignore_index=True)
                # Save the DataFrame back to the Excel file
                df.to_excel(excel_file, index=False)
                print(f'Reagent "{reagent}" added successfully.')
        except FileNotFoundError:
            print('Error: The file was not found.')
add_reag('reagents.xlsx', 'RED', 2)
