import pandas as pd

def subpack(amount):
    amount = int(amount)
    reagent_dic= {'CLV': 0, 'RTN': 1, 'EXA': 2, 'EXB': 3, 'IMG': 4, 'QCB': 5,'NSB': 6, 'CSR': 7, 'BLK': 8, 'SIP': 9, 'RXB': 10, 'RIP': 11, 'RXP': 12}
    excel_file = 'reagents.xlsx'
    df = pd.read_excel(excel_file)
    df.loc[0, 'Quantity'] = (df.loc[0, 'Quantity'] - amount * (2))
    df.loc[1, 'Quantity'] = (df.loc[1, 'Quantity'] - amount * (2))
    df.loc[2, 'Quantity'] = (df.loc[2, 'Quantity'] - amount * (1))
    df.loc[3, 'Quantity'] = (df.loc[3, 'Quantity'] - amount * (1))
    df.loc[4, 'Quantity'] = (df.loc[4, 'Quantity'] - amount * (1))
    df.loc[5, 'Quantity'] = (df.loc[5, 'Quantity'] - amount * (1))
    df.loc[6, 'Quantity'] = (df.loc[6, 'Quantity'] - amount * (2))
    df.loc[7, 'Quantity'] = (df.loc[7, 'Quantity'] - amount * (1))
    df.loc[8, 'Quantity'] = (df.loc[8, 'Quantity'] - amount * (1))
    df.loc[9, 'Quantity'] = (df.loc[9, 'Quantity'] - amount * (1))
    df.loc[10, 'Quantity'] = (df.loc[10, 'Quantity'] - amount * (1))
    df.loc[11, 'Quantity'] = (df.loc[11, 'Quantity'] - amount * (1))
    df.loc[12, 'Quantity'] = (df.loc[12, 'Quantity'] - amount * (1))
    df.to_excel(excel_file, index=False)
    print(str(amount) + " pack(s) successfully removed.")
subpack(3)