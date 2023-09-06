import pandas as pd

def data_summary(path):
    # create the data summary
    df = pd.read_csv(path)
    return df['SEQPLT16'].mean()

