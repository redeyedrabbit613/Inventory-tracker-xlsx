import pandas as pd
from xlsx_func import read_xlsx
from min_max import min_max

excel_file = 'reagents.xlsx'
df = pd.read_excel(excel_file)
excel_dict = df.to_dict(orient='list')
inv_val = excel_dict['Quantity']
min_value = min(inv_val)
max_value = max(inv_val)
if min_value < (max_value/2):
    print('works')
    print(min_value)
    print(max_value)
else:
    print('wrong')
