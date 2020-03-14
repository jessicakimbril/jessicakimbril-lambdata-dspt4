import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\jessi\OneDrive\Documents\School\Datasets\coronavirus_cleaned_21Jan2Feb.csv')

print(df)

df = df.drop(columns='Unnamed: 0')

print(df)