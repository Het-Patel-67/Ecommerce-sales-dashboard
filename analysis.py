# analysis.py

import numpy as np


def total_revenue(df):
    return df["Revenue"].sum()


def average_order_value(df):
    return np.mean(df["Revenue"])


def total_orders(df):
    return len(df)


def top_products(df):

    return (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )


def category_sales(df):

    return (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def state_sales(df):

    return (
        df.groupby("State")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def monthly_sales(df):

    temp = df.copy()

    temp["Month"] = (
        temp["Order_Date"]
        .dt.strftime("%Y-%m")
    )

    return (
        temp.groupby("Month")["Revenue"]
        .sum()
    )