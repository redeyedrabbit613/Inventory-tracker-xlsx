#This funciton will convert the data to a dictionary. It will then identify the min and max value for the dictionary.
import pandas as pd
from email_noti_xlsx import send_noti
#load the Excel file into a DataFrame
def min_max(excel_file):
    excel_file= 'reagents.xlsx'
    try:
        df = pd.read_excel(excel_file)
        #Convert DataFrame to a dictionary
        excel_dict = df.to_dict(orient='list')
        inv_val = excel_dict['Quantity']
        min_value = min(inv_val)
        max_value = max(inv_val)
        send_noti(min_value, max_value)
        print(reagents)
        exit(1)
    except(ValueError, SyntaxError):
        print('Error: Unable to convert the file content to a dictionary.')
        exit(1)


