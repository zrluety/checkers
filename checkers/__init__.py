import pandas as pd


def find_unique(filepath):
    df = pd.read_csv(filepath)

    for column in df:        
        duplicates = df[df.duplicated([column], keep=False)]
        if duplicates.empty:
            return True

    return False