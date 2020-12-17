import pandas as pd
import numpy


def table_creating() -> None:
    file = "Dannye_po_VUZam.csv"
    chunker = pd.read_table(file, chunksize=10000, encoding='windows-1251')
    for chunk in chunker:
        print(chunk.values)


if __name__ == "__main__":
    table_creating()
