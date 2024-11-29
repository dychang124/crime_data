import pandas as pd
import numpy as np

def calcMean() :
    filepath = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(filepath)

    column = 'Vict Age'

    return df[column].mean()

def calcMedian() :
    filepath = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(filepath)

    column = 'Vict Age'

    return df[column].median()

print(calcMean())
print(calcMedian())