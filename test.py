import pandas as pd
excel_file = 'reagents.xlsx'
reagent = 'CLV'
quantity = 2

df = pd.read_excel(excel_file)
        #Modify the Dataframe as needed
        #Define the reagent you want to change and the amount you want to change
        #Define current inventory quantity
row_val = df.loc[0, 'Quantity']
print(row_val)