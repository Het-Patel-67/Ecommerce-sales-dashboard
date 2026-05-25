# data_cleaning.py

import pandas as pd


def load_and_clean_data(filepath):
    
    df = pd.read_csv(filepath)

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # fill missing ratings
    df["Rating"] = df["Rating"].fillna(
        df["Rating"].mean()
    )

    # convert date
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"]
    )

    # remove invalid prices
    df = df[df["Price"] > 0]

    # standardize category names
    df["Category"] = (
        df["Category"]
        .str.strip()
        .str.title()
    )

    # revenue calculation
    df["Revenue"] = (
        df["Price"] *
        df["Quantity"]
    ) - df["Discount"]

    return df