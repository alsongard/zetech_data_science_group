import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

df = pd.read_csv("./myData/coaster_db.csv")
print(df)
print(df.columns)
print(df.describe())
# pd.option_context("display.max_rows, 250"):
print("\n")
new_df = df.copy()
print(new_df)
print(type(new_df))

print("\n")
new_column_df  = new_df[['coaster_name','Length','Speed','Location','Status','Opening date', 'Type','year_introduced','latitude','longitude','Gforce_clean']]
print(new_column_df.columns)

#conversion of date to time 
print(new_column_df.isnull().sum())
print(new_column_df.duplicated().sum())
print("only opening date")
print(new_column_df["Opening date"])
print(type(new_column_df["Opening date"]))
# new_column_df["opening_date"] = pd.to_datetime(new_column_df["Opening date"])