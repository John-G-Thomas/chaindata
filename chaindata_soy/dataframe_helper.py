"""
Function cleans dataframe
"""
import pandas as pd
from comtypes.npsupport import datetime64


def clean(df):
    df = df.copy()
    # Drop NaN and extra columns and index
    df.dropna(subset=[df.select_dtypes(include=['datetime64'])], inplace=True)
    df.set_index(pd.to_datetime(df.select_dtypes(include=['datetime64'])), inplace=True)
    assert isinstance(df, datetime64)
    return df


"""
clean datas and add pecific columns# def cleandate(df):
"""


def date(df):
    df = df.copy()
    df['Year'] = (df.select_dtypes(include=['datetime64']).to_period('Y'))
    df['Month'] = (df.select_dtypes(include=['datetime64']).to_period('M'))
    df['Day'] = (df.select_dtypes(include=['datetime64']).to_period('D'))
    return df
