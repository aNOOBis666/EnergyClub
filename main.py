import pandas as pd
import numpy as np


def table_creating():
    ml = pd.read_csv('Dannye_po_VUZam.csv', sep=';', encoding='windows-1251')
    ml_2 = pd.read_csv('grnti.csv', sep=';', encoding='windows-1251')
    ml.head()
    ml_2.head()

    return ml, ml_2


def take_groups():
    # выделение структурного подразделения и руководителя
    pass


if __name__ == "__main__":
    table_creating()
