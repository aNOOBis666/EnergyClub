import pandas as pd
import numpy as np


def table_creating():
    ml = pd.read_csv('Dannye_po_VUZam.csv', sep=';', encoding='windows-1251')
    ml_2 = pd.read_csv('grnti.csv', sep=';', encoding='windows-1251')
    ml.head()
    ml_2.head()
    result_ml = type_replace(ml)

    return ml, ml_2, result_ml


def type_replace(data):
    data = data.replace({'Not Available': np.nan})
    # print(data.info())
    for row in list(data.row):
        data[row].replace('.', '')
    # Iterate through the columns
    for col in list(data.columns):
        if ('Responsible for information' in col or '№ p/p' in col or 'Agreement, №' in col or 'Structural unit 1' in
                col or 'Structural unit 2' in col or 'Name' in col or 'Leader' in col or 'Customer' in col or 'Customer sector' in
                col or 'Average cost of the entire contract' in col or 'Grant' in col or 'Co-contractor / subcontractor' in
                col or 'Financing' in col or 'Type of work' in col or 'Service type' in col or 'type of service' in
                col or 'Direction XX.00.00' in col or 'Direction XX.XX.00' in
                col or 'Direction XX.XX.XX' in col or 'TRL level' in col or 'Patents (Numbers)' in col):
            # Convert the data type to float
            data[col] = data[col].astype(float)
            print(data[col])
    return data


def take_groups():
    pass


if __name__ == "__main__":
    table_creating()
