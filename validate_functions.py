import pandas as pd
import numpy as np

def checkVictSex() :
    filepath = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(filepath)

    column = 'Vict Sex'

    if column in df.columns:
        hasNull = df[column].isnull().any()
        notMF = df[column].apply(lambda x: x not in ['M', 'F']).any()
        if(hasNull or notMF):
            return False
    return True

def checkVictAge() :
    filepath = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(filepath)

    column = 'Vict Age'

    if column in df.columns:
        hasNull = df[column].isnull().any()
        notInRange = df[column].apply(lambda x: x < 0 or x > 100).any()
        if(hasNull or notInRange):
            return False
    return True

print (checkVictSex())
print(checkVictAge())