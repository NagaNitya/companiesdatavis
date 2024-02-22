import pandas as pd
import re

def conv_bil(market_cap_str):
    match=re.search(r'\$(\d+\.?\d*)\s*(B|T)', market_cap_str) # check for the specified pattern in the string
    if match:
        value, unit=match.groups()
        value=float(value)
        return (value*1000 if unit=='T' else value)
    return 0

def load_csv(file_path):
    #load csv file and process Market Cap (USD) column
    df = pd.read_csv(file_path, index_col=0)
    df['Market Cap (USD) Numerical']=df['Market Cap (USD)'].apply(conv_bil) # apply() passes each record as input to the functiion given
    return df

def filter_df(df, excluded_companies):
    if excluded_companies:
        exclude_list=[i.strip() for i in excluded_companies.split("_")] # separate each company name from the string of comma separated values and remove extra whitespaces
        return df[~df['Company'].isin(exclude_list)]
    return df